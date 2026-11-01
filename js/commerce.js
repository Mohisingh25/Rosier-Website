// Rosier Foods — commerce layer: persistent cart + drawer, live search, quick view,
// sticky add-to-cart, frequently bought together, recently viewed, filters, tabs.
(function () {
  var RF = window.RF || { p: [] };
  var $ = function (s, c) { return (c || document).querySelector(s); };
  var $$ = function (s, c) { return Array.prototype.slice.call((c || document).querySelectorAll(s)); };
  var BY = {}; RF.p.forEach(function (p) { BY[p.h] = p; });
  var TIERS = [[2499, 'a free bottle'], [4999, 'a free tumbler'], [7999, 'a free bottle + tumbler']];
  var inr = function (n) { n = Math.round(n * 100) / 100; return '₹' + n.toLocaleString('en-IN', { minimumFractionDigits: n % 1 ? 2 : 0, maximumFractionDigits: 2 }); };
  var esc = function (s) { return String(s).replace(/[&<>"]/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]; }); };
  var store = {
    get: function (k, d) { try { var v = JSON.parse(localStorage.getItem(k)); return v == null ? d : v; } catch (e) { return d; } },
    set: function (k, v) { try { localStorage.setItem(k, JSON.stringify(v)); } catch (e) {} }
  };

  /* ---------------- cart state ---------------- */
  var cart = store.get('rf_cart', null);
  if (!cart) { cart = []; }
  function save() { store.set('rf_cart', cart); render(); }
  function line(h, label, price, mrp) { return cart.filter(function (l) { return l.h === h && l.v === label; })[0]; }
  function add(h, q, label, price, mrp, vid) {
    var p = BY[h]; if (!p) return;
    label = label || p.s; price = price || p.p; mrp = mrp || p.m; vid = vid || p.v;
    var l = line(h, label);
    if (l) { l.q += q; l.vid = l.vid || vid; } else cart.push({ h: h, v: label, p: price, m: mrp, q: q, vid: vid });
    save(); openDrawer(p.n);
  }
  function totals() {
    var sub = 0, mrp = 0, n = 0;
    cart.forEach(function (l) { sub += l.p * l.q; mrp += l.m * l.q; n += l.q; });
    return { sub: Math.round(sub * 100) / 100, mrp: mrp, n: n };
  }

  /* ---------------- drawer ---------------- */
  var dr = document.createElement('aside');
  dr.className = 'cdr'; dr.setAttribute('aria-label', 'Your cart'); dr.setAttribute('aria-hidden', 'true');
  dr.innerHTML = '<div class="cdr__scrim" data-cdr-close></div><div class="cdr__panel" role="dialog" aria-modal="true" aria-label="Cart">' +
    '<header class="cdr__head"><h3>Your Cart <span class="cdr__n"></span></h3><button class="cdr__x" data-cdr-close aria-label="Close cart">×</button></header>' +
    '<div class="cdr__added" hidden></div>' +
    '<div class="cdr__gift"><p class="cdr__giftmsg"></p><div class="gift-bar__track"><div class="gift-bar__fill"></div></div><div class="cdr__marks"><span>₹2,499<br><small>Bottle</small></span><span>₹4,999<br><small>Tumbler</small></span><span>₹7,999<br><small>Both</small></span></div></div>' +
    '<div class="cdr__items"></div>' +
    '<div class="cdr__up"><p class="opt-label">Families also add</p><div class="cdr__upl"></div></div>' +
    '<footer class="cdr__foot"><div class="cdr__club"></div><div class="sum-row"><span>MRP total</span><b class="cdr__mrp"></b></div><div class="sum-row"><span>You save</span><b class="cdr__save" style="color:var(--olive)"></b></div>' +
    '<div class="sum-row sum-row--total"><span>Subtotal</span><b class="cdr__sub"></b></div><p class="tax">Tax included. Shipping calculated at checkout.</p>' +
    '<a href="cart.html" class="btn btn--outline btn--block">View Cart</a><a href="cart.html" class="btn btn--primary btn--block cdr__checkout" style="margin-top:8px">Checkout on rosierfoods.com</a><p class="tax" style="text-align:center;margin-top:8px">Payment and order confirmation happen securely on rosierfoods.com.</p></footer></div>';
  document.body.appendChild(dr);
  function openDrawer(addedName) {
    var a = $('.cdr__added', dr);
    if (addedName) { a.hidden = false; a.innerHTML = '✓ <b>' + esc(addedName) + '</b> added to your cart'; } else a.hidden = true;
    dr.classList.add('open'); dr.setAttribute('aria-hidden', 'false'); document.body.style.overflow = 'hidden';
  }
  function closeDrawer() { dr.classList.remove('open'); dr.setAttribute('aria-hidden', 'true'); document.body.style.overflow = ''; }
  dr.addEventListener('click', function (e) {
    if (e.target.closest('[data-cdr-close]')) return closeDrawer();
    var b = e.target.closest('[data-cq]'); if (b) { var i = +b.dataset.i; cart[i].q += +b.dataset.cq; if (cart[i].q < 1) cart.splice(i, 1); save(); }
    var r = e.target.closest('[data-crm]'); if (r) { cart.splice(+r.dataset.i, 1); save(); }
    var u = e.target.closest('[data-up]'); if (u) add(u.dataset.up, 1);
  });
  document.addEventListener('keydown', function (e) { if (e.key === 'Escape') { closeDrawer(); closeQV(); closeSearch(); } });

  function giftHTML(sub) {
    var next = TIERS.filter(function (t) { return sub < t[0]; })[0];
    return next ? 'Add <b>' + inr(Math.ceil(next[0] - sub)) + '</b> more to get <b>' + next[1] + '</b> 🎁' : 'You’ve unlocked <b>a free bottle + tumbler</b> 🎉';
  }

  function checkoutUrl() {
    var ok = cart.length && cart.every(function (l) { return l.vid || (BY[l.h] && BY[l.h].v); });
    return ok ? 'https://www.rosierfoods.com/cart/' + cart.map(function (l) { return (l.vid || BY[l.h].v) + ':' + l.q; }).join(',') : 'cart.html';
  }
  function render() {
    var t = totals();
    $$('.cdr__checkout, #checkout').forEach(function (a) { a.href = checkoutUrl(); });
    $$('.cart-count').forEach(function (c) { c.textContent = t.n; c.classList.toggle('has', t.n > 0); });
    $('.cdr__n', dr).textContent = t.n ? '(' + t.n + ')' : '';
    $('.cdr__giftmsg', dr).innerHTML = giftHTML(t.sub);
    $('.gift-bar__fill', dr).style.width = Math.min(100, t.sub / 7999 * 100) + '%';
    $$('.cdr__marks span', dr).forEach(function (s, i) { s.classList.toggle('hit', t.sub >= TIERS[i][0]); });
    $('.cdr__items', dr).innerHTML = cart.length ? cart.map(function (l, i) {
      var p = BY[l.h] || {};
      return '<div class="cdr__it"><a href="product-' + l.h + '.html"><img src="' + p.i + '&width=200" alt=""></a><div><a href="product-' + l.h + '.html" class="cdr__nm">' + esc(p.n) + '</a><small>' + esc(l.v) + '</small>' +
        '<div class="cdr__row"><div class="qty qty--sm"><button data-cq="-1" data-i="' + i + '" aria-label="Decrease">−</button><span>' + l.q + '</span><button data-cq="1" data-i="' + i + '" aria-label="Increase">+</button></div><b>' + inr(l.p * l.q) + '</b></div>' +
        '<button class="cdr__rm" data-crm data-i="' + i + '">Remove</button></div></div>';
    }).join('') : '<div class="cdr__empty"><p>Your cart is empty.</p><a href="shop.html" class="btn btn--primary">Start Shopping</a></div>';
    var inCart = cart.map(function (l) { return l.h; });
    var ups = (RF.best || []).filter(function (h) { return inCart.indexOf(h) < 0; }).slice(0, 3);
    $('.cdr__up', dr).style.display = ups.length ? '' : 'none';
    $('.cdr__upl', dr).innerHTML = ups.map(function (h) { var p = BY[h]; return '<div class="cdr__ui"><img src="' + p.i + '&width=160" alt=""><div><span>' + esc(p.n) + '</span><b>' + inr(p.p) + '</b></div><button data-up="' + h + '" aria-label="Add ' + esc(p.n) + '">+</button></div>'; }).join('');
    $('.cdr__mrp', dr).textContent = inr(t.mrp);
    $('.cdr__save', dr).textContent = '− ' + inr(Math.round((t.mrp - t.sub) * 100) / 100);
    $('.cdr__sub', dr).textContent = inr(t.sub);
    $('.cdr__club', dr).innerHTML = t.sub ? '<span class="earnback__coin" aria-hidden="true">₹</span><span>Benefit Club members save about <b>' + inr(Math.round(t.sub * .15)) + '</b> more on this cart. <a href="membership.html">Join from ₹299</a></span>' : '';
    $('.cdr__foot', dr).style.display = cart.length ? '' : 'none';
    $('.cdr__gift', dr).style.display = cart.length ? '' : 'none';
    renderCartPage(t);
  }

  /* cart page */
  function renderCartPage(t) {
    var box = $('#cart-items'); if (!box) return;
    $('.empty-cart').style.display = cart.length ? 'none' : 'block';
    $('.cart-grid').style.display = cart.length ? '' : 'none';
    box.innerHTML = cart.map(function (l, i) {
      var p = BY[l.h] || {};
      return '<div class="citem"><div class="citem__img"><img src="' + p.i + '&width=300" alt=""></div><div><h3><a href="product-' + l.h + '.html">' + esc(p.n) + '</a></h3><small>' + esc(l.v) + ' · <s>' + inr(l.m) + '</s> ' + inr(l.p) + ' each</small>' +
        '<div class="qty qty--sm" style="margin-top:12px"><button data-cq="-1" data-i="' + i + '">−</button><span>' + l.q + '</span><button data-cq="1" data-i="' + i + '">+</button></div></div>' +
        '<div class="citem__right"><b>' + inr(l.p * l.q) + '</b><button data-crm data-i="' + i + '">Remove</button></div></div>';
    }).join('');
    $('#gift-msg').innerHTML = giftHTML(t.sub);
    $('.gift-bar__fill', $('.gift-bar')).style.width = Math.min(100, t.sub / 7999 * 100) + '%';
    $('#s-mrp').textContent = inr(t.mrp);
    $('#s-save').textContent = '− ' + inr(Math.round((t.mrp - t.sub) * 100) / 100);
    $('#s-total').textContent = inr(t.sub);
    $('#s-club').textContent = inr(Math.round(t.sub * .15));
  }
  var cb = $('#cart-items');
  if (cb) cb.addEventListener('click', function (e) {
    var b = e.target.closest('[data-cq]'); if (b) { var i = +b.dataset.i; cart[i].q += +b.dataset.cq; if (cart[i].q < 1) cart.splice(i, 1); save(); }
    var r = e.target.closest('[data-crm]'); if (r) { cart.splice(+r.dataset.i, 1); save(); }
  });

  /* add-to-cart buttons */
  document.addEventListener('click', function (e) {
    var b = e.target.closest('[data-h]');
    if (b && b.matches('button')) {
      e.preventDefault();
      if (b.id === 'pdp-add' || b.classList.contains('satc__btn') || b.hasAttribute('data-buy')) {
        var v = $('.variant.on'), q = parseInt(($('#pdp-qty') || {}).value, 10) || 1;
        add(b.dataset.h, q, v ? v.textContent : null, v ? +v.dataset.price : null, v ? +v.dataset.mrp : null, v ? +v.dataset.vid : null);
      } else add(b.dataset.h, 1);
      b.classList.add('pop'); setTimeout(function () { b.classList.remove('pop'); }, 500);
      if (b.hasAttribute('data-buy')) { closeDrawer(); location.href = 'cart.html'; }
    }
    var o = e.target.closest('[data-open-cart]'); if (o) { e.preventDefault(); openDrawer(); }
  });

  /* ---------------- live search ---------------- */
  var sp = document.createElement('div'); sp.className = 'srch'; sp.hidden = true; sp.setAttribute('role', 'listbox');
  document.body.appendChild(sp);
  var sInput = null;
  function closeSearch() { sp.hidden = true; }
  function norm(s) { return s.toLowerCase().replace(/[^a-z0-9 ]/g, ' '); }
  function searchFor(q) {
    q = norm(q).trim();
    var res = q ? RF.p.filter(function (p) { var t = norm(p.n + ' ' + p.cn + ' ' + p.s + ' ' + (p.k || '')); return q.split(/\s+/).every(function (w) { return t.indexOf(w) > -1; }); }) : (RF.best || []).map(function (h) { return BY[h]; });
    return res.slice(0, 7);
  }
  function showSearch(inp) {
    sInput = inp; var r = inp.getBoundingClientRect();
    sp.style.top = (r.bottom + window.scrollY + 8) + 'px';
    sp.style.left = Math.max(10, Math.min(r.left, innerWidth - 390)) + 'px';
    var q = inp.value, res = searchFor(q);
    sp.innerHTML = '<p class="srch__h">' + (q ? (res.length ? 'Products' : 'No match for “' + esc(q) + '”. Try ghee, oil or atta.') : 'Popular right now') + '</p>' +
      res.map(function (p) { return '<a class="srch__r" href="product-' + p.h + '.html"><img src="' + p.i + '&width=120" alt=""><span><b>' + esc(p.n) + '</b><small>' + esc(p.cn) + ' · ' + esc(p.s) + '</small></span><em>' + inr(p.p) + '</em></a>'; }).join('') +
      (q && res.length ? '<a class="srch__all" href="shop.html?q=' + encodeURIComponent(q) + '">See all results →</a>' : '') +
      (q && !res.length ? '<p class="srch__h">Try: <a href="shop.html?q=ghee">ghee</a> · <a href="shop.html?q=atta">atta</a> · <a href="shop.html?q=honey">honey</a> · <a href="shop.html?q=oil">oil</a></p>' : '');
    sp.hidden = false;
  }
  $$('input[type=search]').forEach(function (inp) {
    if (inp.id === 'lab-q') return;
    inp.setAttribute('autocomplete', 'off');
    inp.addEventListener('focus', function () { showSearch(inp); });
    inp.addEventListener('input', function () { showSearch(inp); });
    inp.setAttribute('aria-autocomplete', 'list');
  });
  document.addEventListener('click', function (e) { if (!e.target.closest('.srch') && !e.target.closest('input[type=search]')) closeSearch(); });
  addEventListener('resize', closeSearch);

  /* ---------------- quick view ---------------- */
  var qv = document.createElement('div'); qv.className = 'qv'; qv.setAttribute('aria-hidden', 'true');
  document.body.appendChild(qv);
  function closeQV() { qv.classList.remove('open'); qv.setAttribute('aria-hidden', 'true'); }
  document.addEventListener('click', function (e) {
    var b = e.target.closest('[data-qv]'); if (!b) return;
    e.preventDefault(); var p = BY[b.dataset.qv]; if (!p) return;
    var o = Math.round((1 - p.p / p.m) * 100);
    qv.innerHTML = '<div class="qv__scrim" data-qv-close></div><div class="qv__box" role="dialog" aria-modal="true" aria-label="' + esc(p.n) + '"><button class="cdr__x qv__x" data-qv-close aria-label="Close">×</button>' +
      '<div class="qv__img"><img src="' + p.i + '&width=900" alt="' + esc(p.n) + '"><img class="qv__img2" src="' + p.i2 + '&width=900" alt=""></div>' +
      '<div class="qv__info"><p class="eyebrow">' + esc(p.cn) + '</p><h3>' + esc(p.n) + '</h3>' + (p.r ? '<span class="stars"><svg><use href="#i-star"/></svg><b>' + p.r.toFixed(1) + '</b></span>' : '') +
      '<div class="pdp__price"><b>' + inr(p.p) + '</b>' + (o > 0 ? '<s>' + inr(p.m) + '</s><span class="off">' + o + '% OFF</span>' : '') + '</div><p class="tax">' + esc(p.s) + ' · Tax included</p>' +
      (p.lab ? '<a class="qv__lab" href="' + p.lab + '" target="_blank" rel="noopener"><svg><use href="#i-flask"/></svg>View lab report</a>' : '') +
      '<button class="btn btn--primary btn--block" data-h="' + p.h + '">Add to Cart</button><a class="btn btn--outline btn--block" href="product-' + p.h + '.html" style="margin-top:8px">View full details</a></div></div>';
    qv.classList.add('open'); qv.setAttribute('aria-hidden', 'false');
  });
  qv.addEventListener('click', function (e) { if (e.target.closest('[data-qv-close]') || e.target.closest('[data-h]')) closeQV(); });

  /* ---------------- PDP: sticky add-to-cart, FBT, recently viewed ---------------- */
  var pAdd = $('#pdp-add');
  if (pAdd) {
    var h = pAdd.dataset.h, p = BY[h];
    var bar = document.createElement('div'); bar.className = 'satc';
    bar.innerHTML = '<div class="container satc__in"><img src="' + p.i + '&width=120" alt=""><div class="satc__t"><b>' + esc(p.n) + '</b><span class="satc__p">' + inr(p.p) + '</span></div><button class="btn btn--primary satc__btn" data-h="' + h + '">Add to Cart</button></div>';
    document.body.appendChild(bar);
    if ('IntersectionObserver' in window) new IntersectionObserver(function (es) { bar.classList.toggle('show', !es[0].isIntersecting && es[0].boundingClientRect.top < 0); }).observe(pAdd);
    $$('.variant').forEach(function (v) { v.addEventListener('click', function () { $('.satc__p', bar).textContent = inr(+v.dataset.price); }); });
    var rec = store.get('rf_recent', []).filter(function (x) { return x !== h && BY[x]; });
    var rv = $('#recent');
    if (rv && rec.length) {
      rv.hidden = false;
      $('.recent__row', rv).innerHTML = rec.slice(0, 6).map(function (x) { var q = BY[x]; return '<a class="mini" href="product-' + x + '.html"><img src="' + q.i + '&width=300" alt=""><span>' + esc(q.n) + '</span><b>' + inr(q.p) + '</b></a>'; }).join('');
    }
    store.set('rf_recent', [h].concat(rec).slice(0, 10));
  }
  var fbt = $('.fbt');
  if (fbt) {
    var upd = function () {
      var sum = 0, n = 0;
      $$('.fbt input', fbt).forEach(function (c) { c.closest('.fbt__i').classList.toggle('off', !c.checked); if (c.checked) { sum += BY[c.value].p; n++; } });
      $('.fbt__total', fbt).textContent = inr(sum); $('.fbt__n', fbt).textContent = n;
    };
    fbt.addEventListener('change', upd); upd();
    $('.fbt__add', fbt).addEventListener('click', function () {
      $$('.fbt input:checked', fbt).forEach(function (c) { var l = line(c.value, BY[c.value].s); if (l) l.q++; else cart.push({ h: c.value, v: BY[c.value].s, p: BY[c.value].p, m: BY[c.value].m, q: 1 }); });
      save(); openDrawer('Your bundle was');
    });
  }

  /* ---------------- collection filters ---------------- */
  var grid = $('#shop-grid'), fl = $('.filters');
  if (grid && fl) {
    var range = $('#f-price', fl), out = $('#f-price-v', fl);
    var applyF = function () {
      var max = +range.value, top = $('#f-top', fl).checked, deal = $('#f-deal', fl).checked;
      var packs = $$('.f-pack:checked', fl).map(function (c) { return c.value; }), types = $$('.f-type:checked', fl).map(function (c) { return c.value; }), n = 0;
      var q = (new URLSearchParams(location.search).get('q') || '').toLowerCase().trim();
      out.textContent = inr(max);
      $$('.pcard', grid).forEach(function (c) {
        var ok = +c.dataset.price <= max && (!top || +c.dataset.rating >= 4.8) && (!deal || +c.dataset.off >= 20) && (!packs.length || packs.indexOf(c.dataset.pack) > -1) && (!types.length || types.indexOf(c.dataset.type) > -1);
        if (q) { var pr = RF.p[+c.dataset.i] || {}; var hay = norm(c.textContent + ' ' + (pr.k || '') + ' ' + (pr.cn || '')); ok = ok && q.split(/\s+/).every(function (w) { return hay.indexOf(norm(w).trim()) > -1; }); }
        c.classList.toggle('hide', !ok); if (ok) n++;
      });
      var cnt = $('#shop-count'); if (cnt) cnt.textContent = n + (n === 1 ? ' product' : ' products');
      var none = $('.no-res'); if (none) none.hidden = n > 0;
    };
    fl.addEventListener('input', applyF);
    var rs = $('#f-reset', fl); if (rs) rs.addEventListener('click', function () { range.value = range.max; $$('input[type=checkbox]', fl).forEach(function (c) { c.checked = false; }); if (location.search) { history.replaceState(null, '', location.pathname); var t = $('#shop-title'); if (t) t.textContent = t.dataset.t || 'All products'; } applyF(); });
    var ft = $('.f-toggle'); if (ft) ft.addEventListener('click', function () { fl.classList.toggle('open'); });
    var q0 = new URLSearchParams(location.search).get('q'); if (q0) { var t = $('#shop-title'); if (t) t.textContent = 'Results for “' + q0 + '”'; $$('input[name=q]').forEach(function (i) { i.value = q0; }); var pr = $('.shop-promo'); if (pr) pr.style.display = 'none'; }
    applyF();
  }

  /* ---------------- tabs (homepage product rows, need tiles) ---------------- */
  $$('[data-tabs]').forEach(function (w) {
    var btns = $$('[data-tab]', w), panes = $$('[data-pane]', w);
    btns.forEach(function (b) {
      b.addEventListener('click', function () {
        btns.forEach(function (x) { x.classList.toggle('on', x === b); x.setAttribute('aria-selected', x === b); });
        panes.forEach(function (p) { var on = p.dataset.pane === b.dataset.tab; p.hidden = !on; if (on) { p.classList.remove('fadein'); void p.offsetWidth; p.classList.add('fadein'); } });
      });
    });
  });

  /* ---------------- lab report picker ---------------- */
  var lp = $('#lab-pick');
  if (lp) { var go = $('#lab-go'); lp.addEventListener('change', function () { go.href = lp.value; go.classList.toggle('disabled', !lp.value); }); }

  /* ---------------- PDP: variant id, PIN checker ---------------- */
  var pin = $('#pin-form');
  if (pin) pin.addEventListener('submit', function (e) {
    e.preventDefault(); var v = $('#pin', pin).value.trim(), m = $('.pin__msg', pin);
    if (!/^[1-9][0-9]{5}$/.test(v)) { m.className = 'pin__msg err'; m.textContent = 'Please enter a valid 6-digit PIN code.'; return; }
    m.className = 'pin__msg'; m.textContent = 'We ship across India; delivery is usually 3–5 days. Exact serviceability and shipping charges for ' + v + ' are confirmed at checkout.';
  });

  /* ---------------- Know Your Food selector ---------------- */
  var ks = $('#kyf-sel'), kc = $('#kyf-card');
  if (ks && kc && window.KYF) {
    var draw = function () {
      var d = KYF[ks.value]; if (!d) return;
      var tbd = '<span class="tbd">To be added by Rosier</span>';
      kc.innerHTML = '<div class="kyf__head"><img src="' + d.i + '" alt=""><div><h3 style="font-size:24px">' + esc(d.n) + '</h3><p style="color:var(--muted)">' + esc(d.s) + '</p><a class="link-arrow" href="' + d.url + '">View product</a></div></div>' +
        '<dl><dt>What it is</dt><dd>' + esc(d.about) + '</dd>' +
        '<dt>Ingredients</dt><dd>' + (d.ing ? esc(d.ing) : 'Printed on the pack. ' + tbd) + '</dd>' +
        (d.store ? '<dt>Storage</dt><dd>' + esc(d.store) + '</dd>' : '') +
        '<dt>Lab report</dt><dd>' + (d.lab ? '<a href="' + d.lab + '" target="_blank" rel="noopener" style="text-decoration:underline">Open the lab report</a>' : 'Not yet published for this product.') + '</dd>' +
        '<dt>Testing laboratory &amp; date</dt><dd>' + (d.lab ? 'Shown inside the report. ' + tbd : '—') + '</dd>' +
        '<dt>Made by</dt><dd>Rosier Foods Pvt. Ltd. or a licensed partner unit. <a href="#units" style="text-decoration:underline">Match your batch letter</a></dd>' +
        '<dt>FSSAI licence</dt><dd>Listed for each unit in the table below.</dd>' +
        '<dt>Batch traceability</dt><dd>Batch-level journey tracking needs Rosier’s batch system to be connected. ' + tbd + '</dd></dl>';
    };
    ks.addEventListener('change', draw); draw();
  }

  render();
})();
