ABOUT = {
    'amlaprash': 'Made using hand-picked amla fruit and A2 Gir cow ghee. Naturally sweetened with desi khand.',
    'wild-flower-honey': 'Multi-floral honey, responsibly gathered from bees that forage on wild flowers in Himalayan forests. Ingredient: raw honey. Keep it in a cool, dry place with the lid tightly shut, and don\'t refrigerate.',
    'wood-pressed-black-mustard-oil': 'Made from high-quality mustard seeds, stone pressed without chemicals or solvents. A healthy, flavourful traditional cooking oil.',
    'wood-pressed-coconut-oil': 'Unrefined, chemical-free coconut oil, stone pressed from fresh natural coconuts. Great for cooking, baking and daily use.',
    'khapli-emmer-wheat-atta-stoneground-high-fiber-for-gut-health': 'Stone ground Khapli (emmer) wheat flour. A non-GMO heritage grain that\'s high in fibre and low GI.',
}
POLICY = f'''<div class="acc-item"><button class="acc-q" aria-expanded="false">Delivery &amp; returns<svg><use href="#i-plus"/></svg></button><div class="acc-a"><div><p>We deliver across India. For timelines and charges, see our <a href="{SITE}/policies/shipping-policy">Shipping Policy</a>. Something not right? Our <a href="{SITE}/policies/refund-policy">Refund Policy</a> has you covered.</p></div></div></div>'''


def gallery(imgs, alt):
    th = ''.join(f'<button class="{"on" if i == 0 else ""}" aria-label="Image {i+1}"><img src="{img(g, 200)}" data-full="{img(g, 1100)}" alt=""></button>' for i, g in enumerate(imgs))
    return f'''<div class="gallery reveal"><div class="gallery__thumbs">{th}</div>
    <div class="gallery__main"><img src="{img(imgs[0], 1100)}" alt="{html.escape(alt)}"></div></div>'''


def related(h):
    k = CAT_OF.get(h)
    pool = [x for x in (COL[k][5] if k else []) if x != h]
    pool += [x for x in BEST if x != h and x not in pool]
    return pool[:8]


def buybox(h, name, price, mrp, r, variants, reviews=None):
    crumbs = f'<a href="{curl(CAT_OF[h])}">{COL[CAT_OF[h]][1]}</a>' if h in CAT_OF else '<a href="shop.html">Shop</a>'
    o = off(price, mrp)
    return f'''<nav class="crumbs"><a href="index.html">Home</a><span>/</span>{crumbs}</nav>
    <h1 class="pdp__title">{html.escape(name)}</h1>
    <div class="pdp__meta">{stars(r, reviews)}{'<a href="#reviews">Read reviews</a>' if reviews else ''}<a href="lab-reports.html">View lab report</a></div>
    <div class="pdp__price"><b id="pdp-price">{inr(price)}</b>{f'<s id="pdp-mrp">{inr(mrp)}</s><span class="off" id="pdp-off">{o}% OFF</span>' if o > 0 else ''}</div>
    <p class="tax">Tax included.</p>
    <p class="opt-label">Size</p><div class="variants">{variants}</div>
    <div class="buy-row">
      <div class="qty"><button data-d="-" aria-label="Decrease">−</button><input id="pdp-qty" value="1" aria-label="Quantity"><button data-d="+" aria-label="Increase">+</button></div>
      <button class="btn btn--primary" id="pdp-add" data-h="{h}">Add to Cart</button>
    </div>
    <a href="cart.html" class="btn btn--outline btn--block" style="margin-top:10px">Buy Now</a>
    <div class="member-note"><span class="earnback__coin" aria-hidden="true">₹</span><span>Benefit Club members get <b>15% off</b> on every order. <a href="membership.html">Join from ₹299</a></span></div>
    {labblock(h)}'''


def labblock(h):
    if h not in LABMAP: return ''
    return f'''<div class="pdp-lab"><span class="ico"><svg><use href="#i-flask"/></svg></span><span>This product is lab tested. <a href="{LABMAP[h]}" target="_blank" rel="noopener">Open the lab report</a></span></div>'''


