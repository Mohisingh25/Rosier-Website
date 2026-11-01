FILE = 'our-story.html'
TITLE = 'Our Story | Rosier Foods'
DESC = 'We are reviving the traditional ways of Old Bharat. The story, values and founder behind Rosier Foods.'
ACTIVE = 'story'

BODY = f'''
<section class="page-hero">
  <div class="container">
    <nav class="crumbs reveal"><a href="index.html">Home</a><span>/</span>Our Story</nav>
    <h1 class="reveal" style="--d:.06s">We're reviving the traditional<br>ways of <em>Old Bharat</em></h1>
    <p class="lead reveal" style="--d:.12s">Old Bharat's wisdom still shows us the way to eat well. We take age-old recipes, natural methods and trusted ingredients, and hold them to modern quality standards.</p>
  </div>
</section>

<section class="section">
  <div class="container split">
    <div class="split__media reveal"><div class="frame frame--arch"><img src="assets/img/combo-oil-atta.jpg" alt="Rosier stone pressed oil and atta" loading="lazy"></div></div>
    <div class="reveal" style="--d:.1s">
      {eyebrow('Our story')}
      <h2>It started at the dining table</h2>
      <p>We believe good food brings people together. That simple idea grew into our mission: make food that nourishes you, respects the land and is made with real care.</p>
      <p>We source from farmers and suppliers who share our values. We blend traditional recipes with how you cook today. And we never compromise on quality, freshness or flavour.</p>
      <p class="hindi" style="font-style:italic">Rosier Foods — where taste meets care.</p>
    </div>
  </div>
</section>

<section class="tagline" aria-label="Proudly obsessed with tradition">
  <div class="tagline__track">{''.join('<span>Proudly &amp; passionately obsessed with tradition</span><i>✦</i><span>The taste of nature</span><i>✦</i>' for _ in range(3))}</div>
</section>

<section class="section bg-cream2">
  <div class="container">
    <header class="section-head reveal">{eyebrow('What we stand for', True)}<h2>Think about what's on your plate</h2><p class="section-sub">Most of us don't stop to think about what we eat, or how it's made. We'd love for you to choose food that keeps your family strong. Here's our side of the promise.</p></header>
    <div class="values">
      <div class="value reveal"><span class="ico"><svg><use href="#i-hands"/></svg></span><h3>Source to Table</h3><p>Direct ties with heritage grain farmers and sustainable sourcing.</p></div>
      <div class="value reveal" style="--d:.06s"><span class="ico"><svg><use href="#i-mill"/></svg></span><h3>Time-Honored Techniques</h3><p>Bilona churning, stone milling and other traditional methods.</p></div>
      <div class="value reveal" style="--d:.12s"><span class="ico"><svg><use href="#i-leaf"/></svg></span><h3>Unwavering Purity</h3><p>No refined oils and no additives. Ever.</p></div>
      <div class="value reveal" style="--d:.18s"><span class="ico"><svg><use href="#i-heart"/></svg></span><h3>Commitment to Community</h3><p>Fair trade that supports rural farming families.</p></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container split split--rev">
    <div class="split__media reveal"><div class="frame"><img src="assets/img/detail-ghee-honey.jpg" alt="Rosier ghee and honey" loading="lazy"></div></div>
    <div class="reveal" style="--d:.1s">
      {eyebrow('Sustainability')}
      <h2>Good for you. Good for the planet.</h2>
      <p>Our products are minimally processed, made from ingredients that are sustainably sourced and consciously grown. We work closely with our farmer family, because we believe a healthy choice should be healthy for the earth too.</p>
    </div>
  </div>
</section>

<section class="section bg-cream2">
  <div class="container">
    <header class="section-head reveal">{eyebrow('Making of Rosier Gir Cow A2 Ghee', True)}<h2>Slow, the way it should be</h2></header>
    <ol class="made">
      <li class="reveal"><span class="step__num">01</span><h3>Boil the milk</h3><p>Fresh milk from free-grazing Gir cows is brought to a boil.</p></li>
      <li class="reveal" style="--d:.06s"><span class="step__num">02</span><h3>Let it cool</h3><p>It cools naturally to room temperature.</p></li>
      <li class="reveal" style="--d:.12s"><span class="step__num">03</span><h3>Set the curd</h3><p>A natural starter culture sets it into curd overnight.</p></li>
      <li class="reveal" style="--d:.18s"><span class="step__num">04</span><h3>Churn by hand</h3><p>The curd is churned the traditional Bilona way.</p></li>
    </ol>
    <div class="center mt-40 reveal"><a href="product.html" class="btn btn--primary">Shop A2 Ghee <svg><use href="#i-arrow"/></svg></a></div>
  </div>
</section>

<section class="section">
  <div class="container split">
    <div class="split__media reveal"><div class="frame frame--arch"><img src="{HOME['family']}&width=1000" alt="Gaurav with Rosier farmers" loading="lazy"></div></div>
    <div class="reveal" style="--d:.1s">
      {eyebrow('A note from our founder')}
      <h2>Restoring India's traditions in modern life</h2>
      <p>Gaurav has spent over 20 years in the health and fitness industry. Indian culture and timeless values sit at the heart of everything he believes in, and he's deeply drawn to the ancient Indian sciences and the Vedas.</p>
      <p>He believes milk from indigenous Gir desi cows, the kind described in our ancient texts, is better for us than A1 milk from HF and Jersey cows. Rosier is his way of bringing that heritage home to you.</p>
      <p style="font-family:var(--serif);font-size:20px;color:var(--brown-ink);margin-top:22px">— Gaurav, Founder</p>
    </div>
  </div>
</section>

<section style="padding-bottom:clamp(72px,9vw,120px)">
  <div class="container">
    <div class="club-band reveal" style="grid-template-columns:1fr auto">
      <div>{eyebrow('The Rosier promise', light=True)}<h2>Bringing the wisdom and flavors of Old Bharat to today's tables</h2></div>
      <a href="shop.html" class="btn btn--gold">Shop Now <svg><use href="#i-arrow"/></svg></a>
    </div>
  </div>
</section>
'''
