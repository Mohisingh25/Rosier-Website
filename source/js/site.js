// Rosier Foods — site interactions (quiet, lightweight, no libraries)
(function () {
  var $ = function (s, c) { return (c || document).querySelector(s); };
  var $$ = function (s, c) { return Array.prototype.slice.call((c || document).querySelectorAll(s)); };
  var inr = function (n) { return '₹' + n.toLocaleString('en-IN', { minimumFractionDigits: n % 1 ? 2 : 0, maximumFractionDigits: 2 }); };

  /* Reveal on scroll */
  var items = $$('.reveal');
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (es) {
      es.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); } });
    }, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });
    items.forEach(function (el) { io.observe(el); });
  } else items.forEach(function (el) { el.classList.add('in'); });

  /* Header shadow + sticky mobile CTA */
  var header = $('.header'), sticky = $('.sticky-cta'), plans = $('#plans');
  function onScroll() {
    var y = window.scrollY;
    if (header) header.classList.toggle('is-scrolled', y > 10);
    if (sticky) {
      var hide = false;
      if (plans) { var r = plans.getBoundingClientRect(); hide = r.top < innerHeight && r.bottom > 0; }
      sticky.classList.toggle('show', y > 600 && !hide);
    }
  }
  addEventListener('scroll', onScroll, { passive: true }); onScroll();

  /* Mobile drawer */
  var drawer = $('.drawer');
  $$('[data-drawer]').forEach(function (b) {
    b.addEventListener('click', function () {
      var open = drawer.classList.toggle('open'); document.body.style.overflow = open ? 'hidden' : '';
      $$('[aria-controls=drawer]').forEach(function (x) { x.setAttribute('aria-expanded', open); });
      if (open) setTimeout(function () { var t = b.hasAttribute('data-focus-search') ? $('#q-drawer') : $('.drawer__panel a'); if (t) t.focus(); }, 300);
    });
  });

  /* Accordions (one open per group) */
  $$('.accordion').forEach(function (acc) {
    var qs = $$('.acc-q', acc);
    qs.forEach(function (btn) {
      btn.addEventListener('click', function () {
        var item = btn.parentElement, open = item.classList.contains('open');
        $$('.acc-item.open', acc).forEach(function (o) { o.classList.remove('open'); $('.acc-q', o).setAttribute('aria-expanded', 'false'); });
        if (!open) { item.classList.add('open'); btn.setAttribute('aria-expanded', 'true'); }
      });
    });
    if (qs[0] && !acc.hasAttribute('data-closed')) qs[0].click();
  });

  /* Carousels */
  $$('[data-carousel]').forEach(function (wrap) {
    var track = $('.carousel__track', wrap), id = wrap.getAttribute('data-carousel');
    $$('[data-car="' + id + '"]').forEach(function (btn) {
      btn.addEventListener('click', function () {
        var dir = btn.classList.contains('car-btn--prev') ? -1 : 1;
        track.scrollBy({ left: dir * track.clientWidth * 0.8, behavior: 'smooth' });
      });
    });
  });

  /* Shop: filter + sort */
  var grid = $('#shop-grid');
  if (grid) {
    var cards = $$('.pcard', grid), promo = $('.shop-promo', grid), shown = $('#shop-count');
    var cat = 'all';
    var params = new URLSearchParams(location.search); if (params.get('c')) cat = params.get('c');
    function apply() {
      var n = 0;
      cards.forEach(function (c) { var ok = cat === 'all' || c.dataset.cat === cat; c.classList.toggle('hide', !ok); if (ok) n++; });
      if (promo) promo.classList.toggle('hide', cat !== 'all');
      $$('.chip').forEach(function (ch) { ch.classList.toggle('on', ch.dataset.cat === cat); });
      if (shown) shown.textContent = n + (n === 1 ? ' product' : ' products');
      var t = $('#shop-title'), on = $('.chip.on'); if (t && on) t.textContent = cat === 'all' ? 'All Products' : on.textContent;
    }
    $$('.chip').forEach(function (ch) { ch.addEventListener('click', function () { cat = ch.dataset.cat; apply(); history.replaceState(null, '', cat === 'all' ? 'shop.html' : 'shop.html?c=' + cat); }); });
    var sel = $('#sort');
    if (sel) sel.addEventListener('change', function () {
      var v = sel.value, arr = cards.slice();
      if (v !== 'featured') arr.sort(function (a, b) {
        var pa = +a.dataset.price, pb = +b.dataset.price, ra = +a.dataset.rating, rb = +b.dataset.rating;
        return v === 'low' ? pa - pb : v === 'high' ? pb - pa : v === 'rating' ? rb - ra : (+b.dataset.off) - (+a.dataset.off);
      });
      else arr.sort(function (a, b) { return a.dataset.i - b.dataset.i; });
      arr.forEach(function (c) { grid.appendChild(c); });
      if (promo) grid.insertBefore(promo, grid.children[4] || null);
    });
    apply();
  }

  /* PDP: gallery, variants, qty */
  $$('.gallery__thumbs button').forEach(function (b) {
    b.addEventListener('click', function () {
      var main = $('.gallery__main img');
      $$('.gallery__thumbs button').forEach(function (x) { x.classList.remove('on'); });
      b.classList.add('on'); main.style.opacity = 0;
      setTimeout(function () { var i = $('img', b); main.src = i.dataset.full || i.src; main.style.opacity = 1; }, 200);
    });
  });
  $$('.variant').forEach(function (v) {
    v.addEventListener('click', function () {
      $$('.variant').forEach(function (x) { x.classList.remove('on'); x.setAttribute('aria-pressed', 'false'); }); v.classList.add('on'); v.setAttribute('aria-pressed', 'true');
      var p = +v.dataset.price, m = +v.dataset.mrp;
      $('#pdp-price').textContent = inr(p); $('#pdp-mrp').textContent = inr(m);
      $('#pdp-off').textContent = Math.round((1 - p / m) * 100) + '% OFF';
    });
  });
  $$('.qty').forEach(function (q) {
    var input = $('input', q); if (!input) return;
    $$('button', q).forEach(function (b) {
      b.addEventListener('click', function () {
        var n = (parseInt(input.value, 10) || 1) + (b.dataset.d === '+' ? 1 : -1);
        input.value = Math.max(1, Math.min(20, n));
        input.dispatchEvent(new Event('change', { bubbles: true }));
      });
    });
  });

  /* Lab reports search + tabs */
  var labGrid = $('#lab-grid');
  if (labGrid) {
    var lc = $$('.lab-card', labGrid), ls = $('#lab-q'), lcat = 'all', empty = $('.lab-empty');
    function labApply() {
      var q = (ls.value || '').toLowerCase().trim(), n = 0;
      lc.forEach(function (c) { var ok = (lcat === 'all' || c.dataset.cat === lcat) && c.dataset.name.indexOf(q) > -1; c.classList.toggle('hide', !ok); if (ok) n++; });
      empty.style.display = n ? 'none' : 'block';
    }
    ls.addEventListener('input', labApply);
    $$('.chip[data-lab]').forEach(function (ch) { ch.addEventListener('click', function () { lcat = ch.dataset.lab; $$('.chip[data-lab]').forEach(function (x) { x.classList.toggle('on', x === ch); }); labApply(); }); });
  }

  /* Forms (demo) */
  $$('form[data-demo]').forEach(function (f) {
    f.addEventListener('submit', function (e) {
      e.preventDefault(); var ok = $('.form-ok', f), er = $('.form-err', f);
      if (!f.checkValidity()) { var bad = f.querySelector(':invalid'); if (er) { er.textContent = bad && bad.type === 'checkbox' ? 'Please tick the consent box to continue.' : 'Please fill in the highlighted field correctly.'; er.classList.add('show'); } if (bad) bad.focus(); return; }
      if (er) er.classList.remove('show'); if (ok) ok.classList.add('show'); f.reset();
    });
    f.setAttribute('novalidate', '');
  });

  /* Home hero slider */
  var hs = $('.hs__frame');
  if (hs) {
    var sl = $$('.hs-slide', hs), dt = $$('.hs__dots button', hs), cur = 0, tm;
    function go(n) { sl[cur].classList.remove('on'); dt[cur].classList.remove('on'); cur = (n + sl.length) % sl.length; sl[cur].classList.add('on'); dt[cur].classList.add('on'); }
    function auto() { clearInterval(tm); tm = setInterval(function () { go(cur + 1); }, 5000); }
    dt.forEach(function (d, i) { d.addEventListener('click', function () { go(i); auto(); }); });
    auto();
  }
  /* Category strip arrows */
  $$('.ss__cats').forEach(function (w) {
    var t = $('.ss__track', w);
    $$('.ss-arrow', w).forEach(function (b) { b.addEventListener('click', function () { t.scrollBy({ left: (b.classList.contains('ss-arrow--prev') ? -1 : 1) * t.clientWidth * .6, behavior: 'smooth' }); }); });
  });
  /* Rolling counter */
  var counter = $('.counter');
  if (counter && 'IntersectionObserver' in window) {
    var co = new IntersectionObserver(function (es) {
      if (!es[0].isIntersecting) return;
      $$('.roll', counter).forEach(function (r, i) {
        var col = $('.roll__col', r), h = r.clientHeight, d = +r.dataset.d;
        setTimeout(function () { col.style.transform = 'translateY(' + (-d * h) + 'px)'; }, i * 180);
      });
      co.disconnect();
    }, { threshold: .4 });
    co.observe(counter);
  }

  /* header search toggle (tablet/mobile widths, where the search box collapses to an icon) */
  var st = $('.hdr__stoggle'), sf = $('#hdr-search');
  if (st && sf) {
    st.addEventListener('click', function () {
      var open = !document.body.classList.contains('search-open');
      document.body.classList.toggle('search-open', open); st.setAttribute('aria-expanded', open);
      if (open) setTimeout(function () { var i = $('#q-top'); if (i) i.focus(); }, 30);
    });
    document.addEventListener('keydown', function (e) { if (e.key === 'Escape' && document.body.classList.contains('search-open')) { document.body.classList.remove('search-open'); st.setAttribute('aria-expanded', 'false'); st.focus(); } });
  }
})();
