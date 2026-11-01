GHEE = 'a2-desi-cow-ghee-hand-churned-from-curd'


def gallery(imgs, alt):
    th = ''.join(f'<button class="{"on" if i == 0 else ""}" aria-label="Show image {i+1}"><img src="{img(g, 200)}" data-full="{img(g, 1100)}" alt=""></button>' for i, g in enumerate(imgs))
    return f'''<div class="gallery reveal"><div class="gallery__thumbs">{th}</div>
    <div class="gallery__main"><img src="{img(imgs[0], 1100)}" alt="{html.escape(alt)}" width="1100" height="1100" fetchpriority="high"></div></div>'''


def related(h):
    k = CAT_OF.get(h)
    pool = [x for x in (COL[k][5] if k else []) if x != h]
    pool += [x for x in BEST if x != h and x not in pool]
    return pool[:8]


def variants_html(h, size, price, mrp):
    vs = VARIANTS.get(h) or ([('250 ml', 594.15, 699, 1), ('500 ml', 999.00, 1350, 1), ('1 L', 1808.80, 2380, 1), ('2 L · 2 Glass Jars', 3570.00, 4760, 1),
                               ('2 L · Steel Dolchi', 3585.00, 4780, 1), ('5 L · 5 Glass Jars', 8925.00, 11900, 1), ('5 L · Steel Dolchi', 8925.00, 11900, 1)] if h == GHEE else [(size, price, mrp, 1)])
    return ''.join(f'<button class="variant{" on" if i == 0 else ""}" data-price="{p}" data-mrp="{m}"{"" if a else " disabled aria-disabled=true"}>{n}{"" if a else " · sold out"}</button>' for i, (n, p, m, a) in enumerate(vs))


def buybox(h, name, size, price, mrp, r, reviews=None):
    k = CAT_OF.get(h)
    crumbs = f'<a href="{curl(k)}">{COL[k][1]}</a>' if k else '<a href="shop.html">Shop</a>'
    o = off(price, mrp); I = INFO[info_key(h)]
    lab = f'<a href="{LABMAP[h]}" target="_blank" rel="noopener">View lab report</a>' if h in LABMAP else ''
    why = ''.join(f'<li><svg aria-hidden="true"><use href="#i-check"/></svg>{w}</li>' for w in I['why'])
    return f'''<nav class="crumbs" aria-label="Breadcrumb"><a href="index.html">Home</a><span>/</span>{crumbs}</nav>
    <h1 class="pdp__title">{html.escape(name)}</h1>
    <div class="pdp__meta">{stars(r, reviews)}{'<a href="#reviews">Read reviews</a>' if reviews else ''}{lab}</div>
    <ul class="why" aria-label="Why this product">{why}</ul>
    <div class="pdp__price"><b id="pdp-price">{inr(price)}</b>{f'<s id="pdp-mrp">{inr(mrp)}</s><span class="off" id="pdp-off">{o}% OFF</span>' if o > 0 else ''}</div>
    <p class="tax">MRP inclusive of all taxes. Shipping, if any, shown at checkout.</p>
    <span class="stock">In stock</span>
    <p class="opt-label">Size</p><div class="variants">{variants_html(h, size, price, mrp)}</div>
    <div class="buy-row">
      <div class="qty"><button data-d="-" aria-label="Decrease quantity">−</button><input id="pdp-qty" value="1" inputmode="numeric" aria-label="Quantity"><button data-d="+" aria-label="Increase quantity">+</button></div>
      <button class="btn btn--primary" id="pdp-add" data-h="{h}">Add to Cart</button>
    </div>
    <button class="btn btn--outline btn--block" data-h="{h}" data-buy style="margin-top:10px">Buy Now</button>
    <div class="deliv">
      <span><svg aria-hidden="true"><use href="#i-truck"/></svg>Usually delivered in 3–5 days across India</span>
      <span><svg aria-hidden="true"><use href="#i-check"/></svg>Return or exchange within 2 days if damaged, wrong or seal broken</span>
      <span><svg aria-hidden="true"><use href="#i-shield"/></svg>Made in an <a href="standards.html#units" style="text-decoration:underline">FSSAI-licensed unit</a></span>
    </div>
    <div class="member-note"><span class="earnback__coin" aria-hidden="true">₹</span><span>Benefit Club members get <b>15% off</b> on every order. <a href="membership.html">Join from ₹299</a></span></div>'''


