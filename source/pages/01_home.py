FILE = 'index.html'
TITLE = 'A2 Ghee, Raw Honey, Atta & Cold Pressed Oils | Rosier Foods'
DESC = 'Reviving the tradition of Bharat. A2 Gir Cow Bilona Ghee, Wild Forest Honey, Khapli Atta and Stone Pressed Oils, made in FSSAI-licensed units with lab reports you can read.'
ACTIVE = 'home'
H = HOME

# 1. Hero + category entry
slides = ''.join(f'<a href="shop.html" class="hs-slide{" on" if i == 0 else ""}"><img src="{s}&width=1800" alt="Rosier Foods Diwali sale banner {i+1}" {"fetchpriority=high" if i == 0 else "loading=lazy"} width="1800" height="600"></a>' for i, s in enumerate(H['slides']))
dots = ''.join(f'<button class="{"on" if i == 0 else ""}" aria-label="Show banner {i+1}"></button>' for i in range(len(H['slides'])))
promos = ''.join(f'<a href="{"product-gond-laddoo.html" if "laddoo" in s else u}" class="ss-promo reveal" style="--d:{i*.08}s"><img src="{img(s, 800)}" alt="{a}" width="650" height="356"></a>' for i, (s, u, a) in enumerate(H['promo']))
cats = ''.join(f'<a href="{curl(k)}" class="ss-cat"><span class="ss-cat__img"><img src="{img(t, 300)}" alt="" width="120" height="128"></span><span>{"A2 Ghee" if k == "ghee" else n}</span></a>' for k, n, t, *_ in COLLECTIONS)

# 2. Shop by need (plain, non-medical labels)
NPH = {'staples': PH['ghee_spread'], 'winter': img(BY['amlaprash'][8], 9).split('&width')[0], 'protein': img(BY['high-protein-oats-assorted-pack'][8], 9).split('&width')[0],
       'cooking': PH['oil_range'], 'millets': img(BY['ragi-atta-1kg'][8], 9).split('&width')[0], 'taste': PH['oil_food']}
ntabs = ''.join(f'<button class="{"on" if i == 0 else ""}" data-tab="{k}" role="tab" aria-selected="{"true" if i == 0 else "false"}" aria-controls="need-{k}">{n}</button>' for i, (k, n, *_r) in enumerate(NEEDS))
npanes = ''.join(f'''<div class="need-pane" id="need-{k}" data-pane="{k}" role="tabpanel"{"" if i == 0 else " hidden"}>
  <div class="need-intro" style="--nbg:url('{NPH[k]}&width=900')"><p class="eyebrow eyebrow--light">Shop by need</p><h3>{n}</h3><p>{line}</p></div>
  <div class="need-grid">{''.join(pcard(h, '') for h in hs)}</div></div>''' for i, (k, n, line, hs) in enumerate(NEEDS))

# 3. One product row with tabs (replaces three separate carousels)
COMBOS = ['pickle-tasting-set', 'wild-forest-honey-pack-of-2', 'mango-pickle-natural-sun-dried-pack-of-2', 'stone-pressed-black-mustard-oil-oil-kit-5-ltr',
          'stone-pressed-groundnut-oil-oil-kit-5-ltr', 'khapli-emmer-wheat-atta-5kg', 'green-chilly-pickle-natural-sun-dried-pack-of-2', 'stone-pressed-yellow-mustard-oil-kit-5-ltr']
ROWS = [('best', 'Bestsellers', BEST), ('new', 'New arrivals', NEW), ('value', 'Value packs & family sizes', COMBOS)]
rtabs = ''.join(f'<button class="{"on" if i == 0 else ""}" data-tab="{k}" role="tab">{n}</button>' for i, (k, n, _) in enumerate(ROWS))
rpanes = ''.join(f'<div data-pane="{k}"{"" if i == 0 else " hidden"}>{carousel("row-" + k, hs)}</div>' for i, (k, n, hs) in enumerate(ROWS))
rbtns = ''.join(f'<span data-pane="{k}"{"" if i == 0 else " hidden"}>{car_btns("row-" + k)}</span>' for i, (k, n, _) in enumerate(ROWS))

# 4. Proof
lab_opts = ''.join(f'<option value="{LABMAP[h]}">{BY[h][1]}</option>' for h in sorted([p[0] for p in PRODUCTS], key=lambda x: BY[x][1])
                   if h in LABMAP and 'pack-of' not in h and 'kit' not in h and '5 L' not in BY[h][2] and h not in ('stone-pressed-groundnut-oil-copy', 'khapli-emmer-wheat-atta-5kg', 'stone-pressed-yellow-mustard-oil-5l', 'stone-pressed-sunflower-oil-5-ltr'))
