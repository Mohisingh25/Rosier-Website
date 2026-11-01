# Rosier Foods website: independent QA report

**Date:** 1 Nov 2026
**Build:** 72 HTML pages plus `product.html`, which redirects to the ghee page
**Method:** automated browser testing (Chromium/Playwright) of every page at 360, 390, 430, 768, 1024, 1440 and 1920 px; five scripted user journeys (39 checks); static link, SEO and image audits; screenshots reviewed by eye.

**Test-environment limit:** the test machine cannot reach cdn.shopify.com or Google Fonts. Pages were therefore tested without product photos and webfonts. All image URLs had already been confirmed loading from the live CDN in a real browser in an earlier pass. Final visual sign-off should be done on the deployed GitHub Pages URL.

---

## 1. Scores (honest, evidence-based)

| # | Criterion | Before QA | After QA | Why it's not 10 |
|---|---|---|---|---|
| 1 | Visual appeal | 7 | 8.5 | Not yet checked with real photos and fonts on real phones. |
| 2 | Brand identity | 6.5 | 8.5 | Founder portrait and farmer photos not yet supplied. |
| 3 | Homepage structure | 6.5 | 8.5 | All 14 sections are present and in order. Farmer stories are an honest placeholder until verified profiles exist. |
| 4 | Product discovery | 7 | 8.5 | Search runs in the browser with no typo tolerance. There is no server-side search or analytics. |
| 5 | Product presentation | 6.5 | 8 | Nutrition tables are pending. Reviews for products other than ghee link out to rosierfoods.com. |
| 6 | Trust & credibility | 7 | 8 | Lab names and dates are still pending. Batch-level traceability needs Rosier's batch data. |
| 7 | Storytelling | 6 | 7.5 | All six story pages exist, but the farmer and founder content needs Rosier's verified material. |
| 8 | Navigation | 6.5 | 9 | Mega menu, story dropdown, mobile drawer and bottom nav all work. No broken links or anchors. |
| 9 | Conversion strategy | 5.5 | 8 | The checkout handoff to the Shopify cart link was not live-tested, to avoid touching the real store. The membership "Join" link is a placeholder. |
| 10 | Content hierarchy | 6.5 | 9 | Every page has one h1 and no skipped heading levels. |

No criterion is scored 10/10. Testing does not prove 10 while owner content is missing and live checkout, real-device speed and screen-reader tests have not been done.

---

## 2. Issues found and fixed

### Visibility (the user-reported bug)
- **Cause:** a CSS rule in `bharat.css` replaced the dark gradient backgrounds of `.plan--featured`, `.final`, `.club-band`, `.shop-promo` and `.club-upsell` with a pattern image. That left light text on a light background. The rule was removed and dark backgrounds are now forced in `qa.css`.
- **Verified by screenshot:**
  - desktop and 390 px: the "Most Popular" 6-month card
  - desktop and 390 px: the "Join Rosier Parivaar Today!" band
- **Checker blind spot fixed:** the contrast checker used to skip any element with a background image, which is why the bug was missed. It now tests text against every colour stop of a gradient. The improved checker found more problems, all now fixed:
  - the shop promo heading had dark text on a dark card (contrast 1.19)
  - the category tile overlay was too weak
  - gold step numbers on white (2.6)
  - the ₹ coin and "+" icons had low contrast
- The closed cart drawer cast a shadow strip down the right edge of every page. Fixed: closed drawers have no shadow and are hidden from keyboard tab order.
- Focus outlines are now light on dark sections, so keyboard focus stays visible there.
- On mobile the WhatsApp button covered the membership "Join" bar and the sticky add-to-cart bar. Both are restacked above the bottom nav.

