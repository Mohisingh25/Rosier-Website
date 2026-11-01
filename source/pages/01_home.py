FILE = 'index.html'
TITLE = 'Rosier Foods | A2 Bilona Ghee, Stone Pressed Oils & Khapli Atta'
DESC = 'Reviving the Tradition of Old Bharat. A2 Gir cow bilona ghee, stone pressed oils, stone-ground atta, raw honey and sun-dried pickles. Made in FSSAI-licensed units, lab reports published.'
ACTIVE = 'home'
H = HOME
HEAD = ''
BCFG = load_config('banners.js'); SCFG = load_config('homepage.js')
_b = sorted([b for b in BCFG['banners'] if cfg_live(b)], key=lambda b: b.get('order', 99))
NOSCRIPT_HERO = (f'<noscript><a class="hb__noscript" href="{_b[0]["href"]}"><img src="{_b[0]["desktop"]["src"]}" alt="{html.escape(_b[0].get("alt", ""))}" width="{_b[0]["desktop"].get("width", 3000)}" height="{_b[0]["desktop"].get("height", 1000)}" fetchpriority="high"></a></noscript>' if _b else '')
NOSCRIPT_PROMOS = '<noscript>' + ''.join(f'<a class="ptile" href="{t["href"]}"><img src="{t["image"]}" alt="{html.escape(t.get("alt", t["title"]))}" width="{t.get("width", 800)}" height="{t.get("height", 436)}"><span class="ptile__t">{html.escape(t["title"])}</span></a>' for t in SCFG['promoTiles'] if cfg_live(t)) + '</noscript>'
NOSCRIPT_CATS = '<noscript>' + ''.join(f'<a class="rcat" href="{c["href"]}"><span class="rcat__n">{html.escape(c["name"])}</span></a>' for c in SCFG['categories'] if cfg_live(c)) + '</noscript>'

BEST5 = BEST[:5]
def need_items(hs):
    rest = [h for h in hs if h not in BEST5]
    return rest if len(rest) >= 3 else hs

# 4 · Shop by need
NPH = {'cooking': PH['oil_range'], 'breakfast': img(BY['high-protein-oats-assorted-pack'][8], 9).split('&width')[0],
       'grains': img(BY['khapli-emmer-wheat-atta-stoneground-high-fiber-for-gut-health'][8], 9).split('&width')[0], 'family': PH['ghee_spread'],
       'winter': img(BY['amlaprash'][8], 9).split('&width')[0], 'taste': PH['oil_food']}
ntabs = ''.join(f'<button class="{"on" if i == 0 else ""}" data-tab="{k}" role="tab" id="tab-{k}" aria-selected="{"true" if i == 0 else "false"}" aria-controls="need-{k}">{n}</button>' for i, (k, n, *_r) in enumerate(NEEDS))
npanes = ''.join(f'''<div class="need-pane" id="need-{k}" data-pane="{k}" role="tabpanel" aria-labelledby="tab-{k}"{"" if i == 0 else " hidden"}>
  <div class="need-intro" style="--nbg:url('{NPH[k]}&width=900')"><p class="eyebrow eyebrow--light">Shop by need</p><h3>{n}</h3><p>{line}</p></div>
  <div class="need-grid">{''.join(pcard(h, '') for h in need_items(hs))}</div></div>''' for i, (k, n, line, hs) in enumerate(NEEDS))

# 5 · Bestsellers (one tabbed row)
COMBOS = ['pickle-tasting-set', 'wild-forest-honey-pack-of-2', 'mango-pickle-natural-sun-dried-pack-of-2', 'stone-pressed-black-mustard-oil-oil-kit-5-ltr',
          'stone-pressed-groundnut-oil-oil-kit-5-ltr', 'khapli-emmer-wheat-atta-5kg', 'green-chilly-pickle-natural-sun-dried-pack-of-2', 'stone-pressed-yellow-mustard-oil-kit-5-ltr']
