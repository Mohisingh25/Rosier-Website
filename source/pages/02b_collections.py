exec(open(SRC + '/pages/02_shop.py').read().split("seen, order")[0])
PAGES = []
for k, n, ti, short, desc, hs in COLLECTIONS:
    cards = ''.join(pcard(h, 'reveal', (i % 4) * .05) for i, h in enumerate(hs))
    body = f'''
<section class="page-hero"><div class="container col-hero">
  <div class="col-hero__img reveal"><img src="{img(ti, 300)}" alt="{n}"></div>
  <div><nav class="crumbs reveal"><a href="index.html">Home</a><span>/</span><a href="shop.html">Shop</a><span>/</span>{n}</nav>
  <h1 class="reveal" style="--d:.06s">{n}</h1><p class="lead reveal" style="--d:.12s">{desc}</p></div>
</div></section>
<section style="padding:10px 0 clamp(56px,7vw,90px)"><div class="container">
  {tabs(k)}{sortbar(len(hs))}
  <div class="shop-wrap">{filters([BY[x][3] for x in hs])}<div><div class="shop-grid" id="shop-grid">{cards}</div><p class="no-res" hidden>Nothing matches these filters.</p></div></div>
</div></section>
<section style="padding-bottom:clamp(72px,9vw,110px)"><div class="container">
  <div class="lab-cta reveal"><div class="lab-cta__l"><span class="ico ico--lg"><svg><use href="#i-flask"/></svg></span><div><h3>Don't just trust us. Check the lab report.</h3><p>Lab test reports for our products are open for anyone to read.</p></div></div><a href="lab-reports.html" class="btn btn--primary">See Lab Reports <svg><use href="#i-arrow"/></svg></a></div>
</div></section>'''
    PAGES.append((curl(k), f'{n} | Rosier Foods', desc, 'shop', body))
