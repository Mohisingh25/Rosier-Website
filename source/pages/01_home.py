FILE = 'index.html'
TITLE = 'A2 Ghee, Raw Honey, Atta & Cold Pressed Oils | Rosier Foods'
DESC = 'Reviving the tradition of Bharat. A2 Gir Cow Bilona Ghee, Wild Forest Honey, Khapli Atta, Stone Pressed Oils and more, with lab reports for 32 products.'
ACTIVE = 'home'
H = HOME

slides = ''.join(f'<a href="shop.html" class="hs-slide{" on" if i == 0 else ""}"><img src="{s}&width=1800" alt="Rosier Foods banner {i+1}" {"" if i == 0 else "loading=lazy"}></a>' for i, s in enumerate(H['slides']))
dots = ''.join(f'<button class="{"on" if i == 0 else ""}" aria-label="Slide {i+1}"></button>' for i in range(len(H['slides'])))
promos = ''.join(f'<a href="{"product-gond-laddoo.html" if "laddoo" in s else u}" class="ss-promo reveal" style="--d:{i*.08}s"><img src="{img(s, 800)}" alt="{a}"></a>' for i, (s, u, a) in enumerate(H['promo']))
cats = ''.join(f'<a href="{curl(k)}" class="ss-cat"><span class="ss-cat__img"><img src="{img(t, 300)}" alt="{n}"></span><span>{"A2 Ghee" if k == "ghee" else n}</span></a>' for k, n, t, *_ in COLLECTIONS)
values = [('Source To Table', 'Direct relationships with heritage grain farmers, ensuring sustainable sourcing.'),
          ('Time-Honored Techniques', 'Slow Bilona churning, traditional stone-milling, and authentic methods.'),
          ('Unwavering Purity', 'No refined oils, no additives—just pure, wholesome ingredients.'),
          ('Commitment to Community', 'Fair trade practices and direct support to rural farming families.')]
VPH = [PH['cows'], PH['churning'], PH['ghee_pour'], PH['family_table']]
vals = ''.join(f'<div class="pv reveal" style="--d:{i*.08}s"><div class="pv__img"><img src="{VPH[i]}&width=700" alt="{t}" loading="lazy"></div><div class="pv__txt"><span class="pv__n">0{i+1}</span><h3>{t}</h3><p>{d}</p></div></div>' for i, (t, d) in enumerate(values))
tcards = ''.join(f'''<article class="tcard2"><div class="tcard2__img"><img src="{im}&width=600" alt="{n}" loading="lazy"></div>
  <div class="tcard2__body"><h3>{t}</h3><div class="tstars">★★★★★</div><p>{q}</p><footer><b>{n}</b><small>{p}</small></footer></div></article>''' for t, q, n, p, im in TESTI)
digits = ''.join(f'<span class="roll" data-d="{d}"><span class="roll__col">{"".join(f"<i>{k}</i>" for k in range(10))}</span></span>' for d in '06034')
trust = ''.join(f'<img src="{t}&width=200" alt="" loading="lazy">' for t in H['trust'])

# Shop by need
NPH = {'gut': PH['ghee_spread'], 'immunity': img(BY['amlaprash'][8], 900).split('&width')[0], 'protein': img(BY['high-protein-oats-assorted-pack'][8], 900).split('&width')[0],
       'cooking': PH['oil_range'], 'millets': img(BY['ragi-atta-1kg'][8], 900).split('&width')[0], 'taste': PH['oil_food']}
ntabs = ''.join(f'<button class="{"on" if i == 0 else ""}" data-tab="{k}" role="tab" aria-selected="{"true" if i == 0 else "false"}">{n}</button>' for i, (k, n, *_r) in enumerate(NEEDS))
npanes = ''.join(f'''<div class="need-pane" id="need-{k}" data-pane="{k}" role="tabpanel"{"" if i == 0 else " hidden"}>
  <div class="need-intro" style="--nbg:url('{NPH[k]}&width=900')">{eyebrow('Shop by need', light=True)}<h3>{n}</h3><p>{line}</p><a href="shop.html" class="btn btn--gold btn--sm">Shop all <svg><use href="#i-arrow"/></svg></a></div>
  <div class="need-grid">{''.join(pcard(h, '') for h in hs)}</div></div>''' for i, (k, n, line, hs) in enumerate(NEEDS))

