# Storytelling pages required by the brief. Only verified facts from rosierfoods.com are used;
# anything Rosier still has to supply is marked with an owner note (class="owner-note").

def snav(cur):
    return '<nav class="storynav" aria-label="Our story pages">' + ''.join(
        f'<a href="{u}"{" aria-current=page" if u == cur else ""}>{n}</a>' for u, n in STORY[:6]) + '</nav>'


def hero(cur, img_url, h1, lead, crumb):
    return f'''<section class="photo-hero" style="--ph:url('{img_url}&width=2000')">
  <div class="container"><nav class="crumbs" aria-label="Breadcrumb"><a href="index.html">Home</a><span aria-hidden="true">/</span><a href="our-story.html">Our Story</a><span aria-hidden="true">/</span>{crumb}</nav>
  <h1>{h1}</h1><p>{lead}</p></div></section>
<div class="container">{snav(cur)}</div>'''


OWNER = lambda t: f'<p class="owner-note"><b>Content pending from Rosier:</b> {t}</p>'
PAGES = []

# ---------- Founder ----------
PAGES.append(('founder.html', 'Our Founder | Rosier Foods', "Meet Rosier Foods' founder Gaurav and why he started reviving the tradition of Old Bharat.", 'story', f'''
{hero('founder.html', HOME['family'], 'Our <em>Founder</em>', "Why Rosier exists, in the founder's own beliefs.", 'Our Founder')}
<section class="section"><div class="container split">
  <div class="split__media reveal"><div class="frame frame--arch"><img src="{HOME['family']}&width=1000" alt="Rosier's founder with farmers" loading="lazy"></div></div>
  <div class="reveal">
    {eyebrow('A note from our founder')}
    <h2>Gaurav</h2>
    <p>Gaurav has spent over 20 years in the health and fitness industry. Indian culture and timeless values sit at the heart of what he believes, and he's deeply drawn to the ancient Indian sciences and the Vedas.</p>
    <p>He believes milk from indigenous Gir desi cows, described in our ancient texts, is better for us than A1 milk from HF and Jersey cows. He wants to restore India's traditions in modern life, and Rosier is how he's doing it.</p>
    {OWNER('a founder portrait approved for the website, and a short quote in his own words.')}
  </div>
</div></section>
<section class="section bg-cream2"><div class="container"><p class="pull">Restoring India's traditions in modern society.<cite>Gaurav's mission, as stated on rosierfoods.com</cite></p></div></section>'''))

# ---------- Farmers ----------
PAGES.append(('farmers.html', 'Our Farmers | Rosier Foods', 'How Rosier works with heritage grain farmers and rural farming families.', 'story', f'''
{hero('farmers.html', PH['cows'], 'Our <em>Farmers</em>', 'The people and places our food comes from.', 'Our Farmers')}
<section class="section"><div class="container">
  <header class="section-head">{eyebrow('How we work', True)}<h2>Source to table</h2><p class="section-sub">What we can say today, based on what Rosier has published.</p></header>
  <div class="trio">
    <div><h3>Direct relationships</h3><p>We work directly with heritage grain farmers, for sustainable sourcing.</p></div>
    <div><h3>Fair trade</h3><p>Fair trade practices and direct support to rural farming families.</p></div>
    <div><h3>Gir desi cows</h3><p>Our ghee starts with milk from free-grazing indigenous Gir cows.</p></div>
  </div>
  <div class="center">{OWNER('names, villages, photos and consent of the farmers and suppliers to feature. We will not publish farmer profiles until these are verified.')}</div>
</div></section>'''))

# ---------- Process ----------
steps = [('cows', 'Free-grazing Gir cows', 'Our A2 ghee starts with milk from indigenous Gir desi cows.'),
         ('bilona_pot', 'Boil, cool, set curd', 'The milk is boiled, cools naturally, and a natural starter sets it into curd overnight.'),
         ('churning', 'Hand-churned bilona', 'The curd is churned using the traditional Bilona method.'),
         ('oil_process', 'Stone pressed oils', 'Our oils are cold pressed on stone, without chemicals or solvents.'),
         ('tested', 'Lab tested', 'We publish lab test reports for 32 products.')]
