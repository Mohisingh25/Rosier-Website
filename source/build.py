import re
#!/usr/bin/env python3
"""Builds the Rosier Foods static site redesign.
Product images are hotlinked from the live rosierfoods.com Shopify CDN (see data.py)."""
import os, re, shutil, html, sys

SRC = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SRC)
from data import PRODUCTS, BY, BEST, NEW, COLLECTIONS, HOME, TESTI, GHEE_GALLERY, img, SITE, LABMAP, NEEDS, PH, MANUFACTURERS, POLICY, INFO, info_key, VARIANTS, GUIDES, CONTACT_EMAIL, VIDS, KEYWORDS, PLANS, JOIN_URL
import json

OUT = os.path.dirname(SRC) if os.path.basename(SRC) == 'source' else os.path.join(os.path.dirname(SRC), 'rosier-site')

COL = {c[0]: c for c in COLLECTIONS}
CAT_OF = {}
for key, *_r, handles in COLLECTIONS:
    for h in handles:
        CAT_OF.setdefault(h, key)

LAB = [
    ('dairy', [('Gir Cow A2 Ghee', 'merged.pdf?v=1768202574'), ('Malai Paneer', 'Paneer_-112.pdf?v=1753244027')]),
    ('immunity', [('Wild Forest Honey', 'Wild_Forest_Honey.pdf?v=1765369651'), ('Ginger Honey', 'Ginger_Honey_-174.pdf?v=1765641667'), ('Amlaprash', 'Amlaprash_Lab_Report.pdf?v=1765543072')]),
    ('oils', [('Stone Pressed Mustard Oil', 'Black_Mustard_Oil_Lab_Report.pdf?v=1765370195'), ('Stone Pressed Yellow Mustard Oil', 'Yellow_Mustard_Oil_Lab_Report.pdf?v=1765371322'),
              ('Stone Pressed Groundnut Oil', 'Groundnut_Oil_Lab_Report.pdf?v=1765370419'), ('Stone Pressed Coconut Oil', 'Coconut_Oil_Lab_Report.pdf?v=1765370726'),
              ('Stone Pressed Sunflower Oil', 'Sunflower_Oil-020.pdf?v=1765371422'), ('Stone Pressed Sesame Oil', 'ROSIER_WHITE_SESAME20251001_15433420.pdf?v=1788259530'),
              ('Stone Pressed Olive Oil', 'Olive_Oil-023.pdf?v=1788259531')]),
    ('atta', [('Khapli Atta', 'Khapli_Atta_Lab_Report.pdf?v=1765368662'), ('Multigrain Flour', '200-Multigrain_flour_Atta.pdf?v=1776080054'),
              ('Sattu Flour', 'Test_report_of_Sattu_-_206.pdf?v=1776080054'), ('Jowar Flour', 'Test_report_of_Jowar_Flour-202.pdf?v=1776080054'),
              ('Ragi Flour', 'Test_report_of_Ragi_Flour-201.pdf?v=1776080054')]),
    ('breakfast', [('Banana Cinnamon Oats', 'fa20260212-027-114.pdf?v=1776513445'), ('Cafe Mocha Oats', 'fa20260212-027-115.pdf?v=1776513627'),
                   ('Double Chocolate Oats', 'fa20260212-027-116.pdf?v=1776513712'), ('Mango Oats', 'High_Protein_Oats_-_Mango_-033.pdf?v=1788249684'),
                   ('Kulfi Oats', 'Overnight_Oats_Kulfi_-079.pdf?v=1788249685'), ('Better Bars', 'Rosier_foods_Protein_Bar.pdf?v=1749046679'),
                   ('Nut Butter', 'Nut_Butter_Lab_Report.jpg?v=1749047175'), ('Nut Butter Crunchy', 'Nut_Butter_Crunchy_Lab_Report.jpg?v=1749047175'),
                   ('Nut Butter Dark Chocolate', 'Dark_Chocolate_Nut_Butter_Lab_Report.jpg?v=1749047175'), ('Almond Butter Crunchy', 'Almond_Butter_Crunchy_Lab_Report.jpg?v=1749047175')]),
    ('pickles', [('Mango Pickle', 'Mango_pickle.pdf?v=1788250646'), ('Red Chilli Pickle', 'Red_Chilli_pickle.pdf?v=1788249685'),
                 ('Green Chilly Pickle', 'green_chilli_pickle.pdf?v=1788259532'), ('Lemon Pickle', '204-Nimbu_Masala_Pickle.pdf?v=1788266555'),
                 ('Sweet Lemon Pickle', 'Sweet_lemon_Pickle.pdf?v=1788249685')]),
]
LABCAT = {'dairy': 'Ghee & Dairy', 'immunity': 'Honey & Immunity', 'oils': 'Stone Pressed Oils', 'atta': 'Atta & Flours',
          'breakfast': 'Breakfast & Nut Butters', 'pickles': 'Pickles'}