ROWS = [('best', 'Bestsellers', BEST), ('new', 'New arrivals', NEW), ('value', 'Value packs', COMBOS)]
rtabs = ''.join(f'<button class="{"on" if i == 0 else ""}" data-tab="{k}" role="tab" aria-selected="{"true" if i == 0 else "false"}">{n}</button>' for i, (k, n, _) in enumerate(ROWS))
rpanes = ''.join(f'<div data-pane="{k}" role="tabpanel"{"" if i == 0 else " hidden"}>{carousel("row-" + k, hs)}</div>' for i, (k, n, hs) in enumerate(ROWS))
rbtns = ''.join(f'<span data-pane="{k}"{"" if i == 0 else " hidden"}>{car_btns("row-" + k)}</span>' for i, (k, n, _) in enumerate(ROWS))

# 6 · Standards
lab_opts = ''.join(f'<option value="{LABMAP[h]}">{BY[h][1]}</option>' for h in sorted([p[0] for p in PRODUCTS], key=lambda x: BY[x][1])
                   if h in LABMAP and 'pack-of' not in h and 'kit' not in h and '5 L' not in BY[h][2] and h not in ('stone-pressed-groundnut-oil-copy', 'khapli-emmer-wheat-atta-5kg', 'stone-pressed-yellow-mustard-oil-5l', 'stone-pressed-sunflower-oil-5-ltr'))


# 8 · Product in focus
G = BY['a2-desi-cow-ghee-hand-churned-from-curd']

# 9 · Journey
JOURNEY = [('cows', 'Gir desi cows', 'Milk from free-grazing indigenous Gir cows.'),
           ('bilona_pot', 'Set into curd', 'Milk is boiled, cooled naturally, then set into curd overnight.'),
           ('churning', 'Hand-churned bilona', 'The curd is churned the traditional Bilona way.'),
           ('tested', 'Lab tested', 'The ghee lab report is published for you to read.'),
           ('family_table', 'To your table', 'Usually delivered in 3–5 days across India.')]
journey = ''.join(f'<div class="jcard reveal" style="--d:{i*.08}s"><div class="jcard__img"><img src="{PH[k]}&width=600" alt="{t}" loading="lazy" width="300" height="300"><span aria-hidden="true">{i+1}</span></div><h3>{t}</h3><p>{d}</p></div>' for i, (k, t, d) in enumerate(JOURNEY))

# 10 · Customer stories
tcards = ''.join(f'''<article class="tcard2"><div class="tcard2__img"><img src="{im}&width=600" alt="Photo shared by {n}" loading="lazy" width="300" height="400"></div>
  <div class="tcard2__body"><h3>{t}</h3><div class="tstars" role="img" aria-label="Rated 5 out of 5">★★★★★</div><p>{q}</p><footer><b>{n}</b><small>Product: {p}</small></footer></div></article>''' for t, q, n, p, im in TESTI)

# 13 · Knowledge
guides = ''.join(f'''<a class="guide reveal" style="--d:{i*.05}s" href="{SITE}{u}"><div class="guide__img"><img src="{im}&width=700" alt="" loading="lazy" width="700" height="394"></div><span class="guide__tag">{tag}</span><h3>{t}</h3></a>''' for i, (t, u, im, tag) in enumerate(GUIDES))
plans = ''.join(f'<li><b>₹{p}</b><span>{d}</span></li>' for d, p in PLANS)


# 4 · Explore our products (complete catalogue, one tab per category)
EXP = sorted([c for c in COLLECTIONS if c[-1]], key=lambda c: (c[0] == 'ghee', -len(c[-1])))  # ghee (one product page with 7 sizes) last
etabs = ''.join(f'<button class="{"on" if i == 0 else ""}" data-tab="x-{c[0]}" role="tab" id="xt-{c[0]}" aria-selected="{"true" if i == 0 else "false"}" aria-controls="xp-{c[0]}">{c[1]}</button>' for i, c in enumerate(EXP))
epanes = ''.join(f'''<div data-pane="x-{c[0]}" id="xp-{c[0]}" role="tabpanel" aria-labelledby="xt-{c[0]}"{"" if i == 0 else " hidden"}>
  <div class="xgrid">{''.join(pcard(h, '') for h in c[-1][:8])}</div>
  <div class="center" style="margin-top:22px"><a class="btn btn--outline" href="{curl(c[0])}">View all {len(c[-1])} in {c[1]}</a></div></div>''' for i, c in enumerate(EXP))

