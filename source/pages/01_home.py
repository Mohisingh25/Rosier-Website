FILE = 'index.html'
TITLE = 'Rosier Foods | A2 Bilona Ghee, Stone Pressed Oils & Khapli Atta'
DESC = 'Reviving the Tradition of Old Bharat. A2 Gir cow bilona ghee, stone pressed oils, stone-ground atta, raw honey and sun-dried pickles. Made in FSSAI-licensed units, lab reports published.'
ACTIVE = 'home'
H = HOME
HERO = PH['ghee_pour']
HEAD = f'<link rel="preload" as="image" href="{HERO}&width=1600" fetchpriority="high">'

# 4 · Shop by need
NPH = {'cooking': PH['oil_range'], 'breakfast': img(BY['high-protein-oats-assorted-pack'][8], 9).split('&width')[0],
       'grains': img(BY['khapli-emmer-wheat-atta-stoneground-high-fiber-for-gut-health'][8], 9).split('&width')[0], 'family': PH['ghee_spread'],
       'winter': img(BY['amlaprash'][8], 9).split('&width')[0], 'taste': PH['oil_food']}
ntabs = ''.join(f'<button class="{"on" if i == 0 else ""}" data-tab="{k}" role="tab" id="tab-{k}" aria-selected="{"true" if i == 0 else "false"}" aria-controls="need-{k}">{n}</button>' for i, (k, n, *_r) in enumerate(NEEDS))
npanes = ''.join(f'''<div class="need-pane" id="need-{k}" data-pane="{k}" role="tabpanel" aria-labelledby="tab-{k}"{"" if i == 0 else " hidden"}>
  <div class="need-intro" style="--nbg:url('{NPH[k]}&width=900')"><p class="eyebrow eyebrow--light">Shop by need</p><h3>{n}</h3><p>{line}</p></div>
  <div class="need-grid">{''.join(pcard(h, '') for h in hs)}</div></div>''' for i, (k, n, line, hs) in enumerate(NEEDS))

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

# 7 · Categories
CT = [(curl('ghee'), 'A2 Bilona Ghee', 'Made from curd, hand-churned', PH['ghee_pour']),
      (curl('stone-press-oil'), 'Stone-pressed oils', 'Mustard, groundnut, coconut & more', PH['oil_range']),
      (curl('atta'), 'Atta & grains', 'Stone-ground in a chakki', img(BY['khapli-emmer-wheat-atta-stoneground-high-fiber-for-gut-health'][8], 9).split('&width')[0]),
      (curl('pickles'), 'Pickles', 'Sun-dried, ghar jaisa', img(BY['mango-pickle'][8], 9).split('&width')[0]),
      (curl('healthy-snacking'), 'Breakfast', 'High protein oats', img(BY['high-protein-oats-assorted-pack'][8], 9).split('&width')[0]),
      (curl('honey'), 'Honey & Amlaprash', 'Wild forest honey', img(BY['wild-flower-honey'][8], 9).split('&width')[0]),
      (curl('nut-butters'), 'Nut butters', 'Almond, peanut, cashew', img(BY['nut-butter-dark-chocolate'][8], 9).split('&width')[0]),
      ('hampers.html', 'Hampers & gifting', 'Parampara Diwali hampers', PH['hamper_gift'])]
ctiles = ''.join(f'<a class="ctile reveal" style="--d:{i*.04:.2f}s" href="{u}"><img src="{im}&width={900 if i == 0 else 500}" alt="" loading="lazy"><span>{t}<small>{s}</small></span></a>' for i, (u, t, s, im) in enumerate(CT))

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