def inr(n):
    whole, dec = (f"{n:.2f}".split('.')) if n % 1 else (str(int(n)), '')
    if len(whole) > 3:
        head, tail = whole[:-3], whole[-3:]
        head = re.sub(r'(\d)(?=(\d\d)+$)', r'\1,', head)
        whole = head + ',' + tail
    return '₹' + whole + ('.' + dec if dec else '')


def off(p, m): return round((1 - p / m) * 100)
def purl(h): return f'product-{h}.html'
def curl(k): return f'collection-{k}.html'


SPRITE = open(os.path.join(SRC, 'partials', 'sprite.html')).read()


def stars(r, n=None):
    if not r:
        return '<span class="stars">New launch</span>'
    extra = f' · {n}' if n else ''
    return f'<span class="stars"><svg><use href="#i-star"/></svg><b>{r:.1f}</b>{extra}</span>'


def pack(size):
    s = size.lower()
    return 'bulk' if ('5 l' in s or '5 kg' in s) else 'combo' if ('pack of' in s or '×' in s) else 'single'


def ptype(h):
    k = CAT_OF.get(h, '')
    return {'ghee': 'Ghee', 'stone-press-oil': 'Oils', 'pickles': 'Pickles', 'atta': 'Atta & grains', 'healthy-snacking': 'Breakfast',
            'immunity-booster': 'Honey & Amlaprash', 'honey': 'Honey & Amlaprash', 'nut-butters': 'Breakfast'}.get(k, 'Festive & sweets')


def srcset(u, sizes='(max-width:600px) 50vw, 300px'):
    return f'srcset="{img(u, 300)} 300w, {img(u, 600)} 600w" sizes="{sizes}"'


def pcard(h, cls='reveal', delay=0):
    hd, n, size, price, mrp, r, badge, i1, i2 = BY[h]
    d = f' style="--d:{delay:.2f}s"' if delay else ''
    b = f'<span class="pcard__badge">{badge}</span>' if badge else ''
    o = off(price, mrp)
    return f'''<article class="pcard {cls}"{d} data-cat="{CAT_OF.get(h, 'other')}" data-type="{ptype(h)}" data-price="{price}" data-rating="{r}" data-off="{o}" data-pack="{pack(size)}" data-i="{PRODUCTS.index(BY[h])}">
  <a href="{purl(h)}" class="pcard__img" tabindex="-1" aria-hidden="true">{b}
    <img class="pcard__a" src="{img(i1, 600)}" {srcset(i1)} alt="" loading="lazy" width="600" height="600">
    <img class="pcard__b" src="{img(i2, 600)}" {srcset(i2)} alt="" loading="lazy" width="600" height="600"></a>
  <button class="pcard__qv" data-qv="{h}" aria-label="Quick view: {html.escape(n)}"><svg aria-hidden="true"><use href="#i-eye"/></svg></button>
  <div class="pcard__quick"><button class="btn-add" data-h="{h}" aria-label="Add {html.escape(n)} to cart">Add to cart</button></div>
  <div class="pcard__body">
    <h3 class="pcard__name"><a href="{purl(h)}">{html.escape(n)}</a></h3>
    <span class="pcard__size">{size} · {stars(r)}</span>{'<span class="pcard__lab"><svg aria-hidden="true"><use href="#i-flask"/></svg>Lab report available</span>' if h in LABMAP else ''}
    <div class="pcard__price"><b>{inr(price)}</b>{f'<s aria-label="MRP">{inr(mrp)}</s><em>{o}% off</em>' if mrp > price else ''}</div>
    <div class="pcard__add"><button class="btn-add" data-h="{h}" aria-label="Add {html.escape(n)} to cart">Add</button></div>
  </div>
</article>'''


