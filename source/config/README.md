# Changing banners, offers, promo tiles and categories

You can change everything on this page **without rebuilding the site**. Open the file on GitHub, click the pencil icon, edit it, then commit. GitHub Pages updates in about a minute. Hard-refresh the page to see the change.

| What you want to change | File |
|---|---|
| Homepage hero banners | `config/banners.js` |
| Offer ticker at the top of every page | `config/homepage.js` → `announcements` |
| The two promo tiles under the banner | `config/homepage.js` → `promoTiles` |
| The category carousel under the banner | `config/homepage.js` → `categories` |

## Golden rules (the files are JSON)
- Put every key and every text value in `"double quotes"`.
- Put a comma between items, but **no comma after the last item** in a list `[ ]` or an object `{ }`.
- Write dates as `"2026-11-15"`. Use `""` for "no date". A banner shows from the start of its start date until the end of its end date, in the visitor's own time zone.
- If you break the format, the banner area hides itself and the rest of the page still works. Open the browser console (F12) to see a `[Rosier config]` message, or paste the part after `=` into jsonlint.com to find the mistake.

---

## Hero banners: `config/banners.js`

```json
{
  "id": "diwali-sale-2026",          // any unique name
  "active": true,                    // false = hidden
  "order": 1,                        // 1 shows first
  "start": "", "end": "",           // optional schedule, e.g. "2026-11-01" / "2026-11-12"
  "desktop": { "src": "https://…/diwali1_web-banner.png", "width": 3000, "height": 1000 },
  "mobile":  { "src": "https://…/diwali1_mob-banner.png", "width": 1600, "height": 1200 },
  "alt": "Describe the banner, including the offer written on it",
  "headline": "Biggest Diwali Sale",
  "subheading": "Up to 30% off on Rosier staples",
  "offer": "Exclusive freebies on orders above ₹2,499",
  "ctaLabel": "Shop the sale",
  "href": "shop.html",               // where the banner and button go
  "showText": false,                 // true = draw headline/subheading/offer on top of the image
  "showButton": true,                // show the CTA button (desktop, 1200 px and wider)
  "ctaX": "38.5%", "ctaY": "3.5%",   // button position: centre-x, distance from bottom
  "position": "center"               // image focus if it ever needs cropping, e.g. "left center"
}
```
(The `//` notes above are for explanation only. Don't put them in the real file.)

**Add a banner:** copy a whole `{ … }` block, paste it after the last one with a comma between them, and give it a new `id` and `order`.
**Remove a banner:** delete its block, or just set `"active": false`.
**Reorder:** change the `order` numbers.
**Replace an image:** upload it in Shopify under Content → Files, copy the link, and paste it into `desktop.src` and/or `mobile.src`. Update `width` and `height` to match.
**Change the offer or link:** edit `alt`, `headline`, `offer`, `ctaLabel` or `href`.

**Image sizes:** desktop 3000 × 1000 (3:1), mobile 1600 × 1200 (4:3), in WebP or PNG. These match your current Shopify banners.
- If you switch every banner to a different shape (for example mobile 1080 × 1350, which is 4:5), change `"mobileRatio": "4 / 5"` in `settings`.
- Shopify CDN links are resized automatically for each screen, so you upload one large file.
- When the text is part of the image, keep `"showText": false`. Still fill in `headline`, `subheading` and `alt`, because screen readers and Google read them.

**Settings:**
- `intervalMs` is the autoplay speed (5000 = 5 seconds).
- The carousel pauses:
  - on hover
  - while the keyboard is inside it
  - when the browser tab is hidden
  - for visitors who prefer reduced motion
- With only one active banner, autoplay, arrows and dots switch off.

## Offer ticker: `config/homepage.js` → `announcements`
```json
{ "active": true, "text": "Free bottle on orders of ₹2,499", "href": "faq.html#offers", "start": "", "end": "" }
```
- Add, remove or reorder lines.
- With one active message the ticker stays still. With several it scrolls, and pauses on hover.
- When an offer ends, set `"active": false` or give it an `end` date. Also update the Offers answers in the FAQ: those live in `source/pages/04c_story_pages.py` and need a rebuild.

## Promo tiles: `promoTiles`
Two tiles look best. Each tile has its own `image`, `alt`, `href` and optional `start`/`end`. Images are 800 × 436.

## Category carousel: `categories`
```json
{ "active": true, "name": "Honey", "note": "Raw wild forest", "href": "collection-honey.html", "image": "https://…/honey.webp" }
```
- Square images (300 × 300 or larger) look best.
- The order in the file is the order on the page.

### Adding a brand-new category page
1. In `source/data.py`, add the collection to `COLLECTIONS` with its product handles. Copy an existing entry.
2. In `source/pages/02b_collections.py`, add a banner image for it in the `CB` dictionary.
3. Rebuild: run `python3 build.py` inside `source/`. This creates `collection-<key>.html` and adds it to the Shop menu and the "Explore our products" tabs.
4. Add a card for it to `categories` in `config/homepage.js`, with `"href": "collection-<key>.html"`.

A rebuild never overwrites the files in `config/`. Your live edits are safe. `source/config/` is only a starting template.
