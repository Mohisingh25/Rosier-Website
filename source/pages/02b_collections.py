exec(open(SRC + '/pages/02_shop.py').read().split("seen, order")[0])
CB = {'ghee': PH['ghee_pour'], 'stone-press-oil': PH['oil_range'], 'pickles': img(BY['mango-pickle'][8], 10).split('&width')[0],
      'atta': img(BY['khapli-emmer-wheat-atta-stoneground-high-fiber-for-gut-health'][8], 10).split('&width')[0],
      'healthy-snacking': img(BY['high-protein-oats-assorted-pack'][8], 10).split('&width')[0], 'immunity-booster': img(BY['amlaprash'][8], 10).split('&width')[0],
      'honey': img(BY['wild-flower-honey'][8], 10).split('&width')[0], 'nut-butters': img(BY['nut-butter-dark-chocolate'][8], 10).split('&width')[0]}
PAGES = []
for k, n, ti, short, desc, hs in COLLECTIONS:
    cards = ''.join(pcard(h, 'reveal', (i % 4) * .05) for i, h in enumerate(hs))
    body = f'''
<section><div class="container">
  <div class="col-banner reveal" style="--cb:url('{CB[k]}&width=1800')"><div>
    <nav class="crumbs"><a href="index.html">Home</a><span>/</span><a href="shop.html">Shop</a><span>/</span>{n}</nav>
    <h1>{n}</h1><p>{desc}</p>
    <div class="col-banner__stats"><span>{len(hs)} products</span>{'<span>Lab tested</span>' if any(x in LABMAP for x in hs) else ''}<span>Up to {max(off(BY[x][3], BY[x][4]) for x in hs)}% off</span><span>Delivered across India</span></div>
  </div></div>
</div></section>
<section style="padding:10px 0 clamp(56px,7vw,90px)"><div class="container">
  {tabs(k)}{sortbar(len(hs))}
  <div class="shop-wrap">{filters([BY[x][3] for x in hs])}<div><div class="shop-grid" id="shop-grid">{cards}</div><p class="no-res" hidden>Nothing matches these filters.</p></div></div>
</div></section>
<section style="padding-bottom:clamp(72px,9vw,110px)"><div class="container">
  <div class="lab-cta reveal"><div class="lab-cta__l"><span class="ico ico--lg"><svg><use href="#i-flask"/></svg></span><div><h3>Don't just trust us. Check the lab report.</h3><p>Lab test reports for our products are open for anyone to read.</p></div></div><a href="lab-reports.html" class="btn btn--primary">See Lab Reports <svg><use href="#i-arrow"/></svg></a></div>
</div></section>'''
    PAGES.append((curl(k), f'{n} | Rosier Foods', desc, 'shop', body))