def carousel(cid, handles):
    return f'<div class="carousel reveal" data-carousel="{cid}"><div class="carousel__track" tabindex="0" aria-label="Products, scroll sideways">{"".join(pcard(h, "") for h in handles)}</div></div>'


def car_btns(cid):
    return f'''<div class="car-btns"><button class="car-btn car-btn--prev" data-car="{cid}" aria-label="Previous products"><svg aria-hidden="true"><use href="#i-arrow"/></svg></button><button class="car-btn" data-car="{cid}" aria-label="Next products"><svg aria-hidden="true"><use href="#i-arrow"/></svg></button></div>'''


def eyebrow(t, center=False, light=False):
    c = (' eyebrow--center' if center else '') + (' eyebrow--light' if light else '')
    flip = ' <svg class="wheat flip" aria-hidden="true"><use href="#i-wheat"/></svg>' if center else ''
    return f'<p class="eyebrow{c}"><svg class="wheat" aria-hidden="true"><use href="#i-wheat"/></svg> {t}{flip}</p>'


# Navigation exactly as specified in the brief
NAV = [('shop', 'Shop All', 'shop.html'), ('ghee', 'Ghee', curl('ghee')), ('oils', 'Oils', curl('stone-press-oil')), ('atta', 'Atta & Grains', curl('atta')),
       ('pickles', 'Pickles', curl('pickles')), ('breakfast', 'Breakfast', curl('healthy-snacking')), ('story', 'Our Story', 'our-story.html')]
STORY = [('our-story.html', 'Our Story'), ('founder.html', 'Our Founder'), ('farmers.html', 'Our Farmers'), ('process.html', 'Our Process'),
         ('philosophy.html', 'Our Philosophy'), ('commitment.html', 'Our Commitment'), ('standards.html', 'Know Your Food (Standards)'),
         ('membership.html', 'Rosier Parivaar Membership'), ('hampers.html', 'Hampers & Gifting')]
LOGO = f'<img src="{HOME["logo"]}" alt="Rosier Foods" width="80" height="58" onerror="this.onerror=null;this.src=\'assets/img/rosier-logo-green.png\'">'