def fbt(h):
    k = CAT_OF.get(h)
    pals = [x for x in BEST if x != h and CAT_OF.get(x) != k]
    pals = [x for x in pals if x != 'wood-pressed-coconut-oil'][:2]
    items = [h] + pals
    cells = '<span class="fbt__plus">+</span>'.join(f'''<div class="fbt__i"><img src="{img(BY[x][7], 300)}" alt=""><label><input type="checkbox" value="{x}" checked><span>{"This item: " if x == h else ""}{html.escape(BY[x][1])}<br><b>{inr(BY[x][3])}</b></span></label></div>''' for x in items)
    return f'''<section class="section" style="padding-bottom:0"><div class="container"><div class="fbt reveal">
  {eyebrow('Frequently bought together')}<h2 style="font-size:clamp(26px,3vw,36px);margin:8px 0 22px">Complete your Rosier rasoi</h2>
  <div class="fbt__row">{cells}<div class="fbt__sum"><p>Total for <span class="fbt__n">3</span> items</p><b class="fbt__total"></b><button class="btn btn--primary fbt__add">Add selected to cart</button></div></div>
</div></div></section>'''


RECENT = '''<section class="section" id="recent" hidden style="padding-top:0"><div class="container"><div class="head-row"><div><p class="eyebrow">Picked up where you left off</p><h2>Recently viewed</h2></div></div><div class="recent__row"></div></div></section>'''


def related_section(h):
    return f'''<section class="section bg-cream2"><div class="container">
  <div class="head-row reveal"><div>{eyebrow('Pairs well with')}<h2>You may also like</h2></div>{car_btns('rel')}</div>
  {carousel('rel', related(h))}</div></section>'''


