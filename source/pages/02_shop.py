FILE = 'shop.html'
TITLE = 'Shop All Products | Rosier Foods'
DESC = 'Shop A2 Gir Cow Ghee, stone pressed oils, atta, pickles, healthy breakfast and immunity boosters from Rosier Foods.'
ACTIVE = 'shop'

def tabs(active):
    t = f'<a href="shop.html" class="{"on" if active == "all" else ""}"><img src="assets/img/rosier-logo-green.png" alt="">All</a>'
    t += ''.join(f'<a href="{curl(k)}" class="{"on" if k == active else ""}"><img src="{img(ti, 100)}" alt="">{n}</a>' for k, n, ti, *_ in COLLECTIONS)
    return f'<nav class="col-tabs" aria-label="Categories">{t}</nav>'

def filters(prices):
    mx = int(-(-max(prices) // 100) * 100)
    return f'''<aside class="filters" aria-label="Filters">
  <h4>Price</h4><input type="range" id="f-price" min="100" max="{mx}" step="50" value="{mx}" aria-label="Maximum price"><div class="f-price-row"><span>₹100</span><span>up to <b id="f-price-v">₹{mx:,}</b></span></div>
  <h4>Customer rating</h4><label><input type="checkbox" id="f-top">4.8★ and above</label>
  <h4>Offers</h4><label><input type="checkbox" id="f-deal">20% off or more</label>
  <h4>Pack type</h4><label><input type="checkbox" class="f-pack" value="single">Single pack</label><label><input type="checkbox" class="f-pack" value="combo">Combo / Pack of 2+</label><label><input type="checkbox" class="f-pack" value="bulk">Family size (5 L / 5 kg)</label>
  <button id="f-reset" type="button">Clear all filters</button>
</aside>'''


def sortbar(n):
    return f'''<div class="toolbar"><div style="display:flex;gap:12px;align-items:center"><button class="btn btn--outline btn--sm f-toggle" type="button">Filters</button><p class="shop-count" id="shop-count" style="margin:0">{n} products</p></div>
<label class="sort">Sort by <select id="sort"><option value="featured">Featured</option><option value="rating">Top rated</option><option value="low">Price: low to high</option><option value="high">Price: high to low</option><option value="off">Biggest discount</option></select></label></div>'''

seen, order = set(), []
for k, *_r, hs in COLLECTIONS:
    for h in hs:
        if h not in seen: seen.add(h); order.append(h)
for h in [p[0] for p in PRODUCTS]:
    if h not in seen: seen.add(h); order.append(h)
cards = [pcard(h, 'reveal', (i % 4) * .05) for i, h in enumerate(order)]
cards.insert(4, f'''<div class="shop-promo reveal">{eyebrow("Rosier's Benefit Club", light=True)}<h3>Members pay 15% less. On everything.</h3><p>Plus free &amp; fast shipping and a birthday surprise box. From {inr(299)}.</p><a href="membership.html" class="btn btn--gold">See Plans <svg><use href="#i-arrow"/></svg></a></div>''')

BODY = f'''
<section class="page-hero"><div class="container">
  <nav class="crumbs reveal"><a href="index.html">Home</a><span>/</span>Shop</nav>
  <h1 class="reveal" id="shop-title" style="--d:.06s">All Products</h1>
  <p class="lead reveal" style="--d:.12s">Pure, traditional foods. Made the slow way, delivered across India.</p>
</div></section>
<section style="padding:10px 0 clamp(72px,9vw,120px)"><div class="container">
  {tabs('all')}{sortbar(len(order))}
  <div class="shop-wrap">{filters([BY[h][3] for h in order])}<div><div class="shop-grid" id="shop-grid">{''.join(cards)}</div><p class="no-res" hidden>Nothing matches these filters. <button id="f-reset2" class="link-arrow" onclick="document.getElementById('f-reset').click()" style="border:0;background:none">Clear filters</button></p></div></div>
</div></section>
'''