best5 = ''.join(pcard(h, 'reveal', i * .05) for i, h in enumerate(BEST5))

BODY = f'''
<h1 class="sr-only">Rosier Foods: Reviving the Tradition of Old Bharat. A2 bilona ghee, stone pressed oils, chakki atta, raw honey and pickles.</h1>

<!-- HERO BANNERS: edit config/banners.js -->
<section class="hb container" id="hero" aria-roledescription="carousel" aria-label="Offers and highlights">{NOSCRIPT_HERO}</section>
<script>window.RosierRender&&RosierRender.hero(document.getElementById('hero'))</script>

<!-- DISCOVERY: ptile tiles + category carousel, edit config/homepage.js -->
<section class="disc container" aria-label="Shop by category">
  <div class="disc__promos" id="promos">{NOSCRIPT_PROMOS}</div>
  <script>window.RosierRender&&RosierRender.promos(document.getElementById('promos'))</script>
  <div class="rcats" id="rcats">
    <div class="rcats__head"><h2 class="rcats__h">Shop by category</h2><a href="shop.html" class="rcats__all">View all</a></div>
    <div class="rcats__wrap">
      <button type="button" class="rcats__arw rcats__arw--p" aria-label="Previous categories"><svg aria-hidden="true"><use href="#i-arrow"/></svg></button>
      <div class="rcats__track" tabindex="0" aria-label="Categories, scroll sideways">{NOSCRIPT_CATS}</div>
      <button type="button" class="rcats__arw rcats__arw--n" aria-label="More categories"><svg aria-hidden="true"><use href="#i-arrow"/></svg></button>
    </div>
  </div>
  <script>window.RosierRender&&RosierRender.rcats(document.getElementById('rcats'))</script>
</section>

<!-- 1 · BESTSELLERS -->
<section class="section home-best" id="bestsellers" aria-labelledby="best-h">
  <div class="container">
    <div class="head-row reveal"><div>{eyebrow('Bestsellers')}<h2 id="best-h">Loved Across Generations</h2></div><a href="shop.html" class="link-arrow">Shop all {len(PRODUCTS)} products</a></div>
    <div class="best5">{best5}</div>
  </div>
</section>

<!-- 2 · SHOP BY NEED -->
<section class="needs" data-tabs aria-labelledby="need-h">
  <div class="container">
    <header class="section-head reveal" style="margin-bottom:26px">{eyebrow('Shop by need', True)}<h2 id="need-h">What are you shopping for today?</h2><p class="section-sub">Pick a need and we'll show you the right Rosier staples.</p></header>
    <div class="need-tabs reveal" role="tablist" aria-label="Shop by need">{ntabs}</div>
    {npanes}
  </div>
</section>

<!-- 3 · OUR STANDARDS -->
<section class="section bg-cream2" aria-labelledby="std-h">
  <div class="container">
    <header class="section-head reveal">{eyebrow('Our Standards', True)}<h2 id="std-h">Don't Just Trust Us. Check.</h2><p class="section-sub">Every quality claim on this site points to a document you can open.</p></header>
    <div class="proof">
      <div class="proof__lab reveal">
        <h3>Open the lab report for your product</h3>
        <p>Pick a product to open its lab test report in a new tab.</p>
        <div class="lab-pick"><label class="sr-only" for="lab-pick">Choose a product</label><select id="lab-pick"><option value="">Choose a product…</option>{lab_opts}</select><a id="lab-go" class="btn btn--primary disabled" target="_blank" rel="noopener" href="lab-reports.html" aria-disabled="true">Open report</a></div>
        <img class="proof__img" src="{PH['tested']}&width=900" alt="Rosier A2 ghee shown with its lab report" loading="lazy" width="900" height="506">
      </div>
      <div class="proof__side">
        <div class="proof__card reveal"><b>6</b><div><h3 class="h4like">FSSAI-licensed units</h3><p>The first letter of your batch number tells you which unit made your pack.</p><a href="standards.html#units" class="link-arrow">See units &amp; licence numbers</a></div></div>
        <div class="proof__card reveal"><b>32</b><div><h3 class="h4like">Products with lab reports</h3><p>Ghee, oils, atta, honey, oats, nut butters and pickles.</p><a href="lab-reports.html" class="link-arrow">All lab reports</a></div></div>
        <div class="proof__card reveal"><b>2-day</b><div><h3 class="h4like">Returns on damaged or wrong items</h3><p>Our delivery, return and cancellation terms, in plain words.</p><a href="standards.html#returns" class="link-arrow">Read the terms</a></div></div>
      </div>
    </div>
  </div>
</section>

<!-- 4 · EXPLORE OUR PRODUCTS -->
<section class="section" data-tabs id="explore" aria-labelledby="exp-h">
  <div class="container">
    <div class="head-row reveal"><div>{eyebrow('The full Rosier range')}<h2 id="exp-h">Explore our products</h2></div><a href="shop.html" class="link-arrow">Shop all</a></div>
    <div class="xtabs" role="tablist" aria-label="Product categories">{etabs}</div>
    {epanes}
  </div>
</section>

<!-- 5 · PRODUCT IN FOCUS -->
<section class="section bg-cream2" aria-labelledby="focus-h">
  <div class="container focus">
    <div class="focus__img reveal"><img src="{PH['art_of_slow']}&width=900" alt="Rosier Gir Cow A2 Bilona Ghee" loading="lazy" width="900" height="900"></div>
    <div class="reveal" style="--d:.1s">
      {eyebrow('Product in focus')}
      <h2 id="focus-h">Gir Cow A2 Bilona Ghee</h2>
      <div class="pdp__meta" style="margin-top:10px">{stars(4.9, '1,894 reviews')}<a href="{LABMAP[G[0]]}" target="_blank" rel="noopener">View lab report</a></div>
      <p style="margin-top:14px;color:var(--muted)">We set Gir cow milk into curd overnight, then churn it by hand the bilona way. It's slow, and that's the point.</p>
      <ul class="why"><li><svg aria-hidden="true"><use href="#i-check"/></svg>Made from curd, not milk or malai</li><li><svg aria-hidden="true"><use href="#i-check"/></svg>Slow-churned the traditional Bilona way</li><li><svg aria-hidden="true"><use href="#i-check"/></svg>From free-grazing Gir cows</li><li><svg aria-hidden="true"><use href="#i-check"/></svg>250 ml to 5 L, in glass jars or a steel dolchi</li></ul>
      <div class="pdp__price"><b>{inr(G[3])}</b><s>{inr(G[4])}</s><span class="off">{off(G[3], G[4])}% OFF</span></div>
      <p class="tax">Price for 250 ml. MRP inclusive of all taxes.</p>
      <div style="display:flex;gap:10px;flex-wrap:wrap;margin-top:20px"><button class="btn btn--primary" data-h="{G[0]}">Add to Cart</button><a href="product-a2-desi-cow-ghee-hand-churned-from-curd.html" class="btn btn--outline">See all sizes</a></div>
    </div>
  </div>
</section>

<!-- 6 · OUR TRADITIONAL PROCESS -->
<section class="exp" aria-labelledby="journey-h">
  <div class="container">
    <header class="section-head reveal" style="margin-bottom:34px">{eyebrow('Our traditional process', True)}<h2 id="journey-h">From Gir cow to your kitchen</h2><p class="hindi" lang="hi">असली स्वाद की एक सच्ची यात्रा</p></header>
    <div class="exp__video reveal"><video src="{H['video']}" muted loop playsinline preload="none" poster="{PH['churning']}&width=1200" controls aria-label="Video: how Rosier makes its food"></video></div>
    <div class="journey">{journey}</div>
    <div class="center mt-40 reveal"><a href="process.html" class="btn btn--outline">See our full process</a></div>
  </div>
</section>

<!-- 7 · CUSTOMER STORIES -->
<section class="testi bg-cream2" aria-labelledby="rev-h" style="padding-top:clamp(56px,7vw,90px)">
  <div class="container">
    <div class="head-row reveal"><div>{eyebrow('Customer stories')}<h2 id="rev-h">From our Rosier Parivaar</h2><p class="section-sub">Reviews featured on rosierfoods.com. Our A2 Ghee is rated 4.9 from 1,894 reviews.</p></div>{car_btns('testi')}</div>
    <div class="carousel reveal" data-carousel="testi"><div class="carousel__track carousel__track--t" tabindex="0" aria-label="Customer reviews, scroll sideways">{tcards}</div></div>
  </div>
</section>

<!-- 8 · OUR STORY -->
<section class="section ostory" aria-labelledby="os-h">
  <div class="container ostory__grid">
    <div class="ostory__img reveal"><img src="{HOME['family']}&width=1000" alt="Rosier's founder Gaurav with farming families" loading="lazy" width="1000" height="750"></div>
    <div class="reveal" style="--d:.1s">
      {eyebrow('Our story')}
      <h2 id="os-h">Reviving the Tradition of Old Bharat</h2>
      <p class="ostory__lead">Our founder Gaurav spent over 20 years in health and fitness before starting Rosier. He wants to bring India's food traditions back into modern kitchens, and Rosier is how he's doing it.</p>
      <ul class="ostory__trio">
        <li><span lang="hi">परंपरा</span><b>Tradition</b><small>Bilona, stone press, chakki.</small></li>
        <li><span lang="hi">शुद्धता</span><b>Purity</b><small>No refined oils. No additives.</small></li>
        <li><span lang="hi">ईमानदारी</span><b>Honesty</b><small>Lab reports, published.</small></li>
      </ul>
      <div style="display:flex;gap:10px;flex-wrap:wrap;margin-top:22px"><a href="our-story.html" class="btn btn--primary">Read our story</a><a href="founder.html" class="btn btn--outline">Meet our founder</a></div>
    </div>
  </div>
</section>

<!-- 9 · ROSIER PARIVAAR -->
<section style="padding:0 0 clamp(56px,7vw,90px)" aria-labelledby="club-h">
  <div class="container">
    <div class="club-band reveal">
      <div>{eyebrow("Rosier Parivaar membership", light=True)}<h2 id="club-h">Save 15% on every order</h2><p>Free &amp; fast shipping, a birthday surprise box and a free 1 L ghee on ₹15,000 of orders.</p><ul class="mini-plans">{plans}</ul><a href="membership.html#terms" class="btn btn--gold" style="margin-top:18px">See benefits &amp; terms</a></div>
      <ul class="club-perks"><li><svg aria-hidden="true"><use href="#i-tag"/></svg>15% off on all orders</li><li><svg aria-hidden="true"><use href="#i-truck"/></svg>Free &amp; fast shipping</li><li><svg aria-hidden="true"><use href="#i-gift"/></svg>Birthday surprise box</li><li><svg aria-hidden="true"><use href="#i-jar"/></svg>Free 1 L ghee on ₹15,000</li></ul>
    </div>
  </div>
</section>

<!-- 10 · RECIPES & KNOWLEDGE -->
<section class="section bg-cream2" aria-labelledby="learn-h">
  <div class="container">
    <div class="head-row reveal"><div>{eyebrow('Recipes & knowledge')}<h2 id="learn-h">Cook and learn with us</h2></div><a href="{SITE}/blogs/news" class="link-arrow">All articles</a></div>
    <div class="guides">{guides}</div>
    <p class="center mt-40">Have a question before you buy? <a href="faq.html" style="color:var(--brown);text-decoration:underline">Read our FAQs</a>.</p>
  </div>
</section>
'''