### Broken functionality
- Cart and drawer "Checkout" went nowhere (`href="#"`). Each now builds a Shopify cart link, e.g. `rosierfoods.com/cart/VARIANT:QTY,...`, from the real variant IDs, labelled "Checkout on rosierfoods.com". Payment is confirmed only by Shopify.
- The fake coupon field was removed. The page now says coupons are entered at checkout.
- Membership "Join Now" (×3), "Talk to us", "Refund Policy" and the lab reports link were dead. All now point to real pages.
- Contact page "Shipping/Refund Policy" links were dead. They now go to `faq.html#orders` and `faq.html#returns`.
- `product.html` duplicated the ghee page (same title and content). It is now a redirect, and all links point to the real ghee page.
- The honey and nut-butter collections crashed the build. Banners were added.

### Missing features added (from the master prompt)
- **Trust page:** "Know Your Food. Know Its Journey."
  - product selector showing ingredients, storage and the lab report link
  - lab name/date marked as pending
  - maker and FSSAI table, and the batch-letter explainer
- **Story pages:** Our Founder, Our Farmers, Our Process, Our Philosophy and Our Commitment, plus FAQ and 404 pages.
- **Shop page:**
  - category filter on top of price, rating, offer and pack size/type
  - `?q=` results page, with Enter in the search box going there
  - search by ingredient and keyword (for example "gut health" or "achar")
  - empty-search and no-results states with suggestions
- **Product pages:**
  - PIN code check: checks the format only and says honestly that delivery is confirmed at checkout
  - product FAQs
  - nutrition row
  - size buttons expose their selected state to screen readers (aria-pressed)
  - cart lines store the Shopify variant ID
- **Membership:** `#terms` section with price, duration, per-month cost, what's included, a worked savings example that shows when membership may not pay off, exclusions, and owner-pending items.
- **Forms:** the newsletter and contact forms now show validation messages. Success messages no longer claim anything was sent to a server.

### Mobile layout
- The product page was 616 px wide at 360–430 px because the gallery thumbnails overflowed. Fixed.
- The contact and hampers forms overflowed at 360 px and 1024 px. Fixed by making the grid fields able to shrink (`min-width:0`).
- The membership terms table becomes labelled rows on phones.
- The trust bar scrolls sideways on mobile instead of being cut off.

### Accessibility
- Fixed heading-level skips on 64 pages: filters, product FAQs, order summary, and story pages via screen-reader-only h2s.
- Burger menu reports open/closed state (`aria-expanded`) and moves focus into the drawer. "Search" in the bottom nav focuses the search box.
- Hidden duplicate image links in product cards are hidden from screen readers too, and taken out of tab order.

### Performance
- The first image in `<main>` loads first, with high fetch priority, to speed up the largest visible image.
- All other images:
  - load lazily and decode asynchronously
  - have width and height set, so the layout doesn't jump while they load
  - product cards use srcset with 300 w and 600 w versions
- Images are served from Shopify's CDN, which sends WebP automatically to browsers that accept it. All scripts are `defer`.
- Total size: CSS 114 KB, JS 61 KB, both unminified.

### SEO
- All 72 pages have:
  - a unique title
  - a meta description
  - a canonical URL (GitHub Pages base)
  - Open Graph tags
- 97 JSON-LD blocks (Organization, Product, BreadcrumbList), all valid JSON.
- `sitemap.xml` lists 70 URLs. `robots.txt` blocks the cart and points to the sitemap.

### Brand
- No green headings or decorative icons, checked on the rendered pages: a scan of 72 pages found 0. The WhatsApp button and the real Rosier logo keep their own colours.
- Primary #784900, secondary #A56312, beige #E7E0CE. Poppins for UI text, Yathra One for Hindi.

---

## 3. Final test results

| Test | Result |
|---|---|
| Overflow at 7 widths × 72 pages (504 page views) | 0 failures |
| Text contrast, WCAG AA (390 and 1440 px, including gradients) | 0 failures |
| One h1 per page / heading skips | 72/72 pages / 0 skips |
| Unnamed controls, missing alt text, missing canonical | 0 |
| Broken internal links or anchors, dead `#` links | 0 |
| Duplicate page titles | 0 |
| JavaScript errors during journeys | 0 |
| Journeys A–E (39 checks) | 39/39 passed |