PAGES = []
for p in PRODUCTS:
    h, name, size, price, mrp, r, badge, i1, i2 = p
    if h == 'a2-desi-cow-ghee-hand-churned-from-curd':
        V = [('250 ml', 594.15, 699), ('500 ml', 999.00, 1350), ('1 L', 1808.80, 2380), ('2 L · 2 Glass Jars', 3570.00, 4760),
             ('2 L · Steel Dolchi', 3585.00, 4780), ('5 L · 5 Glass Jars', 8925.00, 11900), ('5 L · Steel Dolchi', 8925.00, 11900)]
        variants = ''.join(f'<button class="variant{" on" if i == 0 else ""}" data-price="{vp}" data-mrp="{vm}">{vn}</button>' for i, (vn, vp, vm) in enumerate(V))
        bars = ''.join(f'<div class="bar"><span>{s} ★</span><i style="--w:{w}%"></i><span>{c}</span></div>' for s, w, c in [(5, 91, '1,720'), (4, 9, '165'), (3, .5, '8'), (2, .2, '1'), (1, 0, '0')])
        rv = ''.join(f'''<article class="review reveal"><svg class="q"><use href="#i-quote"/></svg><h3 style="font-size:20px">{t}</h3><p style="color:var(--text);font-size:15px">{q}</p><footer><span class="avatar">{n[0]}</span><div>{n}<small>{pp}</small></div></footer></article>'''
                     for t, q, n, pp, _ in TESTI if 'Ghee' in pp)
        body = f'''
<section class="container pdp">
  {gallery(GHEE_GALLERY, name)}
  <div class="pdp__info reveal" style="--d:.1s">
    {buybox(h, name, price, mrp, r, variants, '1,894 reviews')}
    <ul class="pdp-perks"><li><svg><use href="#i-cow"/></svg>Free-grazing Gir cows</li><li><svg><use href="#i-mill"/></svg>Bilona, made from curd</li><li><svg><use href="#i-flask"/></svg>Lab report published</li></ul>
    <div class="accordion">
      <div class="acc-item"><button class="acc-q" aria-expanded="false">Why you'll love it<svg><use href="#i-plus"/></svg></button><div class="acc-a"><div>
        <p style="padding-bottom:8px">We make this ghee from fresh milk of free-grazing Gir cows. Here's what it brings to your kitchen:</p>
        <ul class="benefit-list" style="padding-bottom:24px">
          <li><svg><use href="#i-check"/></svg>Aids digestion and supports gut health</li><li><svg><use href="#i-check"/></svg>Acts as a natural lubricant for joints</li>
          <li><svg><use href="#i-check"/></svg>High smoke point, great for Indian cooking</li><li><svg><use href="#i-check"/></svg>Contains vitamins A, E and K</li>
          <li><svg><use href="#i-check"/></svg>Anti-bacterial, anti-fungal and antioxidant properties</li><li><svg><use href="#i-check"/></svg>Good for skin, hair and eyes</li>
        </ul></div></div></div>
      <div class="acc-item"><button class="acc-q" aria-expanded="false">Ingredients<svg><use href="#i-plus"/></svg></button><div class="acc-a"><div><p>A2 milk fat, natural yoghurt. That's it.</p></div></div></div>
      {POLICY}
    </div>
  </div>
</section>
<section class="section bg-cream2"><div class="container">
  <header class="section-head reveal">{eyebrow('How we make it', True)}<h2>From Gir cow to your kitchen</h2><p class="section-sub">No shortcuts. The bilona way, step by step.</p></header>
  <ol class="made">
    <li class="reveal"><span class="step__num">01</span><h3>Boil the milk</h3><p>Fresh milk from our free-grazing Gir cows is brought to a boil.</p></li>
    <li class="reveal" style="--d:.06s"><span class="step__num">02</span><h3>Let it cool</h3><p>We let it cool down naturally to room temperature. No rushing.</p></li>
    <li class="reveal" style="--d:.12s"><span class="step__num">03</span><h3>Set the curd</h3><p>A natural starter culture goes in, and it sets into curd overnight.</p></li>
    <li class="reveal" style="--d:.18s"><span class="step__num">04</span><h3>Churn by hand</h3><p>The curd is churned using the traditional Bilona method to get the ghee.</p></li>
  </ol></div></section>
<section class="section" id="reviews"><div class="container">
  <header class="section-head reveal">{eyebrow('Customer reviews', True)}<h2>What families are saying</h2></header>
  <div class="rv-summary"><div class="rv-score reveal"><b>4.9</b>{stars(4.9)}<p>Based on 1,894 reviews</p><div class="bars">{bars}</div></div>
  <div class="rv-list">{rv}</div></div></div></section>
{fbt(h)}
{related_section(h)}
{RECENT}'''
        PAGES.append(('product.html', 'Gir Cow A2 Ghee – Hand Churned Bilona | Rosier Foods', 'Rosier Gir Cow A2 Ghee, made from curd and hand-churned the Bilona way. Rated 4.9 from 1,894 reviews.', 'shop', body))
        PAGES.append((purl(h), 'Gir Cow A2 Ghee – Hand Churned Bilona | Rosier Foods', 'Rosier Gir Cow A2 Ghee, hand-churned the Bilona way.', 'shop', body))
        continue

    about = ABOUT.get(h, f'Part of Rosier Foods\' range of pure, traditional foods. Tap below for the full ingredient list, nutrition and usage details.')
    variants = f'<button class="variant on" data-price="{price}" data-mrp="{mrp}">{size}</button>'
    body = f'''
<section class="container pdp">
  {gallery([i1, i2], name)}
  <div class="pdp__info reveal" style="--d:.1s">
    {buybox(h, name, price, mrp, r, variants)}
    <ul class="pdp-perks"><li><svg><use href="#i-leaf"/></svg>No refined oils, no additives</li><li><svg><use href="#i-truck"/></svg>Delivered across India</li><li><svg><use href="#i-flask"/></svg>Lab reports published</li></ul>
    <div class="accordion">
      <div class="acc-item"><button class="acc-q" aria-expanded="false">About this product<svg><use href="#i-plus"/></svg></button><div class="acc-a"><div><p>{about}</p></div></div></div>
      {POLICY}
    </div>
    <a href="{SITE}/products/{h}" class="link-arrow" style="margin-top:22px">See full details on rosierfoods.com <svg><use href="#i-arrow"/></svg></a>
  </div>
</section>
{fbt(h)}
{related_section(h)}
{RECENT}'''
    PAGES.append((purl(h), f'{name} | Rosier Foods', f'Buy Rosier {name} online. {about}', 'shop', body))
