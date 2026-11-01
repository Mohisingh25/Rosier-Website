/* ============================================================================
   ROSIER SITE CONTENT  (announcement ticker, homepage promo tiles, categories)
   ----------------------------------------------------------------------------
   No rebuild needed: edit, commit to GitHub, and the site updates.
   Full guide: config/README.md
   Same rules as banners.js: "double quotes", no trailing commas,
   dates "YYYY-MM-DD" or "".
   ========================================================================== */
window.ROSIER_SITE = {
  "announcements": [
    { "active": true, "text": "Diwali Sale is live: up to 30% off", "href": "shop.html", "start": "", "end": "" },
    { "active": true, "text": "Free bottle on orders of ₹2,499", "href": "faq.html#offers", "start": "", "end": "" },
    { "active": true, "text": "Free tumbler on orders of ₹4,999", "href": "faq.html#offers", "start": "", "end": "" },
    { "active": true, "text": "Free bottle & tumbler on orders of ₹7,999", "href": "faq.html#offers", "start": "", "end": "" }
  ],
  "promoTiles": [
    {
      "active": true,
      "title": "Diwali Hampers",
      "image": "https://www.rosierfoods.com/cdn/shop/files/diwali-hamper_e4c5d6a9-d698-4f46-86b9-376b7cc87d70.png?v=1791548067",
      "width": 800, "height": 436,
      "alt": "Rosier Diwali hamper with ghee, oil, honey and festive treats",
      "href": "hampers.html",
      "start": "", "end": ""
    },
    {
      "active": true,
      "title": "Ghar Jaisa Gond Laddoo",
      "image": "https://www.rosierfoods.com/cdn/shop/files/laddoo_mini-b.png?v=1791490469",
      "width": 800, "height": 439,
      "alt": "Diwali special: Ghar Jaisa Gond Laddoo made with A2 Bilona Ghee, no refined sugar",
      "href": "product-gond-laddoo.html",
      "start": "", "end": ""
    }
  ],
  "categories": [
    { "active": true, "name": "A2 Ghee", "note": "Bilona, from curd", "href": "collection-ghee.html", "image": "https://www.rosierfoods.com/cdn/shop/files/Ghee_Icons.png?v=1781252536" },
    { "active": true, "name": "Stone Pressed Oils", "note": "Mustard, groundnut & more", "href": "collection-stone-press-oil.html", "image": "https://www.rosierfoods.com/cdn/shop/files/oils.webp?v=1779380714" },
    { "active": true, "name": "Atta & Grains", "note": "Chakki-ground", "href": "collection-atta.html", "image": "https://www.rosierfoods.com/cdn/shop/files/atta.webp?v=1779380667" },
    { "active": true, "name": "Pickles", "note": "Sun-dried, ghar jaisa", "href": "collection-pickles.html", "image": "https://www.rosierfoods.com/cdn/shop/files/pickles.webp?v=1779380696" },
    { "active": true, "name": "Breakfast", "note": "High protein oats", "href": "collection-healthy-snacking.html", "image": "https://www.rosierfoods.com/cdn/shop/files/healthy_breakfast.webp?v=1779380683" },
    { "active": true, "name": "Honey", "note": "Raw wild forest", "href": "collection-honey.html", "image": "https://cdn.shopify.com/s/files/1/0653/2605/5654/files/rosier-foods-honey-500g-wild-forest-honey-1261568412.webp?v=1791459039" },
    { "active": true, "name": "Nut Butter", "note": "Peanut, almond & more", "href": "collection-nut-butters.html", "image": "https://cdn.shopify.com/s/files/1/0653/2605/5654/files/rosier-foods-bars-nutbutters-300g-nut-butter-dark-chocolate-1261568437.webp?v=1791458531" },
    { "active": true, "name": "Immunity", "note": "Amlaprash & more", "href": "collection-immunity-booster.html", "image": "https://www.rosierfoods.com/cdn/shop/files/immunity_bosters.webp?v=1779380728" },
    { "active": true, "name": "Hampers", "note": "Parampara gifting", "href": "hampers.html", "image": "https://www.rosierfoods.com/cdn/shop/files/diwali-hamper_e4c5d6a9-d698-4f46-86b9-376b7cc87d70.png?v=1791548067" }
  ]
};
