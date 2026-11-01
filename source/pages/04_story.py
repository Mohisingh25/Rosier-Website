FILE = 'our-story.html'
TITLE = 'Our Story | Rosier Foods – Reviving the Tradition of Bharat'
DESC = 'We are reviving the traditional ways of Old Bharat. The story, the people, the Gir cows and the slow methods behind Rosier Foods.'
ACTIVE = 'story'

values = [('Source To Table', 'Direct relationships with heritage grain farmers, ensuring sustainable sourcing.', PH['cows']),
          ('Time-Honored Techniques', 'Slow Bilona churning, traditional stone-milling, and authentic methods.', PH['churning']),
          ('Unwavering Purity', 'No refined oils, no additives—just pure, wholesome ingredients.', PH['ghee_pour']),
          ('Commitment to Community', 'Fair trade practices and direct support to rural farming families.', HOME['family'])]
vals = ''.join(f'<div class="pv reveal" style="--d:{i*.08}s"><div class="pv__img"><img src="{im}&width=700" alt="{t}" loading="lazy"></div><div class="pv__txt"><span class="pv__n">0{i+1}</span><h3>{t}</h3><p>{d}</p></div></div>' for i, (t, d, im) in enumerate(values))
steps = [('cows', 'Free-grazing Gir cows', 'Fresh milk from indigenous Gir desi cows.'),
         ('bilona_pot', 'Boiled, cooled, set into curd', 'Milk is boiled, cooled naturally, then set into curd overnight.'),
         ('churning', 'Hand-churned bilona', 'The curd is churned by hand, the traditional Bilona way.'),
         ('tested', 'Lab tested', 'Lab reports published for you to read.'),
         ('family_table', "On your family's table", 'Delivered across India, straight to your rasoi.')]
journey = ''.join(f'<div class="jcard reveal" style="--d:{i*.08}s"><div class="jcard__img"><img src="{PH[k]}&width=700" alt="{t}" loading="lazy"><span>{i+1}</span></div><h3>{t}</h3><p>{d}</p></div>' for i, (k, t, d) in enumerate(steps))

BODY = f'''
<section class="photo-hero" style="--ph:url('{PH['churning']}&width=2200')">
  <div class="container">
    <nav class="crumbs reveal"><a href="index.html">Home</a><span>/</span>Our Story</nav>
    <h1 class="reveal">We're reviving the traditional ways of <em>Old Bharat</em></h1>
    <p class="reveal" style="--d:.1s">Old Bharat's wisdom still shows us the way to eat well. We take age-old recipes, natural methods and trusted ingredients, and hold them to modern quality standards.</p>
  </div>
</section>

<section class="section">
  <div class="container split">
    <div class="split__media reveal"><div class="frame frame--arch"><img src="{PH['ghee_spread']}&width=1000" alt="Rosier A2 ghee on the family table" loading="lazy"></div></div>
    <div class="reveal" style="--d:.1s">
      {eyebrow('Our story')}
      <h2>It started at the dining table</h2>
      <p>We believe good food brings people together. That simple idea grew into our mission: make food that nourishes you, respects the land and is made with real care.</p>
      <p>We source from farmers and suppliers who share our values. We blend traditional recipes with how you cook today. And we never compromise on quality, freshness or flavour.</p>
      <p class="hindi" style="font-style:italic">Rosier Foods — where taste meets care.</p>
    </div>
  </div>
</section>

<section class="strip" aria-label="Proudly obsessed with tradition"><div class="strip__track">{''.join('<span>PROUDLY &amp; PASSIONATELY OBSESSED WITH TRADITION</span><i>✦</i><span>THE TASTE OF NATURE</span><i>✦</i><span>REVIVING THE TRADITION OF BHARAT</span><i>✦</i>' for _ in range(3))}</div></section>

<section class="section">
  <div class="container">
    <header class="section-head reveal">{eyebrow('What we stand for', True)}<h2>Think about what's on your plate</h2><p class="section-sub">Most of us don't stop to think about what we eat, or how it's made. We'd love for you to choose food that keeps your family strong. Here's our side of the promise.</p></header>
    <div class="hv-grid" style="margin-top:0">{vals}</div>
  </div>
</section>

<section class="section bg-cream2">
  <div class="container">
    <header class="section-head reveal">{eyebrow('Making of Rosier Gir Cow A2 Ghee', True)}<h2>Slow, the way it should be</h2></header>
    <div class="journey" style="margin-top:20px">{journey}</div>
    <div class="exp__video reveal" style="margin-top:56px"><video src="{HOME['video']}" autoplay muted loop playsinline preload="metadata"></video></div>
    <div class="center mt-40 reveal"><a href="product.html" class="btn btn--primary">Shop A2 Ghee <svg><use href="#i-arrow"/></svg></a></div>
  </div>
</section>

<section class="section">
  <div class="container split split--rev">
    <div class="split__media reveal"><div class="frame"><img src="{PH['cow_sun']}&width=1100" alt="A Gir cow at the farm" loading="lazy"></div></div>
    <div class="reveal" style="--d:.1s">
      {eyebrow('Sustainability')}
      <h2>Good for you. Good for the planet.</h2>
      <p>Our products are minimally processed, made from ingredients that are sustainably sourced and consciously grown. We work closely with our farmer family, because we believe a healthy choice should be healthy for the earth too.</p>
    </div>
  </div>
</section>

<section class="section bg-cream2">
  <div class="container founder">
    <div class="founder__img reveal"><img src="{HOME['family']}&width=1000" alt="Rosier's founder with farmers" loading="lazy"></div>
    <div class="reveal" style="--d:.1s">
      {eyebrow('A note from our founder')}
      <blockquote>Restoring India's traditions in modern life.</blockquote>
      <p>Gaurav has spent over 20 years in the health and fitness industry. Indian culture and timeless values sit at the heart of everything he believes in, and he's deeply drawn to the ancient Indian sciences and the Vedas.</p>
      <p>He believes milk from indigenous Gir desi cows, the kind described in our ancient texts, is better for us than A1 milk from HF and Jersey cows. Rosier is his way of bringing that heritage home to you.</p>
      <p class="sig">— Gaurav, Founder</p>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="hband reveal" style="--hb:url('{PH['unit']}&width=2000');margin-top:0"><div><p class="eyebrow eyebrow--light">The Rosier promise</p><h3>Bringing the wisdom and flavors of Old Bharat to today's tables</h3><a href="shop.html" class="btn btn--gold">Shop Now <svg><use href="#i-arrow"/></svg></a></div></div>
  </div>
</section>
'''
