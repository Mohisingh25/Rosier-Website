FILE = 'membership.html'
TITLE = "Rosier's Benefit Club – Membership | Rosier Foods"
DESC = "Join Rosier's Benefit Club. 15% off on all orders, free & fast shipping, a birthday surprise box and more. Starting at ₹299."
ACTIVE = 'club'
_src = open(SRC + '/partials/membership-source.html').read()
BODY = _src[_src.index('<main>') + 6:_src.index('</main>')]
BODY = (BODY.replace('assets/images/hero-hamper.svg', 'assets/img/hamper-open-lifestyle.jpg')
            .replace('assets/images/cta-box.svg', 'assets/img/combo-ghee-honey.jpg')
            .replace('assets/images/member-', 'MEMBER-'))
for _i,_h in enumerate(['a2-desi-cow-ghee-hand-churned-from-curd','wild-flower-honey','amlaprash','khapli-emmer-wheat-atta-stoneground-high-fiber-for-gut-health','high-protein-oats-assorted-pack','mango-pickle'],1):
    BODY = BODY.replace(f'MEMBER-{_i}.svg', img(BY[_h][8], 700))
_s = _src.index('<!-- Mobile sticky CTA -->')
AFTER = _src[_s:_src.index('<script', _s)]
import re as _re
BODY = _re.sub(r'(<div class="tcard__img"><img src="[^"]+" alt=")[^"]*(")', r'\1Rosier products\2', BODY)

TERMS = f'''
<section class="section terms-sec" id="terms"><div class="container" style="max-width:900px">
  <header class="section-head">{eyebrow('Before you join', True)}<h2>Membership terms</h2><p class="section-sub">What you get, for how long, and what is not included. Read this before you pay.</p></header>
  <div class="terms">
    <h3>Price and duration</h3>
    <table class="terms__t"><thead><tr><th scope="col">Plan</th><th scope="col">One-time fee</th><th scope="col">Works out to</th><th scope="col">Valid for</th></tr></thead>
    <tbody>{''.join(f'<tr><td data-l="Plan">{d}</td><td data-l="One-time fee">{inr(pr)}</td><td data-l="Works out to">{inr(round(pr / int(d.split()[0])))}/month</td><td data-l="Valid for">{d} from the day you join</td></tr>' for d, pr in PLANS)}</tbody></table>
    <h3>What every plan includes</h3>
    <ul><li>15% off orders placed on rosierfoods.com while the plan is active.</li><li>Free shipping on orders while the plan is active.</li><li>A birthday surprise box, if your birthday falls within your plan and is saved in your account.</li><li>A free 1 L ghee once your orders during the plan add up to {inr(15000)}.</li><li>Member-only offers, early access and priority support.</li></ul>
    <h3>How much you save</h3>
    <p>Your saving depends on how much you order. For example, 15% off {inr(2000)} of orders is {inr(300)}, which covers the 3-month fee. If you order less than that during your plan, the membership may cost more than it saves.</p>
    <h3>Not included</h3>
    <ul><li>Orders on Amazon, Blinkit or other apps and marketplaces.</li></ul>
    <p class="owner-note"><b>Content pending from Rosier:</b> whether the 15% stacks with sale prices or coupons, whether gift hampers are excluded, auto-renewal, and the refund rule for the membership fee. Until Rosier confirms these, the terms shown at checkout apply.</p>
  </div>
</div></section>'''
BODY = BODY.replace('<!-- ============ WHY JOIN ============ -->', TERMS + '\n<!-- ============ WHY JOIN ============ -->', 1)
BODY = (BODY.replace('<a href="#" class="btn btn--outline">Talk to us</a>', '<a href="contact.html" class="btn btn--outline">Talk to us</a>')
            .replace('<a href="#">See our lab reports</a>', '<a href="lab-reports.html">See our lab reports</a>')
            .replace('Membership fees follow our <a href="#">Refund Policy</a>. If something doesn\'t feel right, reach out to our team through Help and we\'ll sort it out with you.',
                     'The refund rule for membership fees is still being confirmed by Rosier, so please check it at checkout. If something doesn\'t feel right, <a href="contact.html">contact our team</a> and we\'ll sort it out with you.')
            .replace('Simple maths. Two orders of about ₹1,000 each save you ₹300 at 15% off.', 'Simple maths. Two orders of ₹1,000 each save you ₹300 at 15% off.')
            .replace('<p class="hero__micro reveal" style="--d:.4s">More benefits. More savings. More love.</p>', '<p class="hero__micro reveal" style="--d:.4s">More benefits. More savings. More love. <a href="#terms" style="text-decoration:underline">See terms</a></p>'))
for _k in ('3m', '6m', '12m'):
    BODY = BODY.replace(f'<a href="#" class="btn btn--outline btn--block" data-plan="{_k}">', f'<a href="{JOIN_URL}" class="btn btn--outline btn--block" data-plan="{_k}">')
    BODY = BODY.replace(f'<a href="#" class="btn btn--gold btn--block" data-plan="{_k}">', f'<a href="{JOIN_URL}" class="btn btn--gold btn--block" data-plan="{_k}">')
BODY = BODY.replace('<div class="earnback reveal">', '<p class="tax" style="text-align:center;margin-top:14px">Joining opens your Rosier account on rosierfoods.com. <a href="#terms" style="text-decoration:underline">Read the terms first</a>.</p>\n    <div class="earnback reveal">', 1)
assert 'href="#"' not in BODY, 'dead link left'