**Journey checks**
- **A. Home → category → product → cart:** size switch, add to cart, variant ID stored, checkout link built.
- **B. Search → results → product → cart:** predictive search, keyword search, empty state, Enter key to results, category and pack filters together.
- **C. Product → lab report → back:** the Know Your Food selector renders and the unit table is present.
- **D. Membership → benefits → terms:**
  - featured card and final band are visible
  - terms anchor works
  - price, duration and exclusions are present
  - no dead links
- **E. Mobile (390 px):**
  - burger menu and drawer link
  - add to cart and checkout handoff
  - PIN check rejects bad input and gives an honest message
  - no overflow

Re-run the tests with `qa.py --full` and `journeys.py`. Ask for the scripts if your developer wants them in the repo.

---

## 4. Claims review (nothing invented)
- Unverifiable figures stay removed: the unlabelled counter, "verified" badges and "save ₹X" plan badges.
- "Perks worth ₹3000+" and the membership benefits come from the owner's own membership design. Rosier should confirm them.
- The Diwali Sale announcement copies the live site. **Remove it when the sale ends.**
- Review counts, ratings, testimonials, FSSAI numbers, policies and prices were all taken from rosierfoods.com.

---

## 5. Missing backend integrations / owner actions
1. **Checkout:** test the cart link with one real order on rosierfoods.com. The Shopify store must allow cart permalinks.
2. **Membership join link:** set `JOIN_URL` in `source/data.py` to the membership product link. It currently goes to the account page.
3. **PIN serviceability:** needs a courier API (e.g. Shiprocket) for a true yes/no. It currently checks the format only.
4. **Reviews:** connect Judge.me (or another reviews app) so every product shows on-page reviews.
5. **Newsletter and contact forms:** connect Shopify Customer, Klaviyo or a form service. They currently only validate in the browser.
6. **Account, login and order tracking:** handled by Shopify. The site links out.
7. **Lab reports:** add the lab name and test date for each report. The reports are scanned images, so these couldn't be read automatically.
8. **Farmer profiles:** names, villages, photos and consent.
9. **Founder:** approved portrait and a quote in his own words.
10. **Membership terms:** whether the discount stacks, hamper exclusions, auto-renewal, and whether the fee is refundable.
11. **Nutrition tables:** per-product nutrition facts in text form.
12. **Batch traceability:** batch-level data from production.
13. **Real-device testing:** Core Web Vitals (Lighthouse or PageSpeed on the live URL) and a screen-reader pass (NVDA or VoiceOver).

---

## 6. Files changed in this QA pass (`source/`)

**Build and data**
- `build.py`
  - new nav, footer and head template
  - image performance pass
  - sitemap and robots
  - `product.html` redirect
  - search keywords
- `data.py`: variant IDs, new collections, keywords, membership plans, `JOIN_URL`, Shop-by-Need labels

**Styles**
- `css/base.css`: brand colour tokens
- `css/bharat.css`: removed the rule that hid dark backgrounds
- `css/site.css`, `css/live.css`: removed green colours
- `css/qa.css` (new): visibility, components, responsive fixes, focus styles

**Scripts**
- `js/commerce.js`:
  - variant IDs and checkout links
  - keyword search and empty states
  - category filter and `?q=` results
  - PIN check
  - Know Your Food selector
- `js/site.js`: drawer accessibility, form validation, variant state

**Pages**
- `pages/01_home.py`: 14-section homepage
- `pages/02_shop.py`: category filter, empty state, heading levels
- `pages/02b_collections.py`: honey and nut-butter banners
- `pages/03_product.py`: PIN check, FAQs, nutrition, variant IDs, reviews link, no duplicate page
- `pages/04b_standards.py`: Know Your Food selector
- `pages/04c_story_pages.py` (new): founder, farmers, process, philosophy, commitment, FAQ, 404
- `pages/05_lab.py`, `pages/07_contact.py`, `pages/08_cart.py`: links, headings, checkout
- `pages/09_membership.py`: terms section, working links, softened FAQ answers

