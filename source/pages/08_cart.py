FILE = 'cart.html'
TITLE = 'Your Cart | Rosier Foods'
DESC = 'Your Rosier Foods cart.'
ACTIVE = 'cart'

def citem(img, name, size, price, mrp, q):
    return f'''<div class="citem" data-price="{price}" data-mrp="{mrp}">
  <div class="citem__img"><img src="{img}" alt="{name}"></div>
  <div><h3>{name}</h3><small>{size} · <s>{inr(mrp)}</s> {inr(price)} each</small>
    <div class="qty"><button data-d="-" aria-label="Decrease">−</button><input value="{q}" aria-label="Quantity"><button data-d="+" aria-label="Increase">+</button></div></div>
  <div class="citem__right"><b class="line">{inr(price*q)}</b><button data-remove>Remove</button></div>
</div>'''

BODY = f'''
<section class="page-hero" style="padding-bottom:40px">
  <div class="container">
    <nav class="crumbs reveal"><a href="index.html">Home</a><span>/</span>Cart</nav>
    <h1 class="reveal" style="--d:.06s">Your cart</h1>
  </div>
</section>

<section>
  <div class="container">
    <div class="cart-grid">
      <div>
        <div class="gift-bar reveal">
          <p id="gift-msg"></p>
          <div class="gift-bar__track"><div class="gift-bar__fill"></div></div>
          <div class="gift-bar__marks"><span style="left:0">₹0</span><span style="left:31.2%">Bottle · ₹2,499</span><span style="left:62.5%">Tumbler · ₹4,999</span><span style="left:100%">Both · ₹7,999</span></div>
        </div>
        <div class="cart-items" id="cart-items"></div>
        <a href="shop.html" class="link-arrow" style="margin-top:24px"><svg style="transform:scaleX(-1)"><use href="#i-arrow"/></svg> Continue shopping</a>
      </div>

      <aside class="summary reveal" style="--d:.1s">
        <h3>Order summary</h3>
        <div class="sum-row"><span>MRP total</span><b id="s-mrp"></b></div>
        <div class="sum-row"><span>Discount on MRP</span><b id="s-save" style="color:var(--olive)"></b></div>
        <div class="sum-row"><span>Shipping</span><b>Shown at checkout, before you pay</b></div>
        <div class="coupon"><input placeholder="Coupon code" aria-label="Coupon code"><button class="btn btn--outline btn--sm">Apply</button></div>
        <div class="sum-row sum-row--total"><span>Total</span><b id="s-total"></b></div>
        <p class="tax">Tax included.</p>
        <a href="#" class="btn btn--primary btn--block">Checkout <svg><use href="#i-arrow"/></svg></a>
        <div class="club-upsell">Benefit Club members get 15% off every order. That's about <b id="s-club"></b> on this cart.<br><a href="membership.html">Join from ₹299 →</a></div>
        <p class="secure"><svg><use href="#i-truck"/></svg>Usually delivered in 3–5 days</p><p class="secure" style="margin-top:4px"><svg><use href="#i-check"/></svg><a href="standards.html#returns" style="text-decoration:underline">2-day returns on damaged or wrong items</a></p>
      </aside>
    </div>
    <div class="empty-cart"><h3>Your cart is empty</h3><p style="color:var(--muted);margin-top:8px">Let's fix that. Start with our bestselling A2 ghee.</p><a href="shop.html" class="btn btn--primary">Shop Now</a></div>
  </div>
</section>

<section class="section bg-cream2">
  <div class="container">
    <div class="head-row reveal"><div>{eyebrow('Add a little more')}<h2>You might also love</h2></div>{car_btns('more')}</div>
    {carousel('more', ['amlaprash','mango-pickle','wood-pressed-black-mustard-oil','gond-laddoo','high-protein-oats-assorted-pack','nut-butter-dark-chocolate'])}
  </div>
</section>
'''