def header(active):
    links = []
    for key, label, href in NAV:
        cur = ' aria-current="page" class="active"' if key == active else ''
        if key == 'shop':
            cats = ''.join(f'<a href="{curl(k)}"><img src="{img(t, 120)}" alt="" width="44" height="44">{n}</a>' for k, n, t, *_ in COLLECTIONS)
            needs = ''.join(f'<a href="index.html#need-{k}">{n}</a>' for k, n, *_ in NEEDS)
            drop = (f'<div class="drop__col"><p class="drop__h">Shop by category</p>{cats}</div>'
                    f'<div class="drop__col drop__need"><p class="drop__h">Shop by need</p>{needs}<p class="drop__h" style="margin-top:12px">Gifting</p><a href="hampers.html">Parampara Diwali Hampers</a><a href="membership.html">Rosier Parivaar Membership</a></div>'
                    f'<a class="drop__feat" href="product-a2-desi-cow-ghee-hand-churned-from-curd.html"><img src="{img(BY[BEST[0]][7], 500)}" alt=""><span>Our bestseller: Hand-churned A2 Bilona Ghee →</span></a>')
            links.append(f'<div class="has-drop"><a href="{href}"{cur} aria-haspopup="true">{label}<svg class="chev" aria-hidden="true"><use href="#i-chev"/></svg></a>'
                         f'<div class="drop">{drop}<a class="drop__all" href="shop.html">Shop all {len(PRODUCTS)} products →</a></div></div>')
        elif key == 'story':
            sl = ''.join(f'<a href="{u}">{n}</a>' for u, n in STORY)
            links.append(f'<div class="has-drop"><a href="{href}"{cur} aria-haspopup="true">{label}<svg class="chev" aria-hidden="true"><use href="#i-chev"/></svg></a><div class="drop drop--sm">{sl}</div></div>')
        else:
            links.append(f'<a href="{href}"{cur}>{label}</a>')
    sub = ''.join(f'<a href="{curl(k)}">{n}</a>' for k, n, *_ in COLLECTIONS)
    ssub = ''.join(f'<a href="{u}">{n}</a>' for u, n in STORY[1:])
    drawer = ''.join(f'<a href="{h}">{l}</a>' + (f'<div class="drawer__sub">{sub}</div>' if k == 'shop' else f'<div class="drawer__sub">{ssub}</div>' if k == 'story' else '')
                     for k, l, h in NAV if k in ('shop', 'story'))
    return f'''
<div class="announce" role="region" aria-label="Announcement"><p>Diwali Sale is live: up to 30% off, plus a free bottle on orders above ₹2,499. <a href="faq.html#offers">Offer details</a></p></div>
<header class="header" id="top"><div class="container header__inner">
  <button class="burger" data-drawer aria-label="Open menu" aria-expanded="false" aria-controls="drawer"><svg aria-hidden="true"><use href="#i-menu"/></svg></button>
  <a class="logo" href="index.html" aria-label="Rosier Foods home">{LOGO}</a>
  <nav class="nav" aria-label="Main">{''.join(links)}</nav>
  <div class="header__actions">
    <form class="search" role="search" action="shop.html"><svg aria-hidden="true"><use href="#i-search"/></svg><label class="sr-only" for="q-top">Search products</label><input id="q-top" name="q" type="search" placeholder="Search ghee, atta, honey…"></form>
    <a href="{SITE}/account" class="icon-btn" aria-label="Account (opens rosierfoods.com)"><svg aria-hidden="true"><use href="#i-user"/></svg></a>
    <a href="cart.html" class="icon-btn" aria-label="Cart" data-open-cart><svg aria-hidden="true"><use href="#i-bag"/></svg><span class="cart-count" aria-live="polite">0</span></a>
  </div>
</div></header>
<div class="tbar"><div class="container tbar__in"><span><svg aria-hidden="true"><use href="#i-flask"/></svg><a href="lab-reports.html">Lab reports for 32 products</a></span><span><svg aria-hidden="true"><use href="#i-shield"/></svg><a href="standards.html#units">Made in FSSAI-licensed units</a></span><span><svg aria-hidden="true"><use href="#i-truck"/></svg>Usually delivered in 3–5 days</span><span><svg aria-hidden="true"><use href="#i-check"/></svg><a href="standards.html#returns">2-day returns on damaged or wrong items</a></span></div></div>
<div class="drawer" id="drawer"><div class="drawer__scrim" data-drawer></div><div class="drawer__panel" role="dialog" aria-modal="true" aria-label="Menu">
  <div class="drawer__top">{LOGO}<button class="burger" style="display:grid" data-drawer aria-label="Close menu"><svg aria-hidden="true"><use href="#i-close"/></svg></button></div>
  <form class="drawer__search" role="search" action="shop.html"><svg aria-hidden="true"><use href="#i-search"/></svg><label class="sr-only" for="q-drawer">Search products</label><input id="q-drawer" name="q" type="search" placeholder="Search ghee, atta, honey…"></form>
  <a href="index.html">Home</a>{drawer}<a href="standards.html">Know Your Food</a><a href="membership.html">Rosier Parivaar</a><a href="faq.html">FAQs</a><a href="contact.html">Contact Us</a>
</div></div>'''