# Tabbed bestseller row
ROWS = [('best', 'Bestsellers', BEST),
        ('ghee-oils', 'Ghee & Oils', ['a2-desi-cow-ghee-hand-churned-from-curd'] + COL['stone-press-oil'][5][:7]),
        ('atta', 'Atta', COL['atta'][5]),
        ('breakfast', 'Healthy Breakfast', COL['healthy-snacking'][5][:8]),
        ('pickles', 'Pickles', COL['pickles'][5][:6])]
rtabs = ''.join(f'<button class="{"on" if i == 0 else ""}" data-tab="{k}">{n}</button>' for i, (k, n, _) in enumerate(ROWS))
rpanes = ''.join(f'<div data-pane="{k}"{"" if i == 0 else " hidden"}>{carousel("row-" + k, hs)}</div>' for i, (k, n, hs) in enumerate(ROWS))
rbtns = ''.join(f'<span data-pane="{k}"{"" if i == 0 else " hidden"}>{car_btns("row-" + k)}</span>' for i, (k, n, _) in enumerate(ROWS))

# Lab report picker
lab_opts = ''.join(f'<option value="{LABMAP[h]}">{BY[h][1]}</option>' for h in sorted([p[0] for p in PRODUCTS], key=lambda x: BY[x][1]) if h in LABMAP and 'pack-of' not in h and 'kit' not in h and '5 L' not in BY[h][2] and '5-ltr' not in h and '5l' not in h and h != 'stone-pressed-groundnut-oil-copy' and h != 'khapli-emmer-wheat-atta-5kg')
bars = ''.join(f'<div class="bar"><span>{s} ★</span><i style="--w:{w}%"></i><span>{c}</span></div>' for s, w, c in [(5, 91, '1,720'), (4, 9, '165'), (3, .5, '8'), (2, .2, '1'), (1, 0, '0')])

JOURNEY = [('cows', 'Free-grazing Gir cows', 'Fresh milk from indigenous Gir desi cows.'),
           ('bilona_pot', 'Boiled, cooled, set into curd', 'Milk is boiled, cooled naturally, then set into curd overnight.'),
           
           ('churning', 'Hand-churned bilona', 'The curd is churned by hand, the traditional Bilona way.'),
           ('tested', 'Lab tested', 'Every product here has its lab report published for you to read.'),
           ('family_table', 'On your family\'s table', 'Delivered across India, straight to your rasoi.')]
journey = ''.join(f'<div class="jcard reveal" style="--d:{i*.08}s"><div class="jcard__img"><img src="{PH[ic]}&width=700" alt="{t}" loading="lazy"><span>{i+1}</span></div><h3>{t}</h3><p>{d}</p></div>' for i, (ic, t, d) in enumerate(JOURNEY))

FAQ = [("What makes Rosier ghee different?", "We make it from the curd of free-grazing Gir cows' milk and churn it by hand, the Bilona way. It's rated 4.9 from 1,894 reviews."),
       ("Are your products lab tested?", f'Yes. We publish lab reports for 32 of our products. <a href="lab-reports.html">See them all here</a>, or use the report finder above.'),
       ("Do you use refined oils or additives?", "No. No refined oils, no additives. Our oils are stone pressed and our atta is stone ground."),
       ("Where do you deliver?", f'Across India. For timelines and charges, see our <a href="{SITE}/policies/shipping-policy">Shipping Policy</a>.'),
       ("What's on offer right now?", "Our Diwali Sale is live with up to 30% off. You also get a free bottle on orders of ₹2,499, a free tumbler on ₹4,999, and both on ₹7,999."),
       ("What if something isn't right with my order?", f'Our <a href="{SITE}/policies/refund-policy">Refund Policy</a> has you covered. You can also <a href="contact.html">write to us</a> or chat on WhatsApp.'),
       ("What is the Rosier Benefit Club?", 'Our membership, from ₹299. You get 15% off on all orders, free &amp; fast shipping, a birthday surprise box and more. <a href="membership.html">See plans</a>.')]
faq = ''.join(f'<div class="acc-item"><button class="acc-q" aria-expanded="false">{q}<svg><use href="#i-plus"/></svg></button><div class="acc-a"><div><p>{a}</p></div></div></div>' for q, a in FAQ)