tl = ''.join(f'<div class="tl reveal"><h3>{t}</h3><p>{d}</p></div>' for _, t, d in steps)
cards = ''.join(f'<div class="jcard reveal"><div class="jcard__img"><img src="{PH[k]}&width=600" alt="{t}" loading="lazy"><span aria-hidden="true">{i+1}</span></div><h3>{t}</h3><p>{d}</p></div>' for i, (k, t, d) in enumerate(steps))
PAGES.append(('process.html', 'Our Process – Bilona, Stone Pressing & Chakki | Rosier Foods', 'How Rosier makes A2 bilona ghee, stone pressed oils and stone-ground atta, step by step.', 'story', f'''
{hero('process.html', PH['churning'], 'Our <em>Process</em>', 'Slow methods, written down step by step.', 'Our Process')}
<section class="section"><div class="container"><h2 class="sr-only">How we make it</h2><div class="journey">{cards}</div></div></section>
<section class="section bg-cream2"><div class="container">
  <header class="section-head">{eyebrow('Watch', True)}<h2>See it for yourself</h2></header>
  <div class="exp__video"><video src="{HOME['video']}" controls muted playsinline preload="none" poster="{PH['churning']}&width=1200" aria-label="Video: how Rosier makes its food"></video></div>
</div></section>
<section class="section"><div class="container"><header class="section-head">{eyebrow('The steps', True)}<h2>From farm to your table</h2></header><div class="timeline">{tl}<div class="tl"><h3>Stone-ground atta</h3><p>Khapli, multigrain, ragi, jowar and sattu are stone-ground in the traditional chakki method.</p></div></div></div></section>'''))

# ---------- Philosophy ----------
PAGES.append(('philosophy.html', 'Our Philosophy – परंपरा • शुद्धता • ईमानदारी | Rosier Foods', "Rosier's philosophy: tradition, purity and honesty.", 'story', f'''
{hero('philosophy.html', PH['ghee_spread'], 'Our <em>Philosophy</em>', 'Three words we hold ourselves to.', 'Our Philosophy')}
<section class="section"><div class="container">
  <h2 class="sr-only">परंपरा, शुद्धता, ईमानदारी: tradition, purity, honesty</h2>
  <div class="trio">
    <div><p class="dev" lang="hi">परंपरा</p><h3>Tradition</h3><p>Bilona churning, stone pressing and chakki milling. The old ways, kept alive.</p></div>
    <div><p class="dev" lang="hi">शुद्धता</p><h3>Purity</h3><p>No refined oils. No additives. Just pure, wholesome ingredients.</p></div>
    <div><p class="dev" lang="hi">ईमानदारी</p><h3>Honesty</h3><p>Lab reports and manufacturer details published, so you never have to take our word for it.</p></div>
  </div>
</div></section>
<section class="section bg-cream2"><div class="container"><p class="pull">Foods that heal, not hype.<cite>Rosier Foods</cite></p></div></section>'''))

# ---------- Commitment ----------
PAGES.append(('commitment.html', 'Our Commitment – Sustainability & Community | Rosier Foods', "Rosier's commitment to sustainability, rural farming families and transparency.", 'story', f'''
{hero('commitment.html', PH['cow_sun'], 'Our <em>Commitment</em>', 'To the land, to farming families, and to you.', 'Our Commitment')}
<section class="section"><div class="container">
  <h2 class="sr-only">What we commit to</h2>
  <div class="std-claims">
    <div class="claim"><img src="{PH['cows']}&width=300" alt="" loading="lazy"><div><h3>Sustainability</h3><p>Minimally processed products from sustainably sourced, consciously grown ingredients.</p></div></div>
    <div class="claim"><img src="{HOME['family']}&width=300" alt="" loading="lazy"><div><h3>Community</h3><p>Fair trade practices and direct support to rural farming families.</p></div></div>
    <div class="claim"><img src="{PH['tested']}&width=300" alt="" loading="lazy"><div><h3>Transparency</h3><p>Lab reports for 32 products and our 6 FSSAI-licensed units, published openly.</p><a class="ev" href="standards.html">Know Your Food →</a></div></div>
    <div class="claim"><img src="{PH['family_table']}&width=300" alt="" loading="lazy"><div><h3>Fair terms</h3><p>Clear delivery, return and cancellation terms, shown before you pay.</p><a class="ev" href="standards.html#returns">Read the terms →</a></div></div>
  </div>
</div></section>'''))