def details(h, size, extra=''):
    I = INFO[info_key(h)]
    rows = [('Net quantity', size)]
    if I.get('ing'): rows.append(('Ingredients', I['ing']))
    if I.get('store'): rows.append(('Storage', I['store']))
    rows.append(('Made by', 'Rosier Foods Pvt. Ltd. or a licensed partner unit. <a href="standards.html#units" style="text-decoration:underline">Find yours from the batch code</a>'))
    if h in LABMAP: rows.append(('Lab report', f'<a href="{LABMAP[h]}" target="_blank" rel="noopener" style="text-decoration:underline">Open the report</a>'))
    dl = ''.join(f'<dt>{a}</dt><dd>{b}</dd>' for a, b in rows)
    use = f'<div class="acc-item"><button class="acc-q" aria-expanded="false">How to use<svg aria-hidden="true"><use href="#i-plus"/></svg></button><div class="acc-a"><div><p>{I["use"]}</p></div></div></div>' if I.get('use') else ''
    return f'''<div class="accordion">
      <div class="acc-item"><button class="acc-q" aria-expanded="false">About this product<svg aria-hidden="true"><use href="#i-plus"/></svg></button><div class="acc-a"><div><p>{I['about']} <a href="{SITE}/products/{h}" style="text-decoration:underline">Full description on rosierfoods.com</a></p>{extra}</div></div></div>
      <div class="acc-item"><button class="acc-q" aria-expanded="false">Product details<svg aria-hidden="true"><use href="#i-plus"/></svg></button><div class="acc-a"><div><dl class="facts">{dl}</dl></div></div></div>
      {use}
      <div class="acc-item"><button class="acc-q" aria-expanded="false">Delivery, returns &amp; cancellation<svg aria-hidden="true"><use href="#i-plus"/></svg></button><div class="acc-a"><div><p>{POLICY['delivery']} {POLICY['returns']} {POLICY['unboxing']} {POLICY['cancel']} <a href="standards.html#returns" style="text-decoration:underline">Read our terms</a></p></div></div></div>
    </div>'''


def fbt(h):
    k = CAT_OF.get(h)
    pals = [x for x in BEST if x != h and CAT_OF.get(x) != k][:2]
    items = [h] + pals
    cells = '<span class="fbt__plus" aria-hidden="true">+</span>'.join(f'''<div class="fbt__i"><img src="{img(BY[x][7], 300)}" alt="" loading="lazy"><label><input type="checkbox" value="{x}" checked><span>{"This item: " if x == h else ""}{html.escape(BY[x][1])}<br><b>{inr(BY[x][3])}</b></span></label></div>''' for x in items)
    return f'''<section class="section" style="padding-bottom:0"><div class="container"><div class="fbt reveal">
  {eyebrow('Frequently bought together')}<h2 style="font-size:clamp(26px,3vw,36px);margin:8px 0 22px">Complete your Rosier rasoi</h2>
  <div class="fbt__row">{cells}<div class="fbt__sum"><p>Total for <span class="fbt__n">3</span> items</p><b class="fbt__total"></b><button class="btn btn--primary fbt__add">Add selected to cart</button></div></div>
</div></div></section>'''


RECENT = '''<section class="section" id="recent" hidden style="padding-top:0"><div class="container"><div class="head-row"><div><p class="eyebrow">Pick up where you left off</p><h2>Recently viewed</h2></div></div><div class="recent__row"></div></div></section>'''


def related_section(h):
    return f'''<section class="section bg-cream2"><div class="container">
  <div class="head-row reveal"><div>{eyebrow('Pairs well with')}<h2>You may also like</h2></div>{car_btns('rel')}</div>
  {carousel('rel', related(h))}</div></section>'''


def ld(h, name, price, r, imgs, rating=None):
    k = CAT_OF.get(h)
    prod = {"@context": "https://schema.org", "@type": "Product", "name": name, "sku": h, "brand": {"@type": "Brand", "name": "Rosier Foods"},
            "image": [img(x, 1000) for x in imgs[:3]], "description": INFO[info_key(h)]['about'],
            "offers": {"@type": "Offer", "priceCurrency": "INR", "price": f"{price:.2f}", "availability": "https://schema.org/InStock", "url": f"{SITE}/products/{h}"}}
    if rating: prod["aggregateRating"] = {"@type": "AggregateRating", "ratingValue": rating[0], "reviewCount": rating[1]}
    crumbs = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": SITE}] + ([{"@type": "ListItem", "position": 2, "name": COL[k][1], "item": f"{SITE}/collections/{k}"}] if k else [])}
    return jsonld(prod) + jsonld(crumbs)


