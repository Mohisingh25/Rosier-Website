FILE = 'lab-reports.html'
TITLE = 'Lab Test Reports | Rosier Foods'
DESC = 'Lab test reports for all Rosier Foods products. Check the report for your ghee, oils, atta, honey, pickles and more.'
ACTIVE = 'lab'

total = sum(len(v) for _, v in LAB)
LABURL='https://cdn.shopify.com/s/files/1/0653/2605/5654/files/'
chips = '<button class="chip on" data-lab="all">All</button>' + ''.join(f'<button class="chip" data-lab="{c}">{LABCAT[c]}</button>' for c, _ in LAB)
cards = ''
k = 0
for c, items in LAB:
    for name, f in items:
        cards += f'''<article class="lab-card reveal" style="--d:{(k % 4) * .04:.2f}s" data-cat="{c}" data-name="{name.lower()}">
  <div class="lab-card__top"><span class="ico"><svg><use href="#i-file"/></svg></span><div><small>{LABCAT[c]}</small><h3>{name}</h3></div></div>
  <a href="{LABURL}{f}" target="_blank" rel="noopener" class="btn btn--outline btn--block">View Lab Report</a></article>'''
        k += 1

BODY = f'''
<section class="page-hero">
  <div class="container">
    <nav class="crumbs reveal"><a href="index.html">Home</a><span>/</span>Lab Reports</nav>
    <h1 class="reveal" style="--d:.06s">Lab reports for <em>all</em> our products</h1>
    <p class="lead reveal" style="--d:.12s">We say pure. We'd rather you see it for yourself. Pick a product, open its report, and decide.</p>
  </div>
</section>

<section style="padding:20px 0 clamp(72px,9vw,120px)">
  <div class="container">
    <div class="lab-intro">
      <h2 class="sr-only">Why we publish lab reports</h2><div class="value reveal"><span class="ico"><svg><use href="#i-flask"/></svg></span><h3>{total} products tested</h3><p>Every product listed here has its lab report published, open for anyone to read.</p></div>
      <div class="value reveal" style="--d:.06s"><span class="ico"><svg><use href="#i-shield"/></svg></span><h3>Nothing hidden</h3><p>No refined oils. No additives. Read the report and see exactly what's in your food.</p></div>
      <div class="value reveal" style="--d:.12s"><span class="ico"><svg><use href="#i-headset"/></svg></span><h3>Got a question?</h3><p>Not sure how to read a report? <a href="contact.html" style="color:var(--brown);text-decoration:underline">Ask our team</a> and we'll walk you through it.</p></div>
    </div>

    <div class="toolbar">
      <div class="chips">{chips}</div>
      <label class="lab-search"><svg><use href="#i-search"/></svg><input id="lab-q" type="search" placeholder="Search a product, e.g. mustard oil"></label>
    </div>
    <div class="lab-grid" id="lab-grid">{cards}</div>
    <p class="lab-empty">No product matches that search. Try “ghee”, “oil” or “oats”.</p>
  </div>
</section>
'''
