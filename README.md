# Rosier Foods — website redesign (HTML)

Open `index.html` in any browser (you need to be online: product photos load straight from your live Shopify store).

## What's inside — 63 pages
- `index.html` — Homepage, same structure as the live rosierfoods.com homepage (hero slider, hamper + laddoo tiles, category icons, village illustration, Loved Across Generations, New Arrivals, More Than a Brand counter, Experience video, values, heritage, testimonials, trust icons, footer)
- `shop.html` — All products
- `collection-ghee.html`, `collection-stone-press-oil.html`, `collection-pickles.html`, `collection-atta.html`, `collection-healthy-snacking.html`, `collection-immunity-booster.html` — the six category pages, same products and order as the live collections
- `product-<handle>.html` — one page for each of the 46 products (`product.html` is the ghee page)
- `our-story.html`, `lab-reports.html` (links to the real report PDFs), `hampers.html`, `contact.html`, `cart.html`, `membership.html`

## Images
Real photography throughout: Gir cows, village bilona churning, the Rosier unit, ghee making, hamper shoots and product lifestyle shots, all pulled from your live store. The homepage values, farm-to-kitchen journey, heritage band, brand story, category banners and Our Story page are all photo-led.

Every product, banner, category, testimonial and illustration image is hotlinked from your store's CDN
(cdn.shopify.com / rosierfoods.com/cdn). If you replace an image in Shopify, update its URL in `source/data.py`.
Hamper photos and logo files in `assets/img` are from your Parampara repo.

## Prices
Prices, MRPs, ratings and badges are a snapshot of the live site on 1 Nov 2026.

## Editing everything at once
`source/data.py` holds products, collections and homepage images. `source/pages/` holds each page.
Run `python3 build.py` inside `source/` to regenerate every page.

## Shopping features (work offline in the browser, no backend needed)
- Cart that remembers items across pages, with a slide-out cart drawer, free-gift progress (₹2,499 / ₹4,999 / ₹7,999), Benefit Club savings and add-on suggestions
- Live product search with photos and prices
- Quick view on every product card
- Product pages: size selector, sticky Add to Cart bar, lab report link, Frequently Bought Together bundle, Recently Viewed
- Collection pages: price slider, rating, offer and pack-type filters, plus sorting
- Homepage: Shop by Need tabs, tabbed bestsellers, farm-to-kitchen journey, lab report finder, review summary, founder note, FAQ
- Mobile bottom navigation, WhatsApp chat button
Checkout buttons are not connected to Shopify; your developer wires them to the store's checkout when this goes live.

## Audit pass (Competitive Website Audit, 1 Nov 2026)
- Homepage follows the recommended order: hero → category/need → bestsellers → proof & standards → process → founder & brand story → reviews → membership → guides & FAQ. Duplicate carousels, the unlabeled counter, the offer band and decorative illustration strips were removed.
- New `standards.html` (Our Standards): claims with evidence links, the 6 FSSAI-licensed units with licence numbers and batch codes (from your Manufacturer List page), lab reports, delivery/returns/cancellation terms (from your live policies).
- Product pages: "why this product" points, stock status, sold-out sizes disabled, delivery 3–5 days, 2-day return rules, product details (net quantity, ingredients/storage where stated, maker, lab report), how to use, Buy Now.
- Shop by Need uses plain, non-medical labels.
- Structured data (Product, BreadcrumbList, Organization), skip link, visible focus, labelled controls, consent checkbox on sign-up.

### Still needs Rosier's input
- Lab report dates and issuing labs (the PDFs are scanned images, so they must be typed in)
- Names and photos of real farmers/suppliers and a founder portrait you approve
- Review dates and variants (export from your reviews app)
- Membership exclusions and terms
- Connecting checkout to Shopify, then real-device speed and usability tests

## Animations
Crossfading hero slider, scroll reveals, product photo swap on hover, rolling number counter, scrolling strips,
hover lifts. All motion switches off for visitors who've turned on "reduce motion".