PAGES = []
for p in PRODUCTS:
    h, name, size, price, mrp, r, badge, i1, i2 = p
    if h == GHEE:
        bars = ''.join(f'<div class="bar"><span>{s} ★</span><i style="--w:{w}%"></i><span>{c}</span></div>' for s, w, c in [(5, 91, '1,720'), (4, 9, '165'), (3, .5, '8'), (2, .2, '1'), (1, 0, '0')])
        rv = ''.join(f'''<article class="review reveal"><svg class="q" aria-hidden="true"><use href="#i-quote"/></svg><h3 style="font-size:20px">{t}</h3><p style="color:var(--text);font-size:15px">{q}</p><footer><span class="avatar" aria-hidden="true">{n[0]}</span><div>{n}<small>{pp}</small></div></footer></article>'''
                     for t, q, n, pp, _ in TESTI if 'Ghee' in pp)
        extra = '<ul class="benefit-list" style="padding-bottom:20px"><li><svg aria-hidden="true"><use href="#i-check"/></svg>From free-grazing Gir cows</li><li><svg aria-hidden="true"><use href="#i-check"/></svg>Contains vitamins A, E and K</li><li><svg aria-hidden="true"><use href="#i-check"/></svg>High smoke point for Indian cooking</li><li><svg aria-hidden="true"><use href="#i-check"/></svg>Made from curd, not milk or malai</li></ul>'
        body = f'''
<section class="container pdp">
  {gallery(GHEE_GALLERY, name)}
  <div class="pdp__info reveal" style="--d:.1s">
    {buybox(h, name, size, price, mrp, r, '1,894 reviews')}
    {details(h, '250 ml, 500 ml, 1 L, 2 L or 5 L (glass jars or steel dolchi)', extra)}
  </div>
</section>
<section class="section bg-cream2"><div class="container">
  <header class="section-head reveal">{eyebrow('How we make it', True)}<h2>From Gir cow to your kitchen</h2><p class="section-sub">No shortcuts. The bilona way, step by step.</p></header>
  <div class="journey" style="margin-top:20px">{''.join(f'<div class="jcard reveal" style="--d:{i*.08}s"><div class="jcard__img"><img src="{PH[kk]}&width=600" alt="{t}" loading="lazy"><span>{i+1}</span></div><h3>{t}</h3><p>{d}</p></div>' for i, (kk, t, d) in enumerate([('cows', 'Boil the milk', 'Fresh milk from free-grazing Gir cows is brought to a boil.'), ('bilona_pot', 'Cool & set curd', 'It cools naturally, then a natural starter sets it into curd overnight.'), ('churning', 'Churn by hand', 'The curd is churned using the traditional Bilona method.'), ('tested', 'Lab tested', 'The lab report is published for you to read.')]))}</div>
</div></section>
<section class="section" id="reviews"><div class="container">
  <header class="section-head reveal">{eyebrow('Customer reviews', True)}<h2>What families are saying</h2><p class="section-sub">4.9 out of 5 from 1,894 reviews on rosierfoods.com.</p></header>
  <div class="rv-summary"><div class="rv-score reveal"><b>4.9</b>{stars(4.9)}<p>Based on 1,894 reviews</p><div class="bars">{bars}</div></div>
  <div class="rv-list">{rv}</div></div></div></section>
{fbt(h)}
{related_section(h)}
{RECENT}
{ld(h, name, price, r, GHEE_GALLERY, ('4.9', '1894'))}'''
        for f in ('product.html', purl(h)):
            PAGES.append((f, 'Gir Cow A2 Ghee – Hand Churned Bilona | Rosier Foods', 'Rosier Gir Cow A2 Ghee, made from curd and hand-churned the Bilona way. Lab tested. Rated 4.9 from 1,894 reviews.', 'shop', body))
        continue

    body = f'''
<section class="container pdp">
  {gallery([i1, i2], name)}
  <div class="pdp__info reveal" style="--d:.1s">
    {buybox(h, name, size, price, mrp, r)}
    {details(h, size)}
  </div>
</section>
{fbt(h)}
{related_section(h)}
{RECENT}
{ld(h, name, price, r, [i1, i2])}'''
    PAGES.append((purl(h), f'{name} | Rosier Foods', f'Buy Rosier {name} ({size}) online. {INFO[info_key(h)]["about"]}', 'shop', body))