---

# Addendum: homepage rebuilt on the live-site layout, with editable banners

## What changed
- **Header (every page):**
  - offer ticker with several messages
  - nav: Home, Shop (mega menu), Our Story (dropdown), Lab Reports, Hampers, Benefit Club
  - logo in the centre
  - search, account and cart on the right
  - trust strip: lab reports, traditional processing, delivery across India, secure checkout
- Below 1280 px the search box becomes an icon that opens it. Below 1200 px the nav moves into the menu drawer.
- **Hero carousel** (`config/banners.js`) uses the live banners and links:
  - Diwali Sale, going to Shop
  - Celebrate Diwali hampers, going to Hampers
  - each banner has separate desktop (3:1) and mobile (4:3) images
- **Discovery block** (`config/homepage.js`):
  - two promo tiles (Diwali Hampers, Gond Laddoo), each with its own link
  - category carousel: A2 Ghee, Oils, Atta & Grains, Pickles, Breakfast, Honey, Nut Butter, Immunity, Hampers, using the live site's category images
- **Section order:** Bestsellers (5) → Shop by Need (excludes the 5 bestsellers) → Our Standards → Explore our products (every category, in tabs) → Product in Focus → Traditional Process (photos + video) → Customer Stories → Our Story → Rosier Parivaar → Recipes & Knowledge → Footer.

## New components and files
- `config/banners.js`, `config/homepage.js`, `config/README.md` (editing guide)
- `js/render.js`: ticker, banner carousel, promo tiles, category carousel. It renders from config at page load.
- `css/home.css`: header, ticker, carousel, discovery, bestsellers, explore tabs, Our Story
- `source/build.py`: new header and nav, config loader. A rebuild never overwrites `config/`.
- `source/pages/01_home.py`: new homepage
- `js/site.js`: search icon toggle

## Acceptance tests (all passed)
- **Banner and category tests:** 42/42.
  - autoplay at about 5 s
  - pauses on hover, in a hidden tab and when the keyboard is inside it
  - arrows, dots, keyboard arrows and swipe all work
  - only the first banner loads up front, with high priority
  - mobile uses the mobile image
  - 3:1 and 4:3 boxes, so images are not stretched
  - CTA and banner clicks work
  - editing the config works for: `active:false`, start/end dates, `order`, image/link/CTA changes, and a single banner (no autoplay)
  - reduced motion turns off autoplay and the ticker scroll
  - the ticker shows all 4 messages
  - each promo tile has its own destination
  - all 9 categories open the right page
  - category arrows and mobile swipe work
  - the search icon opens search with suggestions
  - no JS errors
- **Journeys A–E:** 39/39, covering search, filters, cart, checkout handoff, product page, lab reports, membership and mobile nav.
- **Full sweep:** 72 pages × 7 widths, 0 issues. That covers overflow, contrast, headings, alt text, link names, canonicals, links and duplicate titles.
- **Header spacing:** checked at 360–1920 px. Nothing overlaps the logo.

## Limits of this pass
- The test machine can't load Shopify images. Layout and cropping were tested with placeholder images of the exact same sizes. The real banner, promo and category URLs were confirmed loading, with the right sizes, in your browser on rosierfoods.com.
- **Do a final look on the deployed GitHub Pages URL.**
- The homepage h1 ("Rosier Foods: Reviving the Tradition of Old Bharat…") is for screen readers only, because the visible headline is part of the banner artwork.
- Live offer copy (the Diwali Sale, freebie tiers) comes from rosierfoods.com. Turn it off in `config/` when the sale ends, and update the FAQ Offers answers.