FOOTER = f'''
<footer class="footer"><div class="container footer__grid">
  <div class="footer__brand">
    <img src="{HOME['logo_green']}&width=240" alt="Rosier Foods" width="96" height="80" loading="lazy" onerror="this.onerror=null;this.src='assets/img/rosier-logo-green.png'">
    <p>Reviving the Tradition of Old Bharat.</p>
    <p class="hindi-line" lang="hi">परंपरा • शुद्धता • ईमानदारी</p>
    <div class="socials"><a href="https://www.facebook.com/rosierfoods/" aria-label="Rosier on Facebook">f</a><a href="https://www.instagram.com/rosier.foods/" aria-label="Rosier on Instagram">ig</a><a href="https://www.youtube.com/@RosierFoods" aria-label="Rosier on YouTube">yt</a></div>
  </div>
  <div><h2 class="f-h">About Rosier</h2><ul><li><a href="our-story.html">Our Story</a></li><li><a href="founder.html">Our Founder</a></li><li><a href="process.html">Our Process</a></li><li><a href="standards.html">Know Your Food</a></li><li><a href="lab-reports.html">Lab Reports</a></li><li><a href="standards.html#units">Manufacturer List</a></li><li><a href="https://forms.gle/cJiXL8BdMAhhRE9y8">Careers</a></li></ul></div>
  <div><h2 class="f-h">Help</h2><ul><li><a href="faq.html">FAQs</a></li><li><a href="{SITE}/policies/shipping-policy">Shipping Policy</a></li><li><a href="{SITE}/policies/refund-policy">Return &amp; Refund Policy</a></li><li><a href="{SITE}/pages/privacy-policy">Privacy Policy</a></li><li><a href="{SITE}/pages/terms-of-service">Terms &amp; Conditions</a></li><li><a href="{SITE}/blogs/lets-cook">Recipes</a></li><li><a href="{SITE}/blogs/news">Blog</a></li></ul></div>
  <div><h2 class="f-h">Customer Support</h2><address>Rosier Foods Pvt. Ltd.<br>Burari, Delhi 110084<br>Sector 6, Noida, Uttar Pradesh 201301</address><ul style="margin-top:12px"><li><a href="mailto:{CONTACT_EMAIL}">{CONTACT_EMAIL}</a></li><li><a href="https://wa.me/919711580581">WhatsApp: +91 97115 80581</a></li><li><a href="contact.html">Contact form</a></li></ul></div>
  <div class="footer__news"><h2 class="f-h">Newsletter</h2>
    <form class="news-form" data-demo novalidate><label class="sr-only" for="nf-email">Email</label><input id="nf-email" type="email" placeholder="Your email" required autocomplete="email"><label class="consent"><input type="checkbox" required> I agree to receive emails from Rosier Foods.</label><button class="btn btn--primary btn--sm" type="submit">Subscribe</button><p class="form-err" role="alert"></p><p class="form-ok" role="status">Thanks! Sign-up confirmation needs the newsletter service to be connected.</p></form>
    <img class="pay-img" src="{HOME['payments']}&width=480" alt="Accepted payment methods: cards, UPI and wallets" loading="lazy" width="240" height="40" onerror="this.style.display='none'">
  </div>
</div><div class="footer__bottom">© 2026 Rosier Foods Private Limited. All rights reserved.</div></footer>
<a class="wa-float" href="https://wa.me/919711580581" aria-label="Chat with Rosier on WhatsApp"><svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2zm5.3 14.1c-.2.6-1.3 1.2-1.8 1.3-.5 0-1 .3-3.2-.7-2.7-1.1-4.4-3.9-4.5-4.1-.1-.2-1.1-1.4-1.1-2.7s.7-1.9.9-2.2c.2-.3.5-.3.7-.3h.5c.2 0 .4 0 .6.5l.8 2c.1.2.1.3 0 .5l-.3.5-.4.4c-.1.1-.3.3-.1.6.2.3.8 1.3 1.7 2.1 1.2 1 2.1 1.3 2.4 1.5.3.1.5.1.6-.1l.9-1.1c.2-.3.4-.2.7-.1l1.9.9c.3.1.5.2.5.3.1.2.1.7-.1 1.2z"/></svg></a>
<nav class="mnav" aria-label="Quick links"><a href="index.html"><svg aria-hidden="true"><use href="#i-leaf"/></svg>Home</a><a href="shop.html"><svg aria-hidden="true"><use href="#i-bag"/></svg>Shop</a><button data-drawer data-focus-search aria-label="Search"><svg aria-hidden="true"><use href="#i-search"/></svg>Search</button><a href="membership.html"><svg aria-hidden="true"><use href="#i-badge"/></svg>Parivaar</a><a href="cart.html" data-open-cart><svg aria-hidden="true"><use href="#i-gift"/></svg>Cart<span class="cart-count">0</span></a></nav>'''


