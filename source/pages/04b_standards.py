FILE = 'standards.html'
TITLE = 'Know Your Food. Know Its Journey. – Quality & Transparency | Rosier Foods'
DESC = 'Where Rosier products are made (FSSAI-licensed units), how they are made, their lab reports, and our delivery and return terms. Evidence for every claim.'
ACTIVE = 'standards'

CLAIMS = [
    (PH['bilona_pot'], 'Ghee made from curd, the Bilona way', 'Our Gir Cow A2 Ghee starts as curd, not milk or malai, and is slow-churned by the Bilona method.', 'product-a2-desi-cow-ghee-hand-churned-from-curd.html', 'See the A2 ghee page'),
    (PH['tested'], 'Lab reports you can read', 'We publish lab test reports for 32 products, from ghee and oils to atta, oats, nut butters and pickles.', 'lab-reports.html', 'Open the lab reports'),
    (PH['oil_process'], 'Stone pressed oils', 'Our oils are stone cold pressed and extracted without chemicals or solvents, as described on each oil.', curl('stone-press-oil'), 'See the oils'),
    (img(BY['khapli-emmer-wheat-atta-stoneground-high-fiber-for-gut-health'][8], 9).split('&width')[0], 'Stone-ground atta', 'Khapli, multigrain, ragi, jowar and sattu are stone-ground in the traditional chakki method.', curl('atta'), 'See the atta range'),
]
claims = ''.join(f'<div class="claim reveal" style="--d:{i*.06}s"><img src="{im}&width=300" alt="" loading="lazy"><div><h3>{t}</h3><p>{d}</p><a class="ev" href="{u}">Evidence: {lbl} →</a></div></div>' for i, (im, t, d, u, lbl) in enumerate(CLAIMS))

import json as _j
_kd = {h: dict(n=BY[h][1], s=BY[h][2], i=img(BY[h][7], 300), lab=LABMAP.get(h, ''), about=INFO[info_key(h)]['about'],
              ing=INFO[info_key(h)].get('ing', ''), store=INFO[info_key(h)].get('store', ''), url=purl(h)) for h in [p[0] for p in PRODUCTS]}
_opts = ''.join(f'<option value="{h}">{BY[h][1]} ({BY[h][2]})</option>' for h in sorted(_kd, key=lambda x: BY[x][1]))
KYF = f'''<section class="section" id="product">
  <div class="container">
    <header class="section-head reveal">{eyebrow('Choose a product', True)}<h2>Everything we can tell you about it</h2></header>
    <div class="kyf">
      <div class="kyf__pick"><label for="kyf-sel" class="opt-label" style="margin:0">Product</label><select id="kyf-sel">{_opts}</select>
        <p style="font-size:13px;color:var(--muted);margin-top:12px">Your batch number is printed on the pack. Its first letter tells you the manufacturing unit (table below).</p></div>
      <div class="kyf__card" id="kyf-card" aria-live="polite"></div>
    </div>
  </div>
</section>
<script>window.KYF={_j.dumps(_kd, ensure_ascii=False)};</script>'''

rows = ''.join(f'<tr><td>{n}</td><td>{c}</td><td>{a}</td><td>{l}</td></tr>' for n, c, a, l in MANUFACTURERS)

BODY = f'''
<section class="photo-hero" style="--ph:url('{PH['unit']}&width=2200')">
  <div class="container">
    <nav class="crumbs reveal" aria-label="Breadcrumb"><a href="index.html">Home</a><span aria-hidden="true">/</span>Know Your Food</nav>
    <h1 class="reveal">Know Your Food. <em>Know Its Journey.</em></h1>
    <p class="reveal" style="--d:.1s">Where our food is made, how it's made, how it's tested, and what happens if something goes wrong. All in one place.</p>
  </div>
</section>

{KYF}
<section class="section">
  <div class="container">
    <header class="section-head reveal">{eyebrow('How it is made', True)}<h2>What we say, and where to check it</h2></header>
    <div class="std-claims">{claims}</div>
  </div>
</section>

<section class="section bg-cream2" id="units">
  <div class="container">
    <header class="section-head reveal">{eyebrow('Where it is made', True)}<h2>Six FSSAI-licensed units</h2><p class="section-sub">Every Rosier product is made and packed in one of these units. You can trace yours from the batch number on the pack.</p></header>
    <div class="units-wrap reveal"><table class="units"><thead><tr><th>Manufacturer / plant</th><th>Batch code</th><th>Address</th><th>FSSAI licence no.</th></tr></thead><tbody>{rows}</tbody></table></div>
    <div class="batch reveal"><code>GS…</code><span>Look at the first two letters of the batch number printed on your pack. The <b>first letter</b> is the manufacturing unit, the <b>second</b> is the packing unit. You can also scan the QR code on the pack.</span></div>
  </div>
</section>

<section class="section" id="lab">
  <div class="container split">
    <div class="split__media reveal"><div class="frame"><img src="{PH['tested']}&width=1100" alt="Rosier A2 ghee with its lab report" loading="lazy"></div></div>
    <div class="reveal" style="--d:.1s">
      {eyebrow('How it is tested')}
      <h2>32 products, reports open to all</h2>
      <p>We publish the lab test report for each of these products. Open any report to see exactly what was tested and the results.</p><p class="owner-note"><b>Content pending from Rosier:</b> testing laboratory and report date for each report, so we can list them here.</p>
      <a href="lab-reports.html" class="btn btn--primary">Browse all lab reports</a>
    </div>
  </div>
</section>

<section class="section bg-cream2" id="returns">
  <div class="container">
    <header class="section-head reveal">{eyebrow('Buying from us', True)}<h2>Delivery, returns &amp; cancellations</h2><p class="section-sub">Our terms, in plain words. No surprises after you pay.</p></header>
    <div class="pol">
      <div class="reveal"><h3>Delivery</h3><p>{POLICY['delivery']} Shipping charges, if any, are shown at checkout before you pay.</p></div>
      <div class="reveal" style="--d:.06s"><h3>Returns &amp; exchanges</h3><p>{POLICY['returns']} {POLICY['sale']}</p></div>
      <div class="reveal" style="--d:.12s"><h3>Cancellation</h3><p>{POLICY['cancel']} {POLICY['unboxing']}</p></div>
    </div>
    <p class="center mt-40 reveal" style="color:var(--muted)">Full terms: <a href="{SITE}/policies/shipping-policy" style="color:var(--brown);text-decoration:underline">Shipping Policy</a> · <a href="{SITE}/policies/refund-policy" style="color:var(--brown);text-decoration:underline">Refund Policy</a> · Questions? <a href="mailto:{CONTACT_EMAIL}" style="color:var(--brown);text-decoration:underline">{CONTACT_EMAIL}</a></p>
  </div>
</section>
'''
