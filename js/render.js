/* Rosier — config-driven rendering for the announcement ticker, hero banner carousel,
   homepage ptile tiles and category carousel. Content lives in config/banners.js and
   config/homepage.js; this file only reads it. Loaded without `defer` so each block can be
   rendered by a tiny inline call right after its container (no flash, hero image starts early). */
(function () {
  'use strict';
  var RM = window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches;

  function esc(s) { return String(s == null ? '' : s).replace(/[&<>"']/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]; }); }
  function day(s, endOfDay) {
    if (!s) return null;
    var p = String(s).split('-'); if (p.length !== 3) return null;
    return endOfDay ? new Date(+p[0], +p[1] - 1, +p[2], 23, 59, 59) : new Date(+p[0], +p[1] - 1, +p[2]);
  }
  /* active flag + optional start/end window (inclusive, visitor's local time) */
  function live(item, now) {
    if (!item || item.active === false) return false;
    now = now || new Date();
    var s = day(item.start), e = day(item.end, true);
    return !(s && now < s) && !(e && now > e);
  }
  function warn(m) { if (window.console) console.warn('[Rosier config] ' + m); }
  /* Shopify CDN images can be resized on the fly with &width= */
  function cdn(u) { return /cdn\.shopify\.com|\/cdn\/shop\//.test(u); }
  function sized(u, w) { return u + (u.indexOf('?') > -1 ? '&' : '?') + 'width=' + w; }
  function srcset(u, ws) { return cdn(u) ? ws.map(function (w) { return sized(u, w) + ' ' + w + 'w'; }).join(', ') : ''; }

  var R = window.RosierRender = { live: live };

  /* ---------------- Announcement ticker ---------------- */
  R.ticker = function (el) {
    var cfg = window.ROSIER_SITE;
    if (!el || !cfg || !Array.isArray(cfg.announcements)) return;
    var msgs = cfg.announcements.filter(function (a) { return live(a) && a.text; });
    if (!msgs.length) { el.hidden = true; return; }
    var item = function (a) { return '<li>' + (a.href ? '<a href="' + esc(a.href) + '">' + esc(a.text) + '</a>' : '<span>' + esc(a.text) + '</span>') + '</li>'; };
    var list = msgs.map(item).join('');
    el.classList.toggle('ann--static', msgs.length === 1 || RM);
    el.innerHTML = '<ul class="sr-only" aria-label="Current offers">' + list + '</ul>' +
      '<div class="ann__view" aria-hidden="true"><ul class="ann__track">' + list + (msgs.length > 1 && !RM ? list : '') + '</ul></div>';
    // the moving copy is for sighted mouse/touch users; keyboard and screen-reader users get the
    // same offers as a static, focusable list (sr-only above), so nothing is announced twice
    el.querySelectorAll('.ann__view a').forEach(function (a) { a.tabIndex = -1; });
    var track = el.querySelector('.ann__track');
    if (msgs.length > 1 && !RM) track.style.animationDuration = Math.max(18, msgs.length * 9) + 's';
  };

  /* ---------------- Hero banner carousel ---------------- */
  R.hero = function (el) {
    var cfg = window.ROSIER_BANNERS;
    if (!el) return;
    if (!cfg || !Array.isArray(cfg.banners)) { warn('banners.js missing or invalid, hero hidden'); el.hidden = true; return; }
    var st = cfg.settings || {}, bp = st.mobileBreakpoint || 767;
    var list = cfg.banners.filter(function (b) {
      if (!live(b)) return false;
      if (!b.desktop || !b.desktop.src) { warn('banner "' + b.id + '" has no desktop image, skipped'); return false; }
      return true;
    }).sort(function (a, b) { return (a.order || 99) - (b.order || 99); });
    if (!list.length) { el.hidden = true; return; }
    el.style.setProperty('--hb-d', st.desktopRatio || '3 / 1');
    el.style.setProperty('--hb-m', st.mobileRatio || '4 / 3');

    var slides = list.map(function (b, i) {
      var d = b.desktop, m = b.mobile && b.mobile.src ? b.mobile : d, first = i === 0;
      var dS = srcset(d.src, [1200, 1600, 2400, 3000]), mS = srcset(m.src, [480, 800, 1200, 1600]);
      var attr = function (n, v) { return v ? (first ? ' ' + n + '="' + esc(v) + '"' : ' data-' + n + '="' + esc(v) + '"') : ''; };
      var hasText = b.headline || b.subheading || b.offer;
      var text = hasText ? '<div class="hb__text' + (b.showText ? '' : ' sr-only') + '">' +
        (b.offer ? '<p class="hb__offer">' + esc(b.offer) + '</p>' : '') +
        (b.headline ? '<h2 class="hb__h">' + esc(b.headline) + '</h2>' : '') +
        (b.subheading ? '<p class="hb__sub">' + esc(b.subheading) + '</p>' : '') + '</div>' : '';
      var pos = (b.ctaX ? '--cta-x:' + esc(b.ctaX) + ';' : '') + (b.ctaY ? '--cta-y:' + esc(b.ctaY) + ';' : '');
      var cta = b.href ? '<a class="hb__cta' + (b.showButton || b.showText ? '' : ' sr-only') + '" href="' + esc(b.href) + '"' + (pos ? ' style="' + pos + '"' : '') + '>' + esc(b.ctaLabel || 'Shop now') + '<svg aria-hidden="true"><use href="#i-arrow"/></svg></a>' : '';
      return '<div class="hb__slide' + (first ? ' is-on' : '') + '" role="group" aria-roledescription="slide" aria-label="' + (i + 1) + ' of ' + list.length + '"' + (first ? '' : ' aria-hidden="true"') + ' data-id="' + esc(b.id) + '">' +
        (b.href ? '<a class="hb__hit" href="' + esc(b.href) + '" tabindex="-1" aria-hidden="true"></a>' : '') +
        '<picture>' +
        '<source media="(max-width: ' + bp + 'px)"' + attr('srcset', mS || m.src) + ' sizes="100vw" width="' + (m.width || '') + '" height="' + (m.height || '') + '">' +
        '<img' + attr('src', cdn(d.src) ? sized(d.src, 1600) : d.src) + attr('srcset', dS) + ' sizes="(max-width: 1440px) 100vw, 1440px" width="' + (d.width || 3000) + '" height="' + (d.height || 1000) + '" alt="' + esc(b.alt || b.headline || '') + '"' +
        (first ? ' fetchpriority="high" decoding="async"' : ' decoding="async"') + ' style="object-position:' + esc(b.position || 'center') + '">' +
        '</picture>' + text + cta + '</div>';
    }).join('');
    var n = list.length;
    var dots = n > 1 ? '<div class="hb__dots" role="group" aria-label="Choose banner">' + list.map(function (b, i) {
      return '<button type="button" class="hb__dot' + (i ? '' : ' is-on') + '" aria-label="Show banner ' + (i + 1) + ': ' + esc(b.headline || b.alt || '') + '"' + (i ? '' : ' aria-current="true"') + '></button>'; }).join('') + '</div>' : '';
    var arrows = n > 1 ? '<button type="button" class="hb__arw hb__arw--p" aria-label="Previous banner"><svg aria-hidden="true"><use href="#i-arrow"/></svg></button><button type="button" class="hb__arw hb__arw--n" aria-label="Next banner"><svg aria-hidden="true"><use href="#i-arrow"/></svg></button>' : '';
    var pause = n > 1 && !RM ? '<button type="button" class="hb__pause" aria-label="Pause banner rotation"><span aria-hidden="true"></span></button>' : '';
    el.innerHTML = '<div class="hb__viewport" aria-live="off">' + slides + '</div>' + arrows + dots + pause;
    el.dataset.count = n;
    if (n < 2) return; // single banner: no autoplay, no controls

    var S = el.querySelectorAll('.hb__slide'), D = el.querySelectorAll('.hb__dot'), cur = 0, timer = null,
      hover = false, focus = false, userPaused = false, interval = Math.max(2500, st.intervalMs || 5000);
    function hydrate(i) {
      var s = S[i]; if (!s || s.dataset.ready) return; s.dataset.ready = '1';
      s.querySelectorAll('[data-src],[data-srcset]').forEach(function (x) {
        if (x.dataset.srcset) { x.srcset = x.dataset.srcset; x.removeAttribute('data-srcset'); }
        if (x.dataset.src) { x.src = x.dataset.src; x.removeAttribute('data-src'); }
      });
    }
    S[0].dataset.ready = '1';
    function go(i) {
      i = (i + n) % n; if (i === cur) return;
      hydrate(i); hydrate((i + 1) % n);
      S[cur].classList.remove('is-on'); S[cur].setAttribute('aria-hidden', 'true');
      S[cur].querySelectorAll('a').forEach(function (a) { a.tabIndex = -1; });
      S[i].classList.add('is-on'); S[i].removeAttribute('aria-hidden');
      S[i].querySelectorAll('a:not(.hb__hit)').forEach(function (a) { a.removeAttribute('tabindex'); });
      D[cur].classList.remove('is-on'); D[cur].removeAttribute('aria-current');
      D[i].classList.add('is-on'); D[i].setAttribute('aria-current', 'true');
      cur = i; el.dataset.current = i;
    }
    S.forEach(function (s, i) { if (i) s.querySelectorAll('a').forEach(function (a) { a.tabIndex = -1; }); });
    function canPlay() { return !RM && !userPaused && !hover && !focus && !document.hidden; }
    function stop() { clearInterval(timer); timer = null; }
    function play() { stop(); if (canPlay()) timer = setInterval(function () { go(cur + 1); }, interval); el.classList.toggle('is-paused', !timer); }
    R._hero = { go: function (i) { go(i); play(); }, state: function () { return { cur: cur, playing: !!timer, n: n }; } };

    el.querySelector('.hb__arw--p').addEventListener('click', function () { go(cur - 1); play(); });
    el.querySelector('.hb__arw--n').addEventListener('click', function () { go(cur + 1); play(); });
    D.forEach(function (d, i) { d.addEventListener('click', function () { go(i); play(); }); });
    var pb = el.querySelector('.hb__pause');
    if (pb) pb.addEventListener('click', function () {
      userPaused = !userPaused; pb.setAttribute('aria-label', userPaused ? 'Play banner rotation' : 'Pause banner rotation'); pb.classList.toggle('is-play', userPaused); play();
    });
    el.addEventListener('mouseenter', function () { hover = true; play(); });
    el.addEventListener('mouseleave', function () { hover = false; play(); });
    el.addEventListener('focusin', function () { focus = true; play(); });
    el.addEventListener('focusout', function (e) { if (!el.contains(e.relatedTarget)) { focus = false; play(); } });
    document.addEventListener('visibilitychange', play);
    el.addEventListener('keydown', function (e) {
      if (e.key === 'ArrowRight') { go(cur + 1); play(); e.preventDefault(); }
      else if (e.key === 'ArrowLeft') { go(cur - 1); play(); e.preventDefault(); }
    });
    // touch swipe
    var x0 = null, y0 = 0;
    el.addEventListener('touchstart', function (e) { x0 = e.touches[0].clientX; y0 = e.touches[0].clientY; hover = true; stop(); }, { passive: true });
    el.addEventListener('touchend', function (e) {
      if (x0 == null) return;
      var dx = e.changedTouches[0].clientX - x0, dy = e.changedTouches[0].clientY - y0; x0 = null; hover = false;
      if (Math.abs(dx) > 40 && Math.abs(dx) > Math.abs(dy)) go(cur + (dx < 0 ? 1 : -1));
      play();
    }, { passive: true });
    // warm the next banner once the page has loaded, never before the first one
    window.addEventListener('load', function () { setTimeout(function () { hydrate(1); }, 600); });
    play();
  };

  /* ---------------- Promo tiles ---------------- */
  R.promos = function (el) {
    var cfg = window.ROSIER_SITE; if (!el || !cfg || !Array.isArray(cfg.promoTiles)) return;
    var t = cfg.promoTiles.filter(function (p) { return live(p) && p.image && p.href; });
    if (!t.length) { el.hidden = true; return; }
    el.innerHTML = t.map(function (p) {
      return '<a class="ptile" href="' + esc(p.href) + '"><img src="' + esc(cdn(p.image) ? sized(p.image, 800) : p.image) + '"' +
        (cdn(p.image) ? ' srcset="' + srcset(p.image, [400, 600, 800]) + '" sizes="(max-width:900px) 50vw, 380px"' : '') +
        ' width="' + (p.width || 800) + '" height="' + (p.height || 436) + '" alt="' + esc(p.alt || p.title) + '" loading="lazy" decoding="async">' +
        '<span class="ptile__t">' + esc(p.title) + '<svg aria-hidden="true"><use href="#i-arrow"/></svg></span></a>';
    }).join('');
  };

  /* ---------------- Category carousel ---------------- */
  R.rcats = function (el) {
    var cfg = window.ROSIER_SITE; if (!el || !cfg || !Array.isArray(cfg.categories)) return;
    var c = cfg.categories.filter(function (x) { return live(x) && x.name && x.href; });
    if (!c.length) { el.hidden = true; return; }
    var track = el.querySelector('.rcats__track');
    track.innerHTML = c.map(function (x) {
      return '<a class="rcat" href="' + esc(x.href) + '"><span class="rcat__img"><img src="' + esc(cdn(x.image) ? sized(x.image, 300) : x.image) + '"' +
        (cdn(x.image) ? ' srcset="' + sized(x.image, 200) + ' 200w, ' + sized(x.image, 300) + ' 300w, ' + sized(x.image, 450) + ' 450w" sizes="150px"' : '') +
        ' width="300" height="300" alt="" loading="lazy" decoding="async"></span>' +
        '<span class="rcat__n">' + esc(x.name) + '</span>' + (x.note ? '<span class="rcat__s">' + esc(x.note) + '</span>' : '') + '</a>';
    }).join('');
    var p = el.querySelector('.rcats__arw--p'), nx = el.querySelector('.rcats__arw--n');
    function upd() {
      var max = track.scrollWidth - track.clientWidth - 2;
      p.disabled = track.scrollLeft <= 2; nx.disabled = track.scrollLeft >= max;
      el.classList.toggle('cats--fits', max <= 0);
    }
    function step(dir) { track.scrollBy({ left: dir * Math.max(track.clientWidth * .8, 160), behavior: RM ? 'auto' : 'smooth' }); }
    p.addEventListener('click', function () { step(-1); }); nx.addEventListener('click', function () { step(1); });
    track.addEventListener('scroll', upd, { passive: true }); window.addEventListener('resize', upd); upd();
    window.addEventListener('load', upd);
  };
})();
