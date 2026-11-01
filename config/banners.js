/* ============================================================================
   ROSIER HOMEPAGE BANNERS  (edit this file to change the hero carousel)
   ----------------------------------------------------------------------------
   No rebuild needed: edit, commit to GitHub, and the homepage updates.
   Full guide: config/README.md

   RULES (the file is JSON inside a JS wrapper):
     - keep "double quotes" around every key and text value
     - no comma after the last item in a list or object
     - dates are "YYYY-MM-DD" (India time on the visitor's device);
       leave "" for no start / no end
   QUICK ACTIONS:
     - hide a banner ............ set "active": false
     - change the order ......... change "order" (1 shows first)
     - schedule a banner ........ set "start" and/or "end"
     - replace an image ......... paste the new URL into "desktop.src" / "mobile.src"
       (Shopify: Content > Files > copy link). Recommended sizes:
       desktop 3000 x 1000 (3:1), mobile 1600 x 1200 (4:3), WebP or PNG.
       If you change the shape of all banners, change "desktopRatio"/"mobileRatio".
   ========================================================================== */
window.ROSIER_BANNERS = {
  "settings": {
    "intervalMs": 5000,
    "desktopRatio": "3 / 1",
    "mobileRatio": "4 / 3",
    "mobileBreakpoint": 767
  },
  "banners": [
    {
      "id": "diwali-sale-2026",
      "active": true,
      "order": 1,
      "start": "",
      "end": "",
      "desktop": { "src": "https://www.rosierfoods.com/cdn/shop/files/diwali1_web-banner.png?format=webp&v=1793470352", "width": 3000, "height": 1000 },
      "mobile": { "src": "https://www.rosierfoods.com/cdn/shop/files/diwali1_mob-banner.png?format=webp&v=1793470337", "width": 1600, "height": 1200 },
      "alt": "Biggest Diwali Sale: up to 30% off, with exclusive freebies on orders above ₹2,499. Rosier A2 Bilona Ghee and Raw Wild Forest Honey.",
      "headline": "Biggest Diwali Sale",
      "subheading": "Up to 30% off on Rosier staples",
      "offer": "Exclusive freebies on orders above ₹2,499",
      "ctaLabel": "Shop the sale",
      "href": "shop.html",
      "showText": false,
      "showButton": true,
      "ctaX": "38.5%",
      "ctaY": "3.5%",
      "position": "center"
    },
    {
      "id": "diwali-hampers-2026",
      "active": true,
      "order": 2,
      "start": "",
      "end": "",
      "desktop": { "src": "https://www.rosierfoods.com/cdn/shop/files/home_1.png?format=webp&v=1792714396", "width": 2170, "height": 725 },
      "mobile": { "src": "https://www.rosierfoods.com/cdn/shop/files/home_mob_1.png?format=webp&v=1792714423", "width": 1448, "height": 1086 },
      "alt": "Celebrate Diwali with Rosier: Parampara gift hampers with ghee, honey, oil and festive treats.",
      "headline": "Celebrate Diwali with Rosier",
      "subheading": "Make every celebration more special",
      "offer": "",
      "ctaLabel": "Shop Diwali hampers",
      "href": "hampers.html",
      "showText": false,
      "showButton": false,
      "position": "center"
    }
  ]
};