def jsonld(obj):
    return '<script type="application/ld+json">' + json.dumps(obj, ensure_ascii=False) + '</script>'


BASE = 'https://mohisingh25.github.io/Rosier-Website/'
ORG = {"@context": "https://schema.org", "@type": "Organization", "name": "Rosier Foods", "legalName": "Rosier Foods Private Limited", "url": SITE,
       "logo": HOME['logo_green'], "email": CONTACT_EMAIL, "slogan": "Reviving the Tradition of Old Bharat",
       "sameAs": ["https://www.facebook.com/rosierfoods/", "https://www.instagram.com/rosier.foods/", "https://www.youtube.com/@RosierFoods"]}
PAGES_BUILT = []


def optimise_imgs(doc):
    """Performance pass: the first image in <main> loads eagerly with high priority (LCP); every other
    image without a loading attribute is lazy + async-decoded; images without dimensions get a default
    box so the browser reserves space (CSS controls the rendered size)."""
    m = doc.index('<main')
    state = {'first': True}
    def fix(mo):
        tag, pos = mo.group(0), mo.start()
        logo = HOME['logo'].split('?')[0] in tag
        if 'width=' not in tag:
            tag = tag.replace('<img ', '<img width="600" height="600" ', 1)
        if pos > m and state['first'] and 'loading=' not in tag:
            state['first'] = False
            return tag.replace('<img ', '<img fetchpriority="high" ', 1)
        if pos > m: state['first'] = False
        if 'loading=' not in tag and not logo:
            tag = tag.replace('<img ', '<img loading="lazy" ', 1)
        if 'decoding=' not in tag:
            tag = tag.replace('<img ', '<img decoding="async" ', 1)
        return tag
    return re.sub(r'<img [^>]*>', fix, doc)


def page(fname, title, desc, active, body, after='', head=''):
    PAGES_BUILT.append(fname)
    canon = BASE + ('' if fname == 'index.html' else fname)
    doc = f'''<!doctype html>
<html lang="en-IN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{html.escape(desc)}">
<link rel="canonical" href="{canon}">
<meta property="og:type" content="website"><meta property="og:title" content="{html.escape(title)}"><meta property="og:description" content="{html.escape(desc)}"><meta property="og:url" content="{canon}"><meta property="og:image" content="{img(GHEE_GALLERY[0], 1200)}">
<meta name="theme-color" content="#784900">
<link rel="icon" href="assets/img/rosier-logo-green.png">
<link rel="preconnect" href="https://cdn.shopify.com"><link rel="preconnect" href="https://www.rosierfoods.com">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Brygada+1918:ital,wght@0,400;0,500;0,600;1,400;1,500&family=Poppins:wght@300;400;500;600&family=Yathra+One&display=swap" rel="stylesheet">
{head}
<link rel="stylesheet" href="css/base.css">
<link rel="stylesheet" href="css/site.css">
<link rel="stylesheet" href="css/live.css">
<link rel="stylesheet" href="css/bharat.css">
<link rel="stylesheet" href="css/qa.css">
<script src="js/catalog.js" defer></script>
<script src="js/site.js" defer></script>
<script src="js/commerce.js" defer></script>
</head>
<body data-page="{active}" style="--texture:url('{HOME['texture']}')">
<a class="skip" href="#main">Skip to content</a>
{SPRITE}
{header(active)}
<main id="main">
{body}
</main>
{FOOTER}
{after}
{jsonld(ORG) if active == 'home' else ''}
</body>
</html>
'''
    doc = optimise_imgs(doc)
    open(os.path.join(OUT, fname), 'w').write(doc)