bars = ''.join(f'<div class="bar"><span>{s} ★</span><i style="--w:{w}%"></i><span>{c}</span></div>' for s, w, c in [(5, 91, '1,720'), (4, 9, '165'), (3, .5, '8'), (2, .2, '1'), (1, 0, '0')])

# 5. Process
JOURNEY = [('cows', 'Gir desi cows', 'Milk from free-grazing indigenous Gir cows.'),
           ('bilona_pot', 'Set into curd', 'Milk is boiled, cooled naturally, then set into curd overnight.'),
           ('churning', 'Hand-churned bilona', 'The curd is churned the traditional Bilona way.'),
           ('tested', 'Lab tested', 'The ghee lab report is published for you to read.'),
           ('family_table', 'To your table', 'Usually delivered in 3–5 days across India.')]
journey = ''.join(f'<div class="jcard reveal" style="--d:{i*.08}s"><div class="jcard__img"><img src="{PH[k]}&width=600" alt="{t}" loading="lazy" width="300" height="300"><span>{i+1}</span></div><h3>{t}</h3><p>{d}</p></div>' for i, (k, t, d) in enumerate(JOURNEY))

# 7. Reviews
tcards = ''.join(f'''<article class="tcard2"><div class="tcard2__img"><img src="{im}&width=600" alt="{n}" loading="lazy"></div>
  <div class="tcard2__body"><h3>{t}</h3><div class="tstars" aria-label="5 out of 5 stars">★★★★★</div><p>{q}</p><footer><b>{n}</b><small>Reviewed: {p}</small></footer></div></article>''' for t, q, n, p, im in TESTI)

# 9. Helpful content
guides = ''.join(f'''<a class="guide reveal" style="--d:{i*.05}s" href="{SITE}{u}"><div class="guide__img"><img src="{im}&width=700" alt="" loading="lazy"></div><span class="guide__tag">{tag}</span><h3>{t}</h3></a>''' for i, (t, u, im, tag) in enumerate(GUIDES))
FAQ = [("What makes Rosier ghee different?", "It's made from the curd of free-grazing Gir cows' milk and churned the Bilona way, not made from milk or malai. It's rated 4.9 from 1,894 reviews on our store."),
       ("Can I see proof of quality?", 'Yes. Every claim we make links to evidence on our <a href="standards.html">Our Standards</a> page: the lab reports, the FSSAI-licensed units where our products are made, and how each product is made.'),
       ("How long does delivery take?", POLICY['delivery'] + ' Shipping charges, if any, are shown at checkout before you pay.'),
       ("What if my order arrives damaged or wrong?", POLICY['returns'] + ' ' + POLICY['unboxing']),
       ("Can I cancel my order?", POLICY['cancel']),
       ("What is the Rosier Benefit Club?", 'Our membership, from ₹299. Members get 15% off on all orders, free &amp; fast shipping, a birthday surprise box and more. <a href="membership.html">See plans and terms</a>.')]
faq = ''.join(f'<div class="acc-item"><button class="acc-q" aria-expanded="false">{q}<svg aria-hidden="true"><use href="#i-plus"/></svg></button><div class="acc-a"><div><p>{a}</p></div></div></div>' for q, a in FAQ)