# ---------- FAQ ----------
FAQ = [('offers', 'Offers', [('What is the current offer?', 'Our Diwali Sale is live with up to 30% off. You also get a free bottle on orders of ₹2,499, a free tumbler on ₹4,999, and both on ₹7,999.'),
                              ('Can I return sale items?', POLICY['sale'])]),
       ('orders', 'Orders & delivery', [('How long does delivery take?', POLICY['delivery']), ('Can I cancel my order?', POLICY['cancel']),
                                        ('How much is shipping?', 'Any shipping charge is shown at checkout, before you pay.')]),
       ('returns', 'Returns', [('Can I return or exchange a product?', POLICY['returns']), ('What should I do when my parcel arrives?', POLICY['unboxing'])]),
       ('quality', 'Quality', [('Are your products lab tested?', 'We publish lab reports for 32 products. <a href="lab-reports.html">See them all</a>.'),
                               ('Where are your products made?', 'In six FSSAI-licensed units. <a href="standards.html#units">See units and licence numbers</a>.'),
                               ('How is your ghee made?', 'From the curd of free-grazing Gir cows\' milk, churned the Bilona way. <a href="process.html">See our process</a>.')]),
       ('membership', 'Membership', [('What is Rosier Parivaar?', 'Our membership from ₹299: 15% off all orders, free &amp; fast shipping, a birthday surprise box and more. <a href="membership.html#terms">See terms</a>.')])]
faq_html = ''
for k, t, qs in FAQ:
    items = ''.join(f'<div class="acc-item"><button class="acc-q" aria-expanded="false">{q}<svg aria-hidden="true"><use href="#i-plus"/></svg></button><div class="acc-a"><div><p>{a}</p></div></div></div>' for q, a in qs)
    faq_html += f'<section class="section" id="{k}" style="padding:28px 0"><h2 style="font-size:28px;margin-bottom:10px">{t}</h2><div class="accordion" data-closed>{items}</div></section>'
PAGES.append(('faq.html', 'FAQs – Orders, Delivery, Returns & Quality | Rosier Foods', 'Answers about Rosier Foods offers, delivery times, returns, cancellations, lab reports and membership.', 'faq', f'''
<section class="page-hero"><div class="container"><nav class="crumbs" aria-label="Breadcrumb"><a href="index.html">Home</a><span aria-hidden="true">/</span>FAQs</nav><h1>Frequently asked questions</h1><p class="lead">Can't find your answer? Email <a href="mailto:{CONTACT_EMAIL}" style="color:var(--brown);text-decoration:underline">{CONTACT_EMAIL}</a> or WhatsApp us.</p></div></section>
<div class="container" style="max-width:900px;padding-bottom:80px">{faq_html}</div>'''))

# ---------- 404 ----------
PAGES.append(('404.html', 'Page not found | Rosier Foods', 'This page could not be found.', '404', f'''
<section class="page-hero" style="padding:100px 0"><div class="container"><h1>We couldn't find that page</h1><p class="lead">Try searching, or start from one of these.</p>
<form class="search" role="search" action="shop.html" style="max-width:420px;margin:24px auto 0"><svg aria-hidden="true"><use href="#i-search"/></svg><label class="sr-only" for="q-404">Search products</label><input id="q-404" name="q" type="search" placeholder="Search ghee, atta, honey…"></form>
<div class="storynav" style="margin-top:22px"><a href="index.html">Home</a><a href="shop.html">Shop all</a><a href="faq.html">FAQs</a><a href="contact.html">Contact us</a></div></div></section>'''))