BODY = f'''
<!-- HERO SLIDER -->
<section class="hs container">
  <div class="hs__frame reveal">{slides}<div class="hs__dots">{dots}</div></div>
</section>

<!-- PROMOS + CATEGORIES -->
<section class="ss container">
  <div class="ss__promos">{promos}</div>
  <div class="ss__cats reveal" style="--d:.15s"><button class="ss-arrow ss-arrow--prev" aria-label="Previous"><svg><use href="#i-arrow"/></svg></button><div class="ss__track">{cats}</div><button class="ss-arrow" aria-label="Next"><svg><use href="#i-arrow"/></svg></button></div>
</section>

<!-- SHOP BY NEED -->
<section class="needs" data-tabs>
  <div class="container">
    <header class="section-head reveal" style="margin-bottom:26px"><h2 class="h-live">What does your family need today?</h2><p class="section-sub">Pick a need, and we'll show you what Bharat's kitchens have trusted for generations.</p><div class="motif motif--sm"></div></header>
    <div class="need-tabs reveal" role="tablist">{ntabs}</div>
    {npanes}
  </div>
</section>

<!-- VILLAGE ILLUSTRATION -->
<section class="village container" aria-hidden="true">
  <img class="village__a reveal" src="{H['village']}&width=1260" alt="" loading="lazy">
  <img class="village__b reveal" style="--d:.1s" src="{H['village2']}&width=820" alt="" loading="lazy">
</section>

<!-- LOVED ACROSS GENERATIONS (tabbed) -->
<section class="home-row" data-tabs>
  <div class="container">
    <div class="head-row reveal"><h2 class="h-live">Loved Across Generations</h2><div style="display:flex;gap:18px;align-items:center"><a href="shop.html" class="link-arrow">View more <svg><use href="#i-arrow"/></svg></a>{rbtns}</div></div>
    <div class="row-tabs" role="tablist">{rtabs}</div>
    {rpanes}
  </div>
</section>

<!-- STRIP -->
<section class="strip" aria-label="Foods that heal, not hype"><div class="strip__track">{''.join('<span>FOODS THAT HEAL, NOT HYPE</span><i>✦</i><span>PURE | TRADITIONAL | ETHICALLY CRAFTED</span><i>✦</i><span>REVIVING THE TRADITION OF BHARAT</span><i>✦</i>' for _ in range(3))}</div></section>

<!-- NEW ARRIVALS -->
<section class="home-row">
  <div class="container">
    <div class="head-row reveal"><h2 class="h-live">New Arrivals</h2><div style="display:flex;gap:18px;align-items:center"><a href="shop.html" class="link-arrow">View more <svg><use href="#i-arrow"/></svg></a>{car_btns('new')}</div></div>
    {carousel('new', NEW)}
  </div>
</section>

<!-- DIWALI OFFER + VALUE PACKS (conversion) -->
<section class="home-row" style="padding-top:10px">
  <div class="container">
    <div class="offer reveal" style="--ob:url('{PH['hamper_spread']}&width=1600')">
      <div class="offer__copy"><p class="eyebrow eyebrow--light">Diwali Sale is live</p><h2>Up to 30% off, plus free gifts</h2>
        <ul class="offer__tiers"><li><b>₹2,499+</b><span>Free bottle</span></li><li><b>₹4,999+</b><span>Free tumbler</span></li><li><b>₹7,999+</b><span>Bottle + tumbler</span></li></ul>
        <div style="display:flex;gap:10px;flex-wrap:wrap"><a href="shop.html" class="btn btn--gold">Shop the Sale <svg><use href="#i-arrow"/></svg></a><a href="hampers.html" class="btn btn--ghost">Diwali Hampers</a></div></div>
    </div>
    <div class="head-row reveal" style="margin-top:56px"><div><h2 class="h-live">Value Packs &amp; Family Sizes</h2><p class="section-sub">Stock up your rasoi and save more on every kilo and litre.</p></div>{car_btns('combos')}</div>
    {carousel('combos', ['pickle-tasting-set','wild-forest-honey-pack-of-2','mango-pickle-natural-sun-dried-pack-of-2','stone-pressed-black-mustard-oil-oil-kit-5-ltr','stone-pressed-groundnut-oil-oil-kit-5-ltr','khapli-emmer-wheat-atta-5kg','green-chilly-pickle-natural-sun-dried-pack-of-2','stone-pressed-yellow-mustard-oil-kit-5-ltr'])}
  </div>
</section>

<!-- MORE THAN A BRAND -->
<section class="container family-wrap">
  <div class="family reveal">
    <div class="family__img"><img src="{H['family']}&width=1200" alt="Rosier founder with farmers" loading="lazy"></div>
    <div class="family__copy" style="--fbg:url('{H['family_bg']}')">
      <h2>More Than a Brand, A Family</h2>
      <p class="hindi">जड़ों से जुड़े लोग, असली बदलाव</p>
      <div class="counter" aria-label="06034">{digits}</div>
      <p class="family__cap">Every Number Tells a Story</p>
    </div>
  </div>
</section>

<!-- BRAND MANIFESTO -->
<section class="brand">
  <div class="container brand__grid">
    <div class="brand__copy reveal">
      <img class="brand__logo" src="{HOME['logo_green']}&width=300" alt="Rosier – Nature's Love" onerror="this.src='assets/img/rosier-logo-green.png'">
      <h2>Reviving the tradition of <em>Bharat</em></h2>
      <p>Before refined oils and factory ghee, every Indian kitchen ran on slow food: ghee churned by hand, oil pressed on stone, grain milled fresh. We're bringing that kitchen back.</p>
      <ul class="brand__pillars"><li><b>Pure</b><span>No refined oils. No additives.</span></li><li><b>Traditional</b><span>Bilona, stone pressed, stone ground.</span></li><li><b>Ethically crafted</b><span>Fair trade with rural farming families.</span></li></ul>
      <a href="our-story.html" class="btn btn--primary">Read Our Story <svg><use href="#i-arrow"/></svg></a>
    </div>
    <div class="brand__mosaic reveal" style="--d:.1s">
      <figure class="m1"><img src="{PH['churning']}&width=900" alt="Women churning curd the bilona way" loading="lazy"><figcaption>Hand-churned bilona</figcaption></figure>
      <figure class="m2"><img src="{PH['cows']}&width=700" alt="Indigenous Gir cows" loading="lazy"><figcaption>Gir desi cows</figcaption></figure>
      <figure class="m3"><img src="{PH['ghee_pour']}&width=700" alt="Golden A2 ghee being poured" loading="lazy"><figcaption>Golden A2 ghee</figcaption></figure>
      <figure class="m4"><img src="{PH['unit']}&width=700" alt="The Rosier unit" loading="lazy"><figcaption>Our home</figcaption></figure>
    </div>
  </div>
</section>

<!-- EXPERIENCE + JOURNEY -->
<section class="exp">
  <div class="container">
    <header class="section-head reveal" style="margin-bottom:34px"><h2 class="h-live">The Rosier Foods Experience</h2><p class="hindi">असली स्वाद की एक सच्ची यात्रा</p></header>
    <div class="exp__video reveal"><video src="{H['video']}" autoplay muted loop playsinline preload="metadata"></video></div>
    <header class="section-head reveal" style="margin:72px auto 0">{eyebrow('From Gir cow to your kitchen', True)}<h2 style="font-size:clamp(28px,3.2vw,40px)">How your A2 ghee is made</h2></header>
    <div class="journey">{journey}</div>
    <div class="hv-grid">{vals}</div>
    <a href="our-story.html" class="hband reveal" style="--hb:url('{PH['cows']}&width=2000')"><div><p class="eyebrow eyebrow--light">Our heritage</p><h3>Indigenous Gir cows. Village bilona. Real food.</h3><span class="btn btn--gold">Explore Our Heritage <svg><use href="#i-arrow"/></svg></span></div></a>
  </div>
</section>

<!-- PROOF: LAB + REVIEWS -->
<section class="section" style="padding-top:clamp(40px,5vw,70px)">
  <div class="container proof">
    <div class="proof__lab reveal">
      {eyebrow("Don't just trust us")}
      <h3>Check the lab report for your product</h3>
      <p>Pick any product and open its lab test report. Read it, then decide.</p>
      <div class="lab-pick"><select id="lab-pick" aria-label="Choose a product"><option value="">Choose a product…</option>{lab_opts}</select><a id="lab-go" class="btn btn--primary disabled" target="_blank" rel="noopener" href="#">Open Report <svg><use href="#i-arrow"/></svg></a></div>
      <img class="proof__img" src="{PH['tested']}&width=900" alt="Rosier A2 ghee with its lab report" loading="lazy"><div class="proof__chips"><span><svg><use href="#i-check"/></svg>No refined oils</span><span><svg><use href="#i-check"/></svg>No additives</span><span><svg><use href="#i-check"/></svg>32 products with public reports</span></div>
    </div>
    <div class="proof__rev reveal" style="--d:.1s">
      {eyebrow('Real families, real words')}
      <h3>Our A2 Ghee, as rated by you</h3>
      <div class="rv-big"><b>4.9</b><div><span class="tstars">★★★★★</span><small>from 1,894 reviews</small></div></div>
      <div class="bars">{bars}</div>
      <a href="product.html#reviews" class="link-arrow" style="margin-top:20px">Read the reviews <svg><use href="#i-arrow"/></svg></a>
    </div>
  </div>
</section>

<!-- TESTIMONIALS -->
<section class="testi">
  <div class="container">
    <div class="head-row reveal"><h2 class="h-live">Loved by our Rosier Parivaar</h2>{car_btns('testi')}</div>
    <div class="carousel reveal" data-carousel="testi"><div class="carousel__track carousel__track--t">{tcards}</div></div>
  </div>
</section>

<!-- FOUNDER -->
<section class="section bg-cream2">
  <div class="container founder">
    <div class="founder__img reveal"><img src="{H['family']}&width=1000" alt="Gaurav with Rosier's farmer family" loading="lazy"></div>
    <div class="reveal" style="--d:.1s">
      {eyebrow('A note from our founder')}
      <blockquote>Reviving the traditional ways of Old Bharat, one kitchen at a time.</blockquote>
      <p>Gaurav has spent over 20 years in the health and fitness industry. Indian culture and timeless values sit at the heart of what he believes, and he's deeply drawn to the ancient Indian sciences and the Vedas.</p>
      <p>He started Rosier to bring that wisdom back to your table: milk from indigenous Gir desi cows, grains milled on stone, oils pressed the slow way.</p>
      <p class="sig">— Gaurav, Founder</p>
      <a href="our-story.html" class="btn btn--outline" style="margin-top:24px">Read our story</a>
    </div>
  </div>
</section>

<!-- CLUB -->
<section style="padding:clamp(56px,7vw,90px) 0 0">
  <div class="container">
    <div class="club-band reveal">
      <div>{eyebrow("Rosier's Benefit Club", light=True)}<h2>Save 15% on every order</h2><p>Join from just ₹299. Earn it back in just 2 orders.</p><a href="membership.html" class="btn btn--gold">Join the Club <svg><use href="#i-arrow"/></svg></a></div>
      <ul class="club-perks"><li><svg><use href="#i-tag"/></svg>15% off on all orders</li><li><svg><use href="#i-truck"/></svg>Free &amp; fast shipping</li><li><svg><use href="#i-gift"/></svg>Birthday surprise box</li><li><svg><use href="#i-jar"/></svg>Free 1L ghee on ₹15,000</li></ul>
    </div>
  </div>
</section>

<!-- FAQ -->
<section class="section">
  <div class="container hfaq">
    <header class="reveal">{eyebrow('Questions')}<h2>Got questions?<br>We've got answers.</h2><p class="section-sub" style="margin-top:12px">Still curious? Chat with us on WhatsApp, we're happy to help.</p><a href="https://wa.me/919711580581" class="btn btn--outline" style="margin-top:22px">Chat on WhatsApp</a></header>
    <div class="accordion reveal" style="--d:.1s">{faq}</div>
  </div>
</section>

<!-- NEWSLETTER -->
<section style="padding-bottom:clamp(40px,5vw,60px)">
  <div class="container"><div class="nl reveal">
    <div><h2>Join the Rosier Parivaar</h2><p>Farm stories, recipes and first word on offers. No spam, promise.</p></div>
    <form data-demo><input type="email" placeholder="Your email address" aria-label="Email" required><button class="btn btn--primary" type="submit">Subscribe</button><p class="form-ok" style="width:100%">You're in! Welcome to the Parivaar.</p></form>
  </div></div>
</section>

<!-- TRUST ICONS -->
<section class="trust container" aria-label="Our promises"><div class="trust__row">{trust}</div></section>
'''