def build():
    for d in ('css', 'js', 'assets'):
        if os.path.exists(os.path.join(OUT, d)):
            shutil.rmtree(os.path.join(OUT, d))
    for f in os.listdir(OUT) if os.path.exists(OUT) else []:
        if f.endswith('.html'):
            os.remove(os.path.join(OUT, f))
    os.makedirs(os.path.join(OUT, 'assets', 'img'), exist_ok=True)
    shutil.copytree(os.path.join(SRC, 'css'), os.path.join(OUT, 'css'))
    shutil.copytree(os.path.join(SRC, 'js'), os.path.join(OUT, 'js'))
    for f in os.listdir(os.path.join(SRC, 'img')):
        if not f.startswith('member-') and not f.startswith('ph-'):
            shutil.copy(os.path.join(SRC, 'img', f), os.path.join(OUT, 'assets', 'img', f))
    cat = [dict(h=h, n=n, s=sz, p=pr, m=m, r=r, b=b, i=img(i1, 10).rsplit('width=', 1)[0].rstrip('&?'), i2=img(i2, 10).rsplit('width=', 1)[0].rstrip('&?'),
                c=CAT_OF.get(h, ''), cn=COL[CAT_OF[h]][1] if h in CAT_OF else 'Rosier Foods', lab=LABMAP.get(h, ''),
                v=(VIDS.get(h) or [0])[0], k=' '.join([KEYWORDS.get(info_key(h), ''), INFO[info_key(h)].get('ing', '') or '', h.replace('-', ' ')]).lower())
           for h, n, sz, pr, m, r, b, i1, i2 in PRODUCTS]
    open(os.path.join(OUT, 'js', 'catalog.js'), 'w').write('window.RF=' + json.dumps({'p': cat, 'best': BEST}, ensure_ascii=False) + ';')
    if os.path.basename(SRC) != 'source':
        shutil.copy(os.path.join(SRC, 'README.md'), OUT)

    ctx = dict(SRC=SRC, pcard=pcard, carousel=carousel, car_btns=car_btns, eyebrow=eyebrow, stars=stars, inr=inr, off=off,
               PRODUCTS=PRODUCTS, BY=BY, BEST=BEST, NEW=NEW, COLLECTIONS=COLLECTIONS, COL=COL, HOME=HOME, TESTI=TESTI,
               GHEE_GALLERY=GHEE_GALLERY, img=img, purl=purl, curl=curl, CAT_OF=CAT_OF, LAB=LAB, LABCAT=LABCAT, html=html,
               SITE=SITE, page=page, LABMAP=LABMAP, NEEDS=NEEDS, PH=PH, MANUFACTURERS=MANUFACTURERS, POLICY=POLICY, INFO=INFO, info_key=info_key, VARIANTS=VARIANTS, GUIDES=GUIDES, CONTACT_EMAIL=CONTACT_EMAIL, jsonld=jsonld, VIDS=VIDS, PLANS=PLANS, JOIN_URL=JOIN_URL, ptype=ptype, srcset=srcset, STORY=STORY)
    n = 0
    for name in sorted(os.listdir(os.path.join(SRC, 'pages'))):
        mod = dict(ctx)
        exec(open(os.path.join(SRC, 'pages', name)).read(), mod)
        if 'PAGES' in mod:            # generator modules (collections, products)
            for args in mod['PAGES']:
                page(*args); n += 1
        else:
            page(mod['FILE'], mod['TITLE'], mod['DESC'], mod['ACTIVE'], mod['BODY'], mod.get('AFTER', ''), mod.get('HEAD', '')); n += 1
    urls = ''.join(f'<url><loc>{BASE}{"" if f == "index.html" else f}</loc></url>' for f in sorted(set(PAGES_BUILT)) if f not in ('cart.html', '404.html'))
    open(os.path.join(OUT, 'sitemap.xml'), 'w').write(f'<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{urls}</urlset>')
    g = 'product-a2-desi-cow-ghee-hand-churned-from-curd.html'
    open(os.path.join(OUT, 'product.html'), 'w').write(f'<!doctype html><html lang="en"><head><meta charset="utf-8"><title>Moved | Rosier Foods</title><meta name="robots" content="noindex"><link rel="canonical" href="{BASE}{g}"><meta http-equiv="refresh" content="0;url={g}"></head><body><p><a href="{g}">Go to Gir Cow A2 Ghee</a></p></body></html>')
    open(os.path.join(OUT, 'robots.txt'), 'w').write(f'User-agent: *\nAllow: /\nDisallow: /cart.html\nSitemap: {BASE}sitemap.xml\n')
    print('built', n, 'pages into', OUT)


if __name__ == '__main__':
    build()