BODY = f'''
<!-- 1 · HERO & PRIMARY ACTION -->
<section class="hs container" aria-label="Featured">
  <div class="hs__frame reveal">{slides}<div class="hs__dots">{dots}</div></div>
</section>
<section class="ss container" aria-label="Shop by category">
  <div class="ss__promos">{promos}</div>
  <div class="ss__cats reveal" style="--d:.15s"><button class="ss-arrow ss-arrow--prev" aria-label="Previous categories"><svg aria-hidden="true"><use href="#i-arrow"/></svg></button><div class="ss__track">{cats}</div><button class="ss-arrow" aria-label="More categories"><svg aria-hidden="true"><use href="#i-arrow"/></svg></button></div>
</section>

<!-- 2 · SHOP BY NEED -->
<section class="needs" data-tabs>
  <div class="container">
    <header class="section-head reveal" style="margin-bottom:26px"><h2 class="h-live">Where would you like to start?</h2><p class="section-sub">Pick what you're shopping for. We'll show you the right Rosier staples.</p><div class="motif motif--sm"></div></header>
    <div class="need-tabs reveal" role="tablist" aria-label="Shop by need">{ntabs}</div>
    {npanes}
  </div>
</section>

<!-- 3 · BESTSELLERS -->
<section class="home-row" data-tabs>
  <div class="container">
    <div class="head-row reveal"><h2 class="h-live">Loved Across Generations</h2><div style="display:flex;gap:18px;align-items:center">{rbtns}</div></div>
    <div class="row-tabs" role="tablist" aria-label="Product lists">{rtabs}</div>
    {rpanes}
    <div class="center" style="margin-top:8px"><a href="shop.html" class="btn btn--outline">Shop all {len(PRODUCTS)} products</a></div>
  </div>
</section>

<section class="strip" aria-hidden="true"><div class="strip__track">{''.join('<span>FOODS THAT HEAL, NOT HYPE</span><i>✦</i><span>PURE | TRADITIONAL | ETHICALLY CRAFTED</span><i>✦</i><span>REVIVING THE TRADITION OF BHARAT</span><i>✦</i>' for _ in range(3))}</div></section>

<!-- 4 · PROOF & QUALITY STANDARDS -->
<section class="section">
  <div class="container">
    <header class="section-head reveal">{eyebrow('Our Standards', True)}<h2>Don't just trust us. Check.</h2><p class="section-sub">Every quality claim on this site points to evidence you can open.</p></header>
    <div class="proof">
      <div class="proof__lab reveal">
        <h3>Read the lab report for your product</h3>
        <p>Pick a product and open its lab test report.</p>
        <div class="lab-pick"><label class="sr-only" for="lab-pick">Choose a product</label><select id="lab-pick"><option value="">Choose a product…</option>{lab_opts}</select><a id="lab-go" class="btn btn--primary disabled" target="_blank" rel="noopener" href="#">Open Report</a></div>
        <img class="proof__img" src="{PH['tested']}&width=900" alt="Rosier A2 ghee with its lab report" loading="lazy">
      </div>
      <div class="proof__side">
        <div class="proof__card reveal" style="--d:.06s"><b>6</b><div><h4>FSSAI-licensed units</h4><p>Every product is made in one of six licensed units. The first letter of your batch number tells you which one.</p><a href="standards.html#units" class="link-arrow">See the units <svg aria-hidden="true"><use href="#i-arrow"/></svg></a></div></div>
        <div class="proof__card reveal" style="--d:.12s"><b>32</b><div><h4>Products with lab reports</h4><p>Ghee, oils, atta, honey, oats, nut butters and pickles, all open to read.</p><a href="lab-reports.html" class="link-arrow">All lab reports <svg aria-hidden="true"><use href="#i-arrow"/></svg></a></div></div>
        <div class="proof__card reveal" style="--d:.18s"><b>4.9★</b><div><h4>1,894 reviews on our A2 Ghee</h4><div class="bars" style="margin-top:8px">{bars}</div></div></div>
      </div>
    </div>
    <div class="center mt-40 reveal"><a href="standards.html" class="btn btn--primary">Explore Our Standards <svg aria-hidden="true"><use href="#i-arrow"/></svg></a></div>
  </div>
</section>

<!-- 5 · PROCESS -->
<section class="exp bg-cream2">
  <div class="container">
    <header class="section-head reveal" style="margin-bottom:34px"><h2 class="h-live">The Rosier Foods Experience</h2><p class="hindi">असली स्वाद की एक सच्ची यात्रा</p></header>
    <div class="exp__video reveal"><video src="{H['video']}" autoplay muted loop playsinline preload="metadata" aria-label="How Rosier makes its food"></video></div>
    <header class="section-head reveal" style="margin:64px auto 0"><h3 style="font-size:clamp(26px,3vw,36px)">How your A2 ghee is made</h3></header>
    <div class="journey">{journey}</div>
    <div class="center mt-40 reveal"><a href="product.html" class="btn btn--primary">Shop A2 Bilona Ghee <svg aria-hidden="true"><use href="#i-arrow"/></svg></a></div>
  </div>
</section>

<!-- 6 · FOUNDER & BRAND STORY -->
<section class="brand">
  <div class="container brand__grid">
    <div class="brand__copy reveal">
      <img class="brand__logo" src="{HOME['logo_green']}&width=300" alt="Rosier – Nature's Love" onerror="this.src='assets/img/rosier-logo-green.png'">
      <h2>Reviving the tradition of <em>Bharat</em></h2>
      <p>For us, that means three concrete things: ghee made from curd and churned by hand, oils pressed on stone without chemicals or solvents, and grain ground slowly in a chakki.</p>
      <p>Our founder, Gaurav, spent over 20 years in health and fitness before starting Rosier. He believes milk from indigenous Gir desi cows is better for us than A1 milk, and that India's old food wisdom belongs in today's kitchens.</p>
      <ul class="brand__pillars"><li><b>Source to table</b><span>Direct relationships with heritage grain farmers.</span></li><li><b>Time-honoured</b><span>Bilona churning, stone-milling, stone pressing.</span></li><li><b>Pure</b><span>No refined oils. No additives.</span></li><li><b>Community</b><span>Fair trade and direct support to rural farming families.</span></li></ul>
      <a href="our-story.html" class="btn btn--primary">Read Our Story <svg aria-hidden="true"><use href="#i-arrow"/></svg></a>
    </div>
    <div class="brand__mosaic reveal" style="--d:.1s">
      <figure class="m1"><img src="{HOME['family']}&width=900" alt="Rosier's founder with farmers" loading="lazy"><figcaption>Our founder with farmers</figcaption></figure>
      <figure class="m2"><img src="{PH['churning']}&width=700" alt="Curd being churned the bilona way" loading="lazy"><figcaption>The bilona way</figcaption></figure>
      <figure class="m3"><img src="{PH['unit']}&width=700" alt="A Rosier Foods unit" loading="lazy"><figcaption>A Rosier unit</figcaption></figure>
    </div>
  </div>
</section>

<!-- 7 · REVIEWS -->
<section class="testi">
  <div class="container">
    <div class="head-row reveal"><div><h2 class="h-live">Loved by our Rosier Parivaar</h2><p class="section-sub">Customer reviews featured on rosierfoods.com.</p></div>{car_btns('testi')}</div>
    <div class="carousel reveal" data-carousel="testi"><div class="carousel__track carousel__track--t">{tcards}</div></div>
  </div>
</section>

<!-- 8 · MEMBERSHIP -->
<section style="padding:0 0 clamp(56px,7vw,90px)">
  <div class="container">
    <div class="club-band reveal">
      <div>{eyebrow("Rosier's Benefit Club", light=True)}<h2>Save 15% on every order</h2><p>Plans from ₹299. Earn it back in just 2 orders.</p><a href="membership.html" class="btn btn--gold">See Plans &amp; Terms</a></div>
      <ul class="club-perks"><li><svg aria-hidden="true"><use href="#i-tag"/></svg>15% off on all orders</li><li><svg aria-hidden="true"><use href="#i-truck"/></svg>Free &amp; fast shipping</li><li><svg aria-hidden="true"><use href="#i-gift"/></svg>Birthday surprise box</li><li><svg aria-hidden="true"><use href="#i-jar"/></svg>Free 1L ghee on ₹15,000</li></ul>
    </div>
  </div>
</section>

<!-- 9 · HELPFUL CONTENT -->
<section class="section bg-cream2">
  <div class="container">
    <div class="head-row reveal"><div>{eyebrow('Learn & cook')}<h2>Guides and recipes from our kitchen</h2></div><a href="{SITE}/blogs/news" class="link-arrow">All articles <svg aria-hidden="true"><use href="#i-arrow"/></svg></a></div>
    <div class="guides">{guides}</div>
  </div>
</section>
<section class="section">
  <div class="container hfaq">
    <header class="reveal">{eyebrow('Questions')}<h2>Before you buy</h2><p class="section-sub" style="margin-top:12px">Still have a question? Email <a href="mailto:{CONTACT_EMAIL}" style="color:var(--brown);text-decoration:underline">{CONTACT_EMAIL}</a> or chat with us on WhatsApp.</p><a href="https://wa.me/919711580581" class="btn btn--outline" style="margin-top:22px">Chat on WhatsApp</a></header>
    <div class="accordion reveal" style="--d:.1s">{faq}</div>
  </div>
</section>
<section style="padding-bottom:clamp(48px,6vw,80px)">
  <div class="container"><div class="nl reveal">
    <div><h2>Join the Rosier Parivaar</h2><p>Recipes, farm stories and first word on offers. Unsubscribe anytime.</p></div>
    <form data-demo><label class="sr-only" for="nl-email">Email</label><input id="nl-email" type="email" placeholder="Your email address" required><button class="btn btn--primary" type="submit">Subscribe</button>
      <label class="consent"><input type="checkbox" required> I agree to receive emails from Rosier Foods. I can unsubscribe anytime.</label>
      <p class="form-ok" style="width:100%">You're in! Welcome to the Parivaar.</p></form>
  </div></div>
</section>
'''
