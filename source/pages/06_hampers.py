FILE = 'hampers.html'
TITLE = 'Parampara Diwali Hampers | Rosier Foods'
DESC = 'Rosier Parampara Diwali gift hampers. Traditional and Lifestyle boxes with A2 ghee, honey, trail mix and festive goodies. Bulk and corporate orders welcome.'
ACTIVE = 'hampers'

def hamper(img, name, tag, price, mrp, inside, slug, d=0):
    li = ''.join(f'<li>{x}</li>' for x in inside)
    return f'''<article class="hamper reveal" style="--d:{d}s">
  <div class="hamper__img"><img src="assets/img/{img}" alt="Rosier Parampara {name} hamper" loading="lazy"></div>
  <div class="hamper__body">
    <p class="eyebrow">{tag}</p>
    <h3>Parampara {name}</h3>
    <div class="pdp__price"><b>{inr(price)}</b><s>{inr(mrp)}</s><span class="off">{off(price, mrp)}% OFF</span></div>
    <p class="opt-label" style="margin-top:4px">What's inside</p>
    <ul class="inside">{li}</ul>
    <div class="btn-row"><a class="btn btn--primary" href="{SITE}/pages/hampers">Buy Now</a><a href="#enquiry" class="btn btn--outline">Bulk Order</a></div>
  </div>
</article>'''

BODY = f'''
<section class="hero">
  <div class="hero__glow" aria-hidden="true"></div>
  <div class="container hero__grid">
    <div class="hero__copy">
      {eyebrow('Parampara · Diwali 2026')}
      <h1 class="hero__title reveal" style="--d:.08s">Gift something<br><em>real</em> this Diwali</h1>
      <p class="hero__sub reveal" style="--d:.16s">Pure ghee, raw honey and festive goodies, packed in boxes your family will want to keep. Two hampers. Endless blessings.</p>
      <div class="hero__actions reveal" style="--d:.24s">
        <a href="#hampers" class="btn btn--primary">Shop Hampers <svg><use href="#i-arrow"/></svg></a>
        <a href="#enquiry" class="btn btn--outline">Corporate Gifting</a>
      </div>
      <div class="hero__cta reveal" style="--d:.32s;margin-top:28px"><div class="hero__price" style="border:0;padding:0"><span class="hero__price-label">Starting at</span><span class="hero__price-value">{inr(2499)}</span></div></div>
    </div>
    <div class="hero__visual reveal" style="--d:.15s">
      <div class="arch"><img src="assets/img/gifting-hands.jpg" alt="Rosier Parampara hamper being gifted" width="560" height="640"></div>
      <div class="float-card float-card--a"><span class="float-card__big">2</span><span class="float-card__small">festive<br>hampers</span></div>
    </div>
  </div>
</section>

<section class="section" id="hampers">
  <div class="container">
    <header class="section-head reveal">{eyebrow('The Parampara collection', True)}<h2>Pick your hamper</h2><p class="section-sub">Both come with our A2 ghee, honey, trail mix and a Rosier taash deck.</p></header>
    <div class="hamper-grid">
      {hamper('box-traditional.jpg', 'Traditional', 'Pichwai Gir cow artwork', 2999, 3499, ['Gir Cow A2 Ghee', 'Honey', 'Gond Laddoo', 'Trail Mix', 'Rosier Taash Cards', 'Festive goodies'], 'traditional')}
      {hamper('box-lifestyle.jpg', 'Lifestyle', '“Light Up The Good Within”', 2499, 2899, ['Gir Cow A2 Ghee', 'Honey', 'High Protein Oats', 'Trail Mix', 'Sipper', 'Keychain', '“Desi At Heart” magnet', 'Rosier Taash Cards'], 'lifestyle', .1)}
    </div>
  </div>
</section>

<section class="section bg-cream2">
  <div class="container">
    <header class="section-head reveal">{eyebrow('A closer look', True)}<h2>Every detail, made with love</h2></header>
    <div class="mosaic reveal">
      <figure class="w2 h2"><img src="assets/img/hamper-open-lifestyle.jpg" alt="Open Lifestyle hamper" loading="lazy"></figure>
      <figure><img src="assets/img/detail-lid-art.jpg" alt="Pichwai lid artwork" loading="lazy"></figure>
      <figure><img src="assets/img/detail-ghee-honey.jpg" alt="Ghee and honey inside the hamper" loading="lazy"></figure>
      <figure><img src="assets/img/detail-oats-goodies.jpg" alt="High protein oats and goodies" loading="lazy"></figure>
      <figure><img src="assets/img/detail-trailmix-deck.jpg" alt="Trail mix and taash deck" loading="lazy"></figure>
    </div>
  </div>
</section>

<section class="section" id="enquiry">
  <div class="container split">
    <div class="reveal">
      {eyebrow('Corporate &amp; bulk gifting')}
      <h2>Gifting for your whole team?</h2>
      <p>Tell us how many hampers you need and we'll get back to you with pricing, custom options and dispatch dates.</p>
      <div class="split__media" style="margin-top:28px"><div class="frame"><img src="assets/img/corporate-spread.jpg" alt="Rosier corporate gifting spread" loading="lazy"></div></div>
    </div>
    <form class="form-card reveal" style="--d:.1s" data-demo>
      <h3>Bulk enquiry</h3><p>Share a few details and we'll take it from there.</p>
      <div class="fields">
        <div class="field"><label for="b-name">Your name</label><input id="b-name" required></div>
        <div class="field"><label for="b-co">Company</label><input id="b-co"></div>
        <div class="field"><label for="b-ph">Phone</label><input id="b-ph" type="tel" required></div>
        <div class="field"><label for="b-em">Email</label><input id="b-em" type="email"></div>
        <div class="field"><label for="b-h">Hamper</label><select id="b-h"><option>Parampara Traditional</option><option>Parampara Lifestyle</option><option>Mix of both</option><option>Custom</option></select></div>
        <div class="field"><label for="b-q">Quantity</label><select id="b-q"><option>10–25</option><option>25–50</option><option>50–100</option><option>100+</option></select></div>
        <div class="field field--full"><label for="b-msg">Anything else?</label><textarea id="b-msg" placeholder="Branding, delivery city, date you need them by…"></textarea></div>
      </div>
      <button class="btn btn--primary btn--block" type="submit">Send Enquiry <svg><use href="#i-arrow"/></svg></button>
      <p class="form-ok">Thank you! Our gifting team will reach out soon.</p>
    </form>
  </div>
</section>
'''