BODY = f'''
<!-- 3 · HERO (brand-first) -->
<section class="bhero" aria-labelledby="hero-h">
  <div class="bhero__img"><img src="{HERO}&width=1600" srcset="{HERO}&width=800 800w, {HERO}&width=1600 1600w, {HERO}&width=2200 2200w" sizes="100vw" alt="Golden A2 bilona ghee being poured" width="1600" height="900" fetchpriority="high"></div>
  <div class="container"><div class="bhero__copy">
    <h1 id="hero-h">Reviving the Tradition of Old Bharat</h1>
    <p class="hindi-line" lang="hi">परंपरा • शुद्धता • ईमानदारी</p>
    <p class="lead">Ghee churned from curd, oils pressed on stone, grain milled in a chakki. Real food, made the slow way, with the lab reports to show for it.</p>
    <div class="bhero__cta"><a href="shop.html" class="btn btn--gold">Shop Bestsellers</a><a href="standards.html" class="btn btn--light">Know Your Food</a></div>
  </div></div>
</section>

<!-- 4 · SHOP BY NEED -->
<section class="needs" data-tabs aria-labelledby="need-h">
  <div class="container">
    <header class="section-head reveal" style="margin-bottom:26px"><h2 class="h-live" id="need-h">What are you shopping for today?</h2><p class="section-sub">Pick a need and we'll show you the right Rosier staples.</p></header>
    <div class="need-tabs reveal" role="tablist" aria-label="Shop by need">{ntabs}</div>
    {npanes}
  </div>
</section>

<!-- 5 · BESTSELLERS -->
<section class="home-row" data-tabs aria-labelledby="best-h">
  <div class="container">
    <div class="head-row reveal"><h2 class="h-live" id="best-h">Loved Across Generations</h2><div style="display:flex;gap:18px;align-items:center">{rbtns}</div></div>
    <div class="row-tabs" role="tablist" aria-label="Product lists">{rtabs}</div>
    {rpanes}
    <div class="center" style="margin-top:8px"><a href="shop.html" class="btn btn--outline">Shop all {len(PRODUCTS)} products</a></div>
  </div>
</section>

<!-- 6 · OUR STANDARDS -->
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

<!-- 7 · SHOP BY CATEGORY -->
<section class="section" aria-labelledby="cat-h">
  <div class="container">
    <div class="head-row reveal"><h2 class="h-live" id="cat-h">Shop by category</h2><a href="shop.html" class="link-arrow">Shop all</a></div>
    <div class="catgrid">{ctiles}</div>
  </div>
</section>

<!-- 8 · PRODUCT IN FOCUS -->
<section class="section bg-cream2" aria-labelledby="focus-h">
  <div class="container focus">
    <div class="focus__img reveal"><img src="{PH['art_of_slow']}&width=900" alt="Rosier Gir Cow A2 Bilona Ghee" loading="lazy" width="900" height="900"></div>
    <div class="reveal" style="--d:.1s">
      {eyebrow('Product in focus')}
      <h2 id="focus-h">Gir Cow A2 Bilona Ghee</h2>
      <div class="pdp__meta" style="margin-top:10px">{stars(4.9, '1,894 reviews')}<a href="{LABMAP[G[0]]}" target="_blank" rel="noopener">View lab report</a></div>
      <ul class="why"><li><svg aria-hidden="true"><use href="#i-check"/></svg>Made from curd, not milk or malai</li><li><svg aria-hidden="true"><use href="#i-check"/></svg>Slow-churned the traditional Bilona way</li><li><svg aria-hidden="true"><use href="#i-check"/></svg>From free-grazing Gir cows</li><li><svg aria-hidden="true"><use href="#i-check"/></svg>250 ml to 5 L, in glass jars or a steel dolchi</li></ul>
      <div class="pdp__price"><b>{inr(G[3])}</b><s>{inr(G[4])}</s><span class="off">{off(G[3], G[4])}% OFF</span></div>
      <p class="tax">Price for 250 ml. MRP inclusive of all taxes.</p>
      <div style="display:flex;gap:10px;flex-wrap:wrap;margin-top:20px"><button class="btn btn--primary" data-h="{G[0]}">Add to Cart</button><a href="product-a2-desi-cow-ghee-hand-churned-from-curd.html" class="btn btn--outline">See all sizes</a></div>
    </div>
  </div>
</section>

<!-- 9 · OUR JOURNEY -->
<section class="exp" aria-labelledby="journey-h">
  <div class="container">
    <header class="section-head reveal" style="margin-bottom:34px"><h2 class="h-live" id="journey-h">Our Journey: from Gir cow to your kitchen</h2><p class="hindi" lang="hi">असली स्वाद की एक सच्ची यात्रा</p></header>
    <div class="exp__video reveal"><video src="{H['video']}" muted loop playsinline preload="none" poster="{PH['churning']}&width=1200" controls aria-label="Video: how Rosier makes its food"></video></div>
    <div class="journey">{journey}</div>
    <div class="center mt-40 reveal"><a href="process.html" class="btn btn--outline">See our full process</a></div>
  </div>
</section>

<!-- 10 · CUSTOMER STORIES -->
<section class="testi bg-cream2" aria-labelledby="rev-h" style="padding-top:clamp(56px,7vw,90px)">
  <div class="container">
    <div class="head-row reveal"><div><h2 class="h-live" id="rev-h">Customer stories</h2><p class="section-sub">Reviews featured on rosierfoods.com. Our A2 Ghee is rated 4.9 from 1,894 reviews.</p></div>{car_btns('testi')}</div>
    <div class="carousel reveal" data-carousel="testi"><div class="carousel__track carousel__track--t" tabindex="0" aria-label="Customer reviews, scroll sideways">{tcards}</div></div>
  </div>
</section>

<!-- 11 · FARMER STORIES (verified content pending) -->
<section class="section" aria-labelledby="farm-h">
  <div class="container farmers reveal">
    <div>
      {eyebrow('Farmer stories')}
      <h2 id="farm-h" style="font-size:var(--fs-2xl)">The families behind our food</h2>
      <p style="margin-top:12px;color:var(--muted)">We work directly with heritage grain farmers and support rural farming families. We're documenting their stories, with their permission, so you can meet them here properly.</p>
      <a href="farmers.html" class="btn btn--outline" style="margin-top:20px">How we work with farmers</a>
    </div>
    <div class="farmers__img"><img src="{HOME['family']}&width=900" alt="Rosier's founder with farmers" loading="lazy" width="900" height="675"></div>
  </div>
</section>

<!-- 12 · ROSIER PARIVAAR -->
<section style="padding:0 0 clamp(56px,7vw,90px)" aria-labelledby="club-h">
  <div class="container">
    <div class="club-band reveal">
      <div>{eyebrow("Rosier Parivaar membership", light=True)}<h2 id="club-h">Save 15% on every order</h2><p>Free &amp; fast shipping, a birthday surprise box and a free 1 L ghee on ₹15,000 of orders.</p><ul class="mini-plans">{plans}</ul><a href="membership.html#terms" class="btn btn--gold" style="margin-top:18px">See benefits &amp; terms</a></div>
      <ul class="club-perks"><li><svg aria-hidden="true"><use href="#i-tag"/></svg>15% off on all orders</li><li><svg aria-hidden="true"><use href="#i-truck"/></svg>Free &amp; fast shipping</li><li><svg aria-hidden="true"><use href="#i-gift"/></svg>Birthday surprise box</li><li><svg aria-hidden="true"><use href="#i-jar"/></svg>Free 1 L ghee on ₹15,000</li></ul>
    </div>
  </div>
</section>

<!-- 13 · RECIPES & KNOWLEDGE -->
<section class="section bg-cream2" aria-labelledby="learn-h">
  <div class="container">
    <div class="head-row reveal"><div>{eyebrow('Recipes & knowledge')}<h2 id="learn-h">Cook and learn with us</h2></div><a href="{SITE}/blogs/news" class="link-arrow">All articles</a></div>
    <div class="guides">{guides}</div>
    <p class="center mt-40">Have a question before you buy? <a href="faq.html" style="color:var(--brown);text-decoration:underline">Read our FAQs</a>.</p>
  </div>
</section>
'''
