FILE = 'contact.html'
TITLE = 'Contact Us | Rosier Foods'
DESC = 'Get in touch with Rosier Foods for order help, product questions, bulk orders or feedback.'
ACTIVE = 'contact'

BODY = f'''
<section class="page-hero">
  <div class="container">
    <nav class="crumbs reveal"><a href="index.html">Home</a><span>/</span>Contact</nav>
    <h1 class="reveal" style="--d:.06s">We'd love to <em>hear from you</em></h1>
    <p class="lead reveal" style="--d:.12s">Order help, a product question, or just want to say hi? Drop us a note. You're family, after all.</p>
  </div>
</section>

<section style="padding:20px 0 clamp(72px,9vw,120px)">
  <div class="container contact-grid">
    <div class="info-cards">
      <div class="info reveal"><span class="ico"><svg><use href="#i-pin"/></svg></span><div><h3>Delhi</h3><p>Rosier Foods Pvt. Ltd.<br>Burari, Delhi 110084</p></div></div>
      <div class="info reveal" style="--d:.06s"><span class="ico"><svg><use href="#i-pin"/></svg></span><div><h3>Noida</h3><p>Rosier Foods Pvt. Ltd.<br>Sector 6, Noida, Uttar Pradesh 201301</p></div></div>
      <div class="info reveal" style="--d:.12s"><span class="ico"><svg><use href="#i-headset"/></svg></span><div><h3>Members come first</h3><p>Benefit Club members get priority customer support. <a href="membership.html">Join the club</a></p></div></div>
      <div class="reveal" style="--d:.18s">
        <p class="opt-label" style="margin:14px 0 10px">Quick help</p>
        <div class="quick-links">
          <a href="#">Shipping Policy <svg><use href="#i-arrow"/></svg></a>
          <a href="#">Refund Policy <svg><use href="#i-arrow"/></svg></a>
          <a href="lab-reports.html">Lab Reports <svg><use href="#i-arrow"/></svg></a>
          <a href="hampers.html#enquiry">Bulk &amp; Corporate <svg><use href="#i-arrow"/></svg></a>
        </div>
      </div>
    </div>

    <form class="form-card reveal" style="--d:.1s" data-demo>
      <h3>Send us a message</h3><p>Tell us what's up and our team will get back to you.</p>
      <div class="fields">
        <div class="field"><label for="c-name">Your name</label><input id="c-name" required></div>
        <div class="field"><label for="c-ph">Phone</label><input id="c-ph" type="tel" required></div>
        <div class="field"><label for="c-em">Email</label><input id="c-em" type="email"></div>
        <div class="field"><label for="c-t">What's it about?</label><select id="c-t"><option>Help with my order</option><option>Product question</option><option>Bulk or corporate order</option><option>Benefit Club membership</option><option>Feedback</option><option>Something else</option></select></div>
        <div class="field field--full"><label for="c-o">Order number (if you have one)</label><input id="c-o" placeholder="#1234"></div>
        <div class="field field--full"><label for="c-msg">Message</label><textarea id="c-msg" required></textarea></div>
      </div>
      <button class="btn btn--primary btn--block" type="submit">Send Message <svg><use href="#i-arrow"/></svg></button>
      <p class="form-ok">Got it! We'll be in touch soon.</p>
    </form>
  </div>
</section>
'''
