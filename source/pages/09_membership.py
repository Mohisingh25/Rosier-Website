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
