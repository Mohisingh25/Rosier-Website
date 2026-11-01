# Live rosierfoods.com data (snapshot 1 Nov 2026). Images hotlinked from the Shopify CDN.
C = 'https://cdn.shopify.com/s/files/1/0653/2605/5654/files/'
S = 'https://www.rosierfoods.com/cdn/shop/files/'
SITE = 'https://www.rosierfoods.com'


def img(path, w=700):
    sep = '&' if '?' in path else '?'
    base = path if path.startswith('http') else C + path
    return f'{base}{sep}width={w}'


# handle, title, size, price, mrp, rating, badge, img1, img2
PRODUCTS = [
    ('a2-desi-cow-ghee-hand-churned-from-curd', 'A2 Ghee – Hand Churned Gir Cow Bilona Ghee', '250 ml', 594.15, 699, 4.9, 'Best Seller',
     'rosier-foods-ghee-250-ml-gir-cow-a2-ghee-made-from-curd-1261568460.webp?v=1791458799', 'rosier-foods-ghee-250-ml-gir-cow-a2-ghee-made-from-curd-250-ml-1240619455.jpg?v=1779888192'),
    ('amlaprash', 'Amlaprash (Chyawanprash)', '500 g', 494.25, 659, 4.9, 'Selling Fast',
     'rosier-foods-amlaprash-amlaprash-chyawanprash-1261568414.webp?v=1791458595', 'rosier-foods-amlaprash-500g-amlaprash-chyawanprash-1238506732.jpg?v=1778844311'),
    ('wild-flower-honey', 'Wild Forest Honey', '500 g', 441.75, 589, 4.7, 'Trending',
     'rosier-foods-honey-500g-wild-forest-honey-1261568412.webp?v=1791459039', 'rosier-foods-honey-500g-wild-forest-honey-1238550349.jpg?v=1778873413'),
    ('wood-pressed-black-mustard-oil', 'Stone Pressed Black Mustard Oil', '1 L PET bottle', 312.00, 390, 4.9, 'Trending',
     'rosier-foods-oil-1000-ml-pet-bottle-stone-pressed-black-mustard-oil-1261568418.webp?v=1791458951', 'rosier-foods-oil-1000-ml-pet-bottle-stone-pressed-black-mustard-oil-1238506731.jpg?v=1778844370'),
    ('khapli-emmer-wheat-atta-stoneground-high-fiber-for-gut-health', 'Khapli (Emmer) Wheat Atta', '2 kg', 399.20, 499, 4.7, 'Must Try',
     S + 'rosier-foods-flour-khapli-emmer-wheat-atta-1261568450.webp?v=1791458379', S + 'rosier-foods-flour-2-kg-khapli-emmer-wheat-atta-1239446981.jpg?v=1779283597'),
    ('mango-pickle', 'Mango Pickle – Natural Sun Dried', '300 g', 279.20, 349, 4.8, 'Summer Special',
     'rosier-foods-pickle-300-gms-mango-pickle-natural-sun-dried-1261568448.webp?v=1791458138', 'rosier-foods-pickle-300-gms-mango-pickle-natural-sun-dried-1239710636.jpg?v=1779377171'),
    ('groundnut-oil', 'Stone Pressed Groundnut Oil', '1 L PET bottle', 356.00, 445, 4.9, 'Trending',
     'rosier-foods-oil-stone-pressed-groundnut-oil-1261568423.webp?v=1791459011', 'rosier-foods-oil-1000-ml-pet-bottle-stone-pressed-groundnut-oil-1238550351.jpg?v=1778873379'),
    ('wood-pressed-coconut-oil', 'Stone Pressed Coconut Oil', '1 L PET bottle', 719.20, 899, 4.9, '',
     'rosier-foods-oil-1000-ml-pet-bottle-stone-pressed-coconut-oil-1261568420.webp?v=1791458889', 'rosier-foods-ghee-1-ltr-a2-ghee-1-ltr-coconut-oil-vrat-wellness-pack-1227543448.jpg?v=1773775898'),
    ('gond-laddoo', 'Gond Laddoo', '200 g', 297.50, 350, 4.9, 'Diwali Special',
     S + 'rosier-foods-gond-laddoo-1261584794.png?v=1791472539', S + 'rosier-foods-gond-laddoo-1261584802.png?v=1791472511'),
    ('bajra-atta', 'Bajra Atta', 'Pack of 2 (500 g)', 190.00, 200, 0, 'Diwali Special',
     'rosier-foods-flour-pack-of-2-500g-bajra-atta-1264002449.png?v=1792681991', 'rosier-foods-flour-pack-of-2-500g-bajra-atta-1263995283.png?v=1792674998'),
    ('multigrain-atta-5kg', 'Khapli Multigrain Atta (5 kg)', '5 kg', 636.00, 795, 4.9, 'New Arrival',
     'rosier-foods-flour-5-kg-khapli-multigrain-atta-5kg-1261568438.webp?v=1791458053', 'rosier-foods-flour-5-kg-khapli-multigrain-atta-5kg-1239446984.jpg?v=1779283511'),
    ('red-chilly-pickle-natural-sun-dried', 'Red Chilly Pickle – Natural Sun Dried', '300 g', 279.20, 349, 4.9, 'New Arrival',
     'rosier-foods-pickle-300-gms-red-chilly-pickle-natural-sun-dried-1261568424.webp?v=1791465459', 'rosier-foods-pickle-300-gms-red-chilly-pickle-natural-sun-dried-1239710632.jpg?v=1779377051'),
    ('stone-pressed-olive-oil', 'Olive Oil', '500 ml', 792.00, 990, 4.6, 'New Arrival',
     'rosier-foods-oil-500-ml-olive-oil-1261568449.webp?v=1791465431', 'rosier-foods-oil-500-ml-stone-pressed-olive-oil-1238550345.jpg?v=1778873051'),
    ('sattu-atta-1kg', 'Sattu Atta (1 kg)', '1 kg', 232.00, 290, 5.0, 'New Arrival',
     'rosier-foods-flour-1-kg-sattu-atta-1kg-1261568456.webp?v=1791465519', 'rosier-foods-flour-1-kg-sattu-atta-1kg-1239446979.jpg?v=1779283479'),
    ('high-protein-oats-assorted-pack', 'High Protein Oats – Assorted Pack', 'Pack of 5', 349.30, 499, 5.0, 'Trending',
     'rosier-foods-bars-nutbutters-pack-of-1-x-5-high-protein-oats-assorted-pack-1261693708.png?v=1791537373', 'rosier-foods-bars-nutbutters-pack-of-1-x-5-high-protein-oats-assorted-pack-1247998648.webp?v=1783416157'),
    ('ragi-atta-1kg', 'Ragi Atta (1 kg)', '1 kg', 168.00, 210, 4.9, 'New Arrival',
     'rosier-foods-flour-1-kg-ragi-atta-1kg-1261568413.webp?v=1791465492', 'rosier-foods-flour-1-kg-ragi-atta-1kg-1239446980.jpg?v=1779283451'),
    # ---- the rest of the collections
    ('jowar-atta-1kg', 'Jowar Atta (1 kg)', '1 kg', 140.00, 175, 5.0, 'New Arrival',
     'rosier-foods-flour-1-kg-jowar-atta-1kg-1261989144.png?v=1791616900', 'rosier-foods-flour-1-kg-jowar-atta-1kg-1231498773.jpg?v=1775641029'),
    ('khapli-emmer-wheat-atta-5kg', 'Khapli Wheat Atta (5 kg)', '5 kg', 899.25, 1199, 4.7, 'Diwali Special',
     'rosier-foods-flour-5-kg-khapli-wheat-atta-5kg-1261568455.webp?v=1791458290', 'rosier-foods-flour-5-kg-khapli-emmer-wheat-atta-1239446982.jpg?v=1779283570'),
    ('high-protein-oats-cafe-latte', 'High Protein Oats – Cafe Latte', 'Pack of 6', 419.30, 599, 5.0, 'New Arrival',
     'rosier-foods-oats-pack-of-1-x-6-high-protein-oats-cafe-latte-1261568431.webp?v=1791465312', 'rosier-foods-oats-pack-of-1-x-6-high-protein-oats-cafe-latte-1259548067.webp?v=1790075801'),
    ('high-protein-oats-mango-tango', 'High Protein Oats – Mango Tango', 'Pack of 6', 419.30, 599, 5.0, 'New Arrival',
     'rosier-foods-oats-pack-of-1-x-6-high-protein-oats-mango-tango-1261568415.webp?v=1791465399', 'rosier-foods-oats-pack-of-1-x-6-high-protein-oats-mango-tango-1248483154.jpg?v=1783696838'),
    ('high-protein-oats-kulfi-masti', 'High Protein Oats – Kulfi Masti', 'Pack of 6', 419.30, 599, 5.0, 'New Arrival',
     'rosier-foods-oats-pack-of-1-x-6-high-protein-oats-kulfi-masti-1261568416.webp?v=1791465370', 'rosier-foods-oats-pack-of-1-x-6-high-protein-oats-kulfi-masti-1248483153.jpg?v=1783696812'),
    ('instant-oats-oats-double-chocolate', 'High Protein Oats – Double Chocolate', 'Pack of 6', 419.30, 599, 5.0, 'New Arrival',
     'rosier-foods-oats-pack-of-1-x-6-high-protein-oats-double-chocolate-1261568422.webp?v=1791458170', 'rosier-foods-oats-pack-of-1-x-6-high-protein-oats-double-chocolate-1259488073.png?v=1790010911'),
    ('instant-oats-cafe-mocha', 'High Protein Oats – Cafe Mocha', 'Pack of 6', 419.30, 599, 5.0, 'New Arrival',
     'rosier-foods-oats-pack-of-1-x-6-high-protein-oats-cafe-mocha-1261568426.webp?v=1791458232', 'rosier-foods-bars-nutbutters-pack-of-1-x-6-high-protein-oats-cafe-mocha-1240688427.jpg?v=1779909857'),
    ('instant-oats-banana-cinnamon', 'High Protein Oats – Banana Cinnamon', 'Pack of 6', 419.30, 599, 4.7, 'New Arrival',
     'rosier-foods-oats-pack-of-1-x-6-high-protein-oats-banana-cinnamon-1261568457.webp?v=1791458200', 'rosier-foods-bars-nutbutters-pack-of-1-x-6-high-protein-oats-banana-cinnamon-1240688428.jpg?v=1779909819'),
    ('nut-butter-dark-chocolate', 'Nut Butter Dark Chocolate', '300 g', 287.00, 410, 4.9, 'Must Try',
     'rosier-foods-bars-nutbutters-300g-nut-butter-dark-chocolate-1261568437.webp?v=1791458531', 'rosier-foods-bars-nutbutters-300g-nut-butter-dark-chocolate-1253320250.webp?v=1786036870'),
    ('almond-butter-crunchy', 'Almond Butter Crunchy', '300 g', 371.00, 530, 4.8, '',
     'rosier-foods-bars-nutbutters-300g-almond-butter-crunchy-1261568427.webp?v=1791458500', 'rosier-foods-bars-nutbutters-300g-almond-butter-crunchy-1253320251.webp?v=1786036813'),
    ('nut-butter-crunchy', 'Nut Butter Crunchy', '300 g', 258.30, 369, 4.8, '',
     'rosier-foods-bars-nutbutters-300g-nut-butter-crunchy-1261568440.webp?v=1791458471', 'rosier-foods-bars-nutbutters-300g-nut-butter-crunchy-1253320253.webp?v=1786036750'),
    ('nut-butter', 'Nut Butter (Creamy)', '300 g', 258.30, 369, 4.8, '',
     'rosier-foods-bars-nutbutters-300g-nut-butter-creamy-1261568443.webp?v=1791458557', 'rosier-foods-bars-nutbutters-300g-nut-butter-1253320249.webp?v=1786036931'),
    ('pickle-tasting-set', 'Pickle Tasting Set', 'Pack of 5 (100 g each)', 519.20, 649, 5.0, '',
     'rosier-foods-pickle-pack-of-5-100-gms-pickle-tasting-set-1261568433.webp?v=1791465340', 'rosier-foods-pickle-pack-of-5-100-gms-pickle-tasting-set-1256801484.png?v=1788362318'),
    ('sweet-lemon-pickle', 'Sweet Lemon Pickle – Natural Sun Dried', '300 g', 279.20, 349, 4.9, 'New Arrival',
     'rosier-foods-pickle-300-gms-sweet-lemon-pickle-natural-sun-dried-1261559549.webp?v=1791451178', 'rosier-foods-pickle-300-gms-sweet-lemon-pickle-natural-sun-dried-1239710634.jpg?v=1779377111'),
    ('green-chilly-pickle', 'Green Chilly Pickle – Natural Sun Dried', '300 g', 279.20, 349, 4.9, 'New Arrival',
     'rosier-foods-pickle-300-gms-green-chilly-pickle-natural-sun-dried-1261568441.webp?v=1791458080', 'rosier-foods-pickle-300-gms-green-chilly-pickle-natural-sun-dried-1239710633.jpg?v=1779377079'),
    ('lemon-pickle', 'Lemon Pickle – Natural Sun Dried', '300 g', 279.20, 349, 4.6, 'New Arrival',
     'rosier-foods-pickle-300-gms-lemon-pickle-natural-sun-dried-1261568454.webp?v=1791458112', 'rosier-foods-pickle-300-gms-lemon-pickle-natural-sun-dried-1239710635.jpg?v=1779377138'),
    ('mango-pickle-natural-sun-dried-pack-of-2', 'Mango Pickle (Pack of 2)', '2 × 300 g', 523.50, 698, 0, '',
     'rosier-foods-pickle-pack-of-2-300-gms-mango-pickle-natural-sun-dried-pack-of-2-1261693707.png?v=1791537249', 'rosier-foods-pickle-pack-of-2-300-gms-mango-pickle-natural-sun-dried-pack-of-2-1255765839.png?v=1787671032'),
    ('sweet-lemon-pickle-natural-sun-dried-pack-of-2', 'Sweet Lemon Pickle (Pack of 2)', '2 × 300 g', 523.50, 698, 0, '',
     'rosier-foods-pickle-pack-of-2-300-gms-sweet-lemon-pickle-natural-sun-dried-pack-of-2-1261693703.png?v=1791537277', 'rosier-foods-pickle-pack-of-2-300-gms-sweet-lemon-pickle-natural-sun-dried-pack-of-2-1255765840.png?v=1787671059'),
    ('green-chilly-pickle-natural-sun-dried-pack-of-2', 'Green Chilly Pickle (Pack of 2)', '2 × 300 g', 523.50, 698, 0, '',
     'rosier-foods-pickle-pack-of-2-300-gms-green-chilly-pickle-natural-sun-dried-pack-of-2-1261693710.png?v=1791537310', 'rosier-foods-pickle-pack-of-2-300-gms-green-chilly-pickle-natural-sun-dried-pack-of-2-1255765841.png?v=1787671093'),
    ('lemon-pickle-natural-sun-dried-pack-of-2', 'Lemon Pickle (Pack of 2)', '2 × 300 g', 523.50, 698, 0, '',
     'rosier-foods-pickle-pack-of-2-300-gms-lemon-pickle-natural-sun-dried-pack-of-2-1261693705.png?v=1791537339', 'rosier-foods-pickle-pack-of-5-100-gms-lemon-pickle-natural-sun-dried-pack-of-2-1255765842.png?v=1788353685'),
    ('stone-pressed-yellow-mustard-oil', 'Stone Pressed Yellow Mustard Oil', '1 L', 392.00, 490, 4.9, 'Trending',
     'rosier-foods-oil-stone-pressed-yellow-mustard-oil-1261568451.webp?v=1791458858', 'rosier-foods-oil-stone-pressed-yellow-mustard-oil-1253320259.webp?v=1786037109'),
    ('stone-pressed-sunflower-oil', 'Stone Pressed Sunflower Oil', '1 L PET bottle', 399.20, 499, 4.8, '',
     'rosier-foods-oil-stone-pressed-sunflower-oil-1261568447.webp?v=1791458437', 'rosier-foods-oil-stone-pressed-sunflower-oil-1238581626.jpg?v=1778923512'),
    ('stone-pressed-sesame-oil', 'Stone Pressed Sesame Oil', '1 L PET bottle', 599.20, 749, 4.9, '',
     'rosier-foods-oil-1000-ml-pet-bottle-stone-pressed-sesame-oil-1261568430.webp?v=1791458259', 'rosier-foods-oil-1000-ml-pet-bottle-stone-pressed-sesame-oil-1238581627.jpg?v=1778923451'),
    ('stone-pressed-black-mustard-oil-oil-5-ltr', 'Stone Pressed Black Mustard Oil 5 Ltr', '5 L tin', 1424.25, 1899, 4.9, 'Diwali Special',
     'rosier-foods-oil-5-l-tin-pack-stone-pressed-black-mustard-oil-1261568425.webp?v=1791458918', 'rosier-foods-oil-5-l-tin-pack-stone-pressed-black-mustard-oil-1238506730.jpg?v=1778844340'),
    ('stone-pressed-groundnut-oil-copy', 'Stone Pressed Groundnut Oil 5 Ltr', '5 L tin', 1574.25, 2099, 4.9, 'Diwali Special',
     'rosier-foods-oil-stone-pressed-groundnut-oil-1261568453.webp?v=1791458978', 'rosier-foods-oil-5-l-tin-pack-stone-pressed-groundnut-oil-1238550350.jpg?v=1778873352'),
    ('stone-pressed-yellow-mustard-oil-5l', 'Stone Pressed Yellow Mustard Oil 5 Ltr', '5 L tin', 1799.25, 2399, 4.9, '',
     'rosier-foods-oil-stone-pressed-yellow-mustard-oil-1261568442.webp?v=1791458829', 'rosier-foods-oil-stone-pressed-yellow-mustard-oil-1238581623.jpg?v=1778923537'),
    ('stone-pressed-sunflower-oil-5-ltr', 'Stone Pressed Sunflower Oil 5 Ltr', '5 L tin', 1871.25, 2495, 4.8, '',
     'rosier-foods-oil-stone-pressed-sunflower-oil-1261568452.webp?v=1791458409', 'rosier-foods-oil-stone-pressed-sunflower-oil-1238581625.jpg?v=1778923479'),
    ('stone-pressed-black-mustard-oil-oil-kit-5-ltr', 'Black Mustard Oil 5 Ltr + Oil Kit', '5 L tin + oil kit', 1574.25, 2099, 4.9, '',
     'rosier-foods-oil-5-l-tin-pack-oil-kit-stone-pressed-black-mustard-oil-1265413933.png?v=1793459590', 'rosier-foods-oil-5-l-tin-pack-oil-kit-stone-pressed-black-mustard-oil-with-oil-kit-5-ltr-1217826166.png?v=1769103576'),
    ('stone-pressed-groundnut-oil-oil-kit-5-ltr', 'Groundnut Oil 5 Ltr + Oil Kit', '5 L tin + oil kit', 1724.25, 2299, 4.9, '',
     'rosier-foods-oil-5-l-tin-pack-oil-kit-stone-pressed-groundnut-oil-1265413934.png?v=1793459617', 'rosier-foods-oil-5-l-tin-pack-oil-kit-stone-pressed-groundnut-oil-oil-kit-5-ltr-1217776999.png?v=1769081678'),
    ('stone-pressed-yellow-mustard-oil-kit-5-ltr', 'Yellow Mustard Oil 5 Ltr + Oil Kit', '5 L tin + oil kit', 1949.25, 2599, 4.9, '',
     'rosier-foods-oil-5-l-tin-pack-oil-kit-stone-pressed-yellow-mustard-oil-1265413931.png?v=1793459560', 'rosier-foods-oil-5-l-tin-pack-oil-kit-stone-pressed-yellow-mustard-oil-with-oil-kit-5-ltr-1217826155.png?v=1769103310'),
    ('stone-pressed-sunflower-oil-oil-kit-5-ltr', 'Sunflower Oil 5 Ltr + Oil Kit', '5 L tin + oil kit', 2021.25, 2695, 4.8, '',
     'rosier-foods-oil-5-l-tin-pack-oil-kit-stone-pressed-sunflower-oil-1265413932.png?v=1793459530', 'rosier-foods-oil-5-l-tin-pack-oil-kit-stone-pressed-sunflower-oil-with-oil-kit-5-ltr-1217826159.png?v=1769103429'),
    ('wild-forest-honey-pack-of-2', 'Wild Forest Honey (Pack of 2)', '2 × 500 g', 883.50, 1178, 4.7, '',
     'rosier-foods-honey-500gms-honey-pack-of-2-wild-forest-honey-pack-of-2-1224221815.jpg?v=1772127069', 'rosier-foods-honey-500g-wild-forest-honey-1248149128.webp?v=1783502591'),
]
BY = {p[0]: p for p in PRODUCTS}

BEST = ['a2-desi-cow-ghee-hand-churned-from-curd', 'amlaprash', 'wild-flower-honey', 'wood-pressed-black-mustard-oil',
        'khapli-emmer-wheat-atta-stoneground-high-fiber-for-gut-health', 'mango-pickle', 'groundnut-oil', 'wood-pressed-coconut-oil']
NEW = ['gond-laddoo', 'bajra-atta', 'multigrain-atta-5kg', 'red-chilly-pickle-natural-sun-dried', 'stone-pressed-olive-oil',
       'sattu-atta-1kg', 'high-protein-oats-assorted-pack', 'ragi-atta-1kg']

# key, title, tile image, short line, description, product handles (live collection order)
COLLECTIONS = [
    ('ghee', 'Gir Cow A2 Desi Ghee', S + 'Ghee_Icons.png?v=1781252536', 'Hand-churned bilona',
     'Pure desi ghee from free-grazing A2 Gir cows, made the Bilona way: slow-churned from curd, rich in vitamins A, E and K.',
     ['a2-desi-cow-ghee-hand-churned-from-curd']),
    ('stone-press-oil', 'Stone Pressed Oils', S + 'oils.webp?v=1779380714', 'Never refined',
     'Mustard, groundnut, coconut, sesame and more. Stone pressed, chemical-free and unrefined, with lab reports to back them.',
     ['wood-pressed-black-mustard-oil', 'groundnut-oil', 'stone-pressed-yellow-mustard-oil', 'stone-pressed-sunflower-oil', 'wood-pressed-coconut-oil',
      'stone-pressed-olive-oil', 'stone-pressed-sesame-oil', 'stone-pressed-black-mustard-oil-oil-5-ltr', 'stone-pressed-groundnut-oil-copy',
      'stone-pressed-yellow-mustard-oil-5l', 'stone-pressed-sunflower-oil-5-ltr', 'stone-pressed-black-mustard-oil-oil-kit-5-ltr',
      'stone-pressed-groundnut-oil-oil-kit-5-ltr', 'stone-pressed-yellow-mustard-oil-kit-5-ltr', 'stone-pressed-sunflower-oil-oil-kit-5-ltr']),
    ('pickles', 'Pickles', S + 'pickles.webp?v=1779380696', 'Sun-dried, ghar jaisa',
     'Sun-dried pickles made the way they are at home. Mango, lemon, sweet lemon, green chilly and red chilly.',
     ['pickle-tasting-set', 'mango-pickle', 'sweet-lemon-pickle', 'green-chilly-pickle', 'lemon-pickle', 'red-chilly-pickle-natural-sun-dried',
      'mango-pickle-natural-sun-dried-pack-of-2', 'sweet-lemon-pickle-natural-sun-dried-pack-of-2', 'green-chilly-pickle-natural-sun-dried-pack-of-2',
      'lemon-pickle-natural-sun-dried-pack-of-2']),
    ('atta', 'Atta', S + 'atta.webp?v=1779380667', 'Stone ground chakki atta',
     'Freshly milled, stone ground atta: Khapli, Multigrain, Ragi, Jowar, Sattu and Bajra.',
     ['khapli-emmer-wheat-atta-stoneground-high-fiber-for-gut-health', 'khapli-emmer-wheat-atta-5kg', 'bajra-atta', 'ragi-atta-1kg', 'sattu-atta-1kg',
      'multigrain-atta-5kg', 'jowar-atta-1kg']),
    ('healthy-snacking', 'Healthy Breakfast', S + 'healthy_breakfast.webp?v=1779380683', 'Oats & nut butters',
     'High protein oats, almond and nut butters. No added sugar, wholesome ingredients.',
     ['high-protein-oats-assorted-pack', 'high-protein-oats-cafe-latte', 'high-protein-oats-mango-tango', 'high-protein-oats-kulfi-masti',
      'instant-oats-oats-double-chocolate', 'instant-oats-cafe-mocha', 'instant-oats-banana-cinnamon', 'nut-butter-dark-chocolate',
      'almond-butter-crunchy', 'nut-butter-crunchy', 'nut-butter']),
    ('immunity-booster', 'Immunity Booster', S + 'immunity_bosters.webp?v=1779380728', 'Amlaprash, honey & more',
     'Amlaprash made with hand-picked amla and A2 Gir cow ghee, plus raw wild forest honey from Himalayan forests.',
     ['amlaprash', 'wild-flower-honey', 'wild-forest-honey-pack-of-2']),
]

HOME = dict(
    slides=[S + 'diwali1_web-banner.png?format=webp&v=1793470352', S + 'home_1.png?format=webp&v=1792714396'],
    promo=[(S + 'diwali-hamper_e4c5d6a9-d698-4f46-86b9-376b7cc87d70.png?v=1791548067', 'hampers.html', 'Diwali Hamper'),
           (S + 'laddoo_mini-b.png?v=1791490469', 'product-gond-laddoo', 'Gond Laddoo')],
    village=S + 'WhatsAppVideo2026-04-18at9.56.10PM-ezgif.com-crop.webp?v=1778905130',
    village2=S + 'freepik-website.webp?v=1778905482',
    family=S + 'gt_replace_sumit.png?format=webp&v=1790230514',
    family_bg=C + 'Group_5653.png?v=1775616484',
    texture=C + '834924_preview_1_1.png?v=1775581038',
    video='https://www.rosierfoods.com/cdn/shop/videos/c/vp/13efe994c55741f19f7d39d83b20da85/13efe994c55741f19f7d39d83b20da85.SD-480p-1.2Mbps-54311062.mp4?v=0',
    values=[S + 'im1_1.png?format=webp&v=1775622475', S + 'im2_1.png?format=webp&v=1775622447', S + 'im3_1.png?format=webp&v=1775622492', S + 'im4_1.png?format=webp&v=1775622461'],
    cow=S + 'img_5_1.png?format=webp&v=1775622506', farmer=S + 'im6_1.png?format=webp&v=1775622520',
    trust=[S + '2_5201fa2c-1458-4728-bf18-0d52e26b9e26.png?format=webp&v=1786969126', S + 'Untitled_design_3.png?format=webp&v=1786969242',
           S + '5_b0022af8-bb27-4e86-9e9b-f82755426fd1.png?format=webp&v=1786969172', S + '4_e22ec1e5-1966-425f-b208-827bf43a438b.png?format=webp&v=1786969187',
           S + '3_fa529f92-3a74-407d-8551-fbc96a0cc64e.png?format=webp&v=1786969198'],
    logo=S + 'black-logo-01_7f1cd910-121f-49c7-bdcf-248849cd14f5.webp',
    logo_green=S + 'Logo_Green.png?format=webp&v=1748263794',
    payments=S + 'Group_140989.png?format=webp&v=1748263798',
)

# testimonials (as on the live homepage)
TESTI = [
    ('Rich Tradition in Every Drop', 'Rosier Foods’ A2 Desi Cow Ghee brings the richness of tradition to my kitchen. Its pure taste elevates every dish beautifully.',
     'Sushmita', 'A2 Ghee – Hand Churned Gir Cow Bilona Ghee', S + '3_44261a12-59c7-42a0-826a-bba75b68d85c.jpg?format=webp&v=1753605850'),
    ('Pure Aroma, Authentic Taste!', 'A2 Desi Cow Ghee from Rosier Foods gives my cooking a rich, authentic flavor. The purity and aroma are unmatched—my family loves it!',
     'Ankush S.', 'A2 Ghee – Hand Churned Gir Cow Bilona Ghee', S + '1_1.jpg?format=webp&v=1753605837'),
    ('Old-school fuel. Real results.', 'Balancing endurance sports, a demanding IT career, and family life has taught me that food needs to do more than just fill the plate. A2 Bilona Desi Ghee supports my digestion, keeps my joints moving freely, and gives me steady, long-lasting energy.',
     'Sumit Suhag', 'A2 Ghee – Hand Churned Gir Cow Bilona Ghee', S + 'sumit_suhag.heic?format=webp&v=1769762816'),
    ('Healthy Choice for Everyday Meals!', 'Switching to Khapli Wheat Atta from Rosier Foods was the best choice for our health. It’s fresh, nutritious, and perfect for our daily meals!',
     'Alisha A.', 'Khapli (Emmer) Wheat Atta', S + '2_84e37763-a7b1-45ab-977a-ceb6899c8d8a.jpg?format=webp&v=1753605846'),
    ('Taste That Feels Like Home', 'Using A2 Desi Cow Ghee from Rosier Foods makes my meals comforting and flavorful. The quality and purity are simply outstanding.',
     'Himanshi S.', 'A2 Ghee – Hand Churned Gir Cow Bilona Ghee', S + '4_bcd971c9-ffda-4ef4-bfd5-c0d24d70019f.jpg?format=webp&v=1753605855'),
]

GHEE_GALLERY = [S + 'rosier-foods-ghee-250-ml-gir-cow-a2-ghee-made-from-curd-1261568460.webp?v=1791458799',
                S + 'rosier-foods-ghee-250-ml-gir-cow-a2-ghee-made-from-curd-250-ml-1240619455.jpg?v=1779888192'] + \
               [S + f'rosier-foods-ghee-gir-cow-a2-ghee-made-from-curd-12104086{n}.jpg?v=1769604150' for n in (87, 85, 84, 83)]

# ---- per-product lab report file (from the live Lab Reports page)
LABF = 'https://cdn.shopify.com/s/files/1/0653/2605/5654/files/'
_L = {
    'merged.pdf?v=1768202574': ['a2-desi-cow-ghee-hand-churned-from-curd'],
    'Amlaprash_Lab_Report.pdf?v=1765543072': ['amlaprash'],
    'Wild_Forest_Honey.pdf?v=1765369651': ['wild-flower-honey', 'wild-forest-honey-pack-of-2'],
    'Black_Mustard_Oil_Lab_Report.pdf?v=1765370195': ['wood-pressed-black-mustard-oil', 'stone-pressed-black-mustard-oil-oil-5-ltr', 'stone-pressed-black-mustard-oil-oil-kit-5-ltr'],
    'Groundnut_Oil_Lab_Report.pdf?v=1765370419': ['groundnut-oil', 'stone-pressed-groundnut-oil-copy', 'stone-pressed-groundnut-oil-oil-kit-5-ltr'],
    'Coconut_Oil_Lab_Report.pdf?v=1765370726': ['wood-pressed-coconut-oil'],
    'Yellow_Mustard_Oil_Lab_Report.pdf?v=1765371322': ['stone-pressed-yellow-mustard-oil', 'stone-pressed-yellow-mustard-oil-5l', 'stone-pressed-yellow-mustard-oil-kit-5-ltr'],
    'Sunflower_Oil-020.pdf?v=1765371422': ['stone-pressed-sunflower-oil', 'stone-pressed-sunflower-oil-5-ltr', 'stone-pressed-sunflower-oil-oil-kit-5-ltr'],
    'Olive_Oil-023.pdf?v=1788259531': ['stone-pressed-olive-oil'],
    'ROSIER_WHITE_SESAME20251001_15433420.pdf?v=1788259530': ['stone-pressed-sesame-oil'],
    'Khapli_Atta_Lab_Report.pdf?v=1765368662': ['khapli-emmer-wheat-atta-stoneground-high-fiber-for-gut-health', 'khapli-emmer-wheat-atta-5kg'],
    '200-Multigrain_flour_Atta.pdf?v=1776080054': ['multigrain-atta-5kg'],
    'Test_report_of_Sattu_-_206.pdf?v=1776080054': ['sattu-atta-1kg'],
    'Test_report_of_Jowar_Flour-202.pdf?v=1776080054': ['jowar-atta-1kg'],
    'Test_report_of_Ragi_Flour-201.pdf?v=1776080054': ['ragi-atta-1kg'],
    'fa20260212-027-114.pdf?v=1776513445': ['instant-oats-banana-cinnamon'],
    'fa20260212-027-115.pdf?v=1776513627': ['instant-oats-cafe-mocha'],
    'fa20260212-027-116.pdf?v=1776513712': ['instant-oats-oats-double-chocolate'],
    'High_Protein_Oats_-_Mango_-033.pdf?v=1788249684': ['high-protein-oats-mango-tango'],
    'Overnight_Oats_Kulfi_-079.pdf?v=1788249685': ['high-protein-oats-kulfi-masti'],
    'Nut_Butter_Lab_Report.jpg?v=1749047175': ['nut-butter'],
    'Nut_Butter_Crunchy_Lab_Report.jpg?v=1749047175': ['nut-butter-crunchy'],
    'Dark_Chocolate_Nut_Butter_Lab_Report.jpg?v=1749047175': ['nut-butter-dark-chocolate'],
    'Almond_Butter_Crunchy_Lab_Report.jpg?v=1749047175': ['almond-butter-crunchy'],
    'Mango_pickle.pdf?v=1788250646': ['mango-pickle', 'mango-pickle-natural-sun-dried-pack-of-2'],
    'Red_Chilli_pickle.pdf?v=1788249685': ['red-chilly-pickle-natural-sun-dried'],
    'green_chilli_pickle.pdf?v=1788259532': ['green-chilly-pickle', 'green-chilly-pickle-natural-sun-dried-pack-of-2'],
    '204-Nimbu_Masala_Pickle.pdf?v=1788266555': ['lemon-pickle', 'lemon-pickle-natural-sun-dried-pack-of-2'],
    'Sweet_lemon_Pickle.pdf?v=1788249685': ['sweet-lemon-pickle', 'sweet-lemon-pickle-natural-sun-dried-pack-of-2'],
}
LABMAP = {h: LABF + f for f, hs in _L.items() for h in hs}

# ---- Shop by need (each line is the brand's own wording from the live site)
NEEDS = [
    ('gut', 'Gut & digestion', 'Bilona ghee and high-fibre Khapli atta', ['a2-desi-cow-ghee-hand-churned-from-curd', 'khapli-emmer-wheat-atta-stoneground-high-fiber-for-gut-health', 'multigrain-atta-5kg', 'jowar-atta-1kg']),
    ('immunity', 'Immunity', 'Amlaprash and raw wild forest honey', ['amlaprash', 'wild-flower-honey', 'wild-forest-honey-pack-of-2', 'gond-laddoo']),
    ('protein', 'Protein breakfast', 'High protein oats and nut butters', ['high-protein-oats-assorted-pack', 'instant-oats-cafe-mocha', 'nut-butter-dark-chocolate', 'almond-butter-crunchy']),
    ('cooking', 'Everyday cooking', 'Stone pressed oils, never refined', ['wood-pressed-black-mustard-oil', 'groundnut-oil', 'stone-pressed-yellow-mustard-oil', 'wood-pressed-coconut-oil']),
    ('millets', 'Millets & heritage grains', 'Ragi, jowar, bajra and sattu', ['ragi-atta-1kg', 'jowar-atta-1kg', 'bajra-atta', 'sattu-atta-1kg']),
    ('taste', 'Ghar jaisa taste', 'Sun-dried pickles, made like home', ['pickle-tasting-set', 'mango-pickle', 'green-chilly-pickle', 'sweet-lemon-pickle']),
]

# ---- Real photography from rosierfoods.com (about page, ghee & product galleries, hampers)
PH = {
    'about_banner': S + '13_About_Page_Banner_811e2119-e31f-4746-992c-b97f3e40f149.jpg?v=1772123938',
    'unit': S + '1_0fe22cef-ad2a-4333-bf02-2ec3f1345b60.jpg?v=1753886632',          # Rosier building
    'churning': S + '2_bf13f74b-4ee2-48f9-a7b1-f0ac1bac7ebe.jpg?v=1753886646',      # women churning bilona
    'cows': S + '3_7aa179f6-294f-4abb-a377-4ef18a1abd37.jpg?v=1753886640',          # Gir cows
    'cow_sun': S + 'Untitled_design_25.png?v=1755009833',
    'family_table': S + 'rosier-foods-ghee-gir-cow-a2-ghee-made-from-curd-1210408680.jpg?v=1769604150',
    'tested': S + 'rosier-foods-ghee-gir-cow-a2-ghee-made-from-curd-1210408681.jpg?v=1769604150',
    'bilona_pot': S + 'rosier-foods-ghee-gir-cow-a2-ghee-made-from-curd-1210408682.jpg?v=1769604150',
    'vs_regular': S + 'rosier-foods-ghee-gir-cow-a2-ghee-made-from-curd-1210408683.jpg?v=1769604150',
    'ghee_spread': S + 'rosier-foods-ghee-gir-cow-a2-ghee-made-from-curd-1210408684.jpg?v=1769604150',
    'art_of_slow': S + 'rosier-foods-ghee-gir-cow-a2-ghee-made-from-curd-1210408685.jpg?v=1769604150',
    'farm_man': S + 'preview_images/f4467422ef4348379fe38c9ed776bda5.thumbnail.0000000000.jpg?v=1686659447',
    'ghee_pour': S + '1_60e7e21f-34ce-42b7-a0dc-bbe6f8039e20.jpg?v=1767372013',
    'ghee_nourish': S + '2_0dbce3a7-ca19-4ab9-b1dc-ede979e63ee2.jpg?v=1767372163',
    'amla_fruit': S + 'Amla_3_cdcd8874-ca6b-41b3-8dce-80f2a6a81caa.jpg?v=1769589581',
    'amla_founder': S + 'Amla_1_b2f88324-2aed-4af5-9ace-e75c1f0242e3.jpg?v=1769589628',
    'oil_process': S + 'B-3_fe9144b6-a0d8-4677-b9a3-9e9e3d399bd4.jpg?v=1768912768',
    'oil_range': S + 'B-7_8056f776-e0ad-4196-bc47-1e87f3e57668.jpg?v=1768912795',
    'oil_food': S + 'B-5_47b4fe6e-664c-4331-9366-b837aebb89f3.jpg?v=1768912782',
    'cooking_lady': S + 'B-6_b9948104-835c-44f7-be0b-d63aa84bb90c.jpg?v=1768912693',
    'oil_drop': S + 'B-1_db36c70e-c527-4944-9775-1988392b6bee.jpg?v=1768912722',
    'hamper_banner': S + 'hamper-banner_2.png?v=1790763320',
    'hamper_trad': S + 'rosier-foods-traditional-hamper-1260194553.png?v=1790615833',
    'hamper_life': S + '4_3.png?v=1790612550',
    'hamper_spread': S + 'rosier-foods-traditional-hamper-1261989145.png?v=1791616573',
    'hamper_gift': S + 'rosier-foods-lifestyle-hamper-1260378722.png?v=1790781340',
}
GHEE_GALLERY = GHEE_GALLERY[:2] + [PH['bilona_pot'], PH['vs_regular'], PH['art_of_slow'], PH['tested'], PH['ghee_spread'], PH['family_table']]

# ======================= Audit pass: verified facts =======================
CONTACT_EMAIL = 'care@rosierfoods.com'   # from the live Refund Policy
WHATSAPP = '919711580581'

# From rosierfoods.com/pages/manufacturer-list (batch-code letter = first two chars of batch no.)
MANUFACTURERS = [
    ('Rosier Foods Private Limited', 'G', '62, Udyog Vihar Phase 1, Gurugram, Haryana 122022', '10825005000070'),
    ('Rosier Foods Private Limited', 'B', 'Village Garwa, Near Canal Garwa, Morka Road, Garwa, Haryana', '10825002000003'),
    ('Rosier Foods Private Limited', 'M', 'Vill. Gesupur Janubi, Kithore, Mawana, Meerut, Uttar Pradesh', '12724051000040'),
    ('Rosier Foods Private Limited', 'S', 'Plot 4/66, Site-4, Industrial Area, Sahibabad, Ghaziabad, Uttar Pradesh 201010', '12726999000238'),
    ('Mapani Food Products', 'J', 'J-822, RIICO Industrial Area, Sitapura, Jaipur, Rajasthan 302022', '12221027000524'),
    ('Graminn Organik', 'N', 'Plot 21, Block-D, Durga Industrial Park, Sahibabad, Ghaziabad, Uttar Pradesh 201005', '12725999000482'),
]

# From the live Shipping & Refund policies (1 Nov 2026)
POLICY = dict(
    delivery='Standard shipping across India, usually delivered in 3–5 days depending on your location.',
    returns='Returns or exchanges within 2 days of delivery if the product is damaged, wrong, has a broken seal or arrived expired. It must be unused, in original packaging, with the invoice.',
    unboxing='Please record an unboxing video. Any order discrepancy must be reported within 48 hours of delivery with that video.',
    sale='Items bought during a sale or from the gifting category are not eligible for return or refund.',
    cancel='You can cancel any order that has not shipped yet, for a full refund.',
)

# Per-product facts, written from each product's own description on rosierfoods.com
INFO = {
    'ghee': dict(why=['Made from curd, not milk or malai', 'Slow-churned the traditional Bilona way', 'From free-grazing Gir cows'],
                 about='Our Gir Cow A2 Ghee comes from curd using the traditional Bilona method, slow-churned and never mass-produced.',
                 use='Stir it into dal, drizzle it on hot rice or use it for everyday cooking.', ing='A2 milk fat, natural yoghurt'),
    'amla': dict(why=['Made with A2 desi cow ghee', 'Sweetened with desi khand', 'Hand-picked amla'],
                 about='Our Amlaprash brings together amla, A2 desi cow ghee and desi khand, following a traditional Ayurvedic-style recipe.',
                 use='Take a spoonful daily, as a family ritual through the season.'),
    'honey': dict(why=['Multi-floral wild forest honey', 'Collected from the Himalayan forests', 'No added sugar'],
                  about='A multi-floral honey, responsibly collected from bees feeding on wild forest flower nectar in the Himalayas.',
                  use='In warm water, on toast, in desserts or as a natural sweetener.', ing='Raw honey', store='Keep in a cool, dry place with the lid tightly shut. Do not refrigerate.'),
    'oil': dict(why=['Stone cold pressed', 'No chemicals or solvents used', 'Unrefined'],
                about='Cold pressed and extracted without chemicals or solvents, so the natural flavour and aroma of the seed stay intact.',
                use='Everyday Indian cooking, tadka, sautéing and frying.'),
    'olive': dict(why=['Cold-processed with minimal heat', 'Traditional extraction', 'Made from high-quality olives'],
                  about='Crafted using traditional extraction methods and cold-processed to keep its authentic taste, aroma and flavour.',
                  use='Everyday cooking, drizzling and finishing dishes.'),
    'khapli': dict(why=['100% non-GMO Emmer (Khapli) wheat', 'Stone ground in a traditional chakki', 'A heritage grain'],
                   about='Milled from 100% non-GMO Emmer wheat, a heritage grain, and stone ground using the traditional chakki method.',
                   use='Rotis, parathas and everyday Indian breads.'),
    'multigrain': dict(why=['Built on 50% Khapli wheat', 'Blended with jowar, maize, barley, ragi and soy', 'No additives, no fillers'],
                       about='Built on Khapli wheat (50%) and blended with jowar, maize, barley, ragi and soy, stone-ground in traditional chakki style.',
                       use='Softer, more filling rotis for the whole family.'),
    'ragi': dict(why=['Finger millet flour', 'Stone-ground in traditional chakkis', 'Earthy, nutty taste'],
                 about='Our Ragi (finger millet) is stone-ground in traditional chakkis, a slow, cool grinding process that keeps the whole grain intact.',
                 use='Rotis, dosas, porridge and baking.'),
    'jowar': dict(why=['100% jowar', 'Stone-ground in traditional chakkis', 'Naturally gluten-free grain'],
                  about="Made from 100% jowar and stone-ground to retain the grain's natural fibre and character.",
                  use='Bhakri and rotis, as a lighter rotation alongside wheat.'),
    'sattu': dict(why=['Made from roasted Bengal gram', 'Stone-ground, chakki method', 'No elaborate prep needed'],
                  about='Made from roasted Bengal gram and stone-ground using traditional chakki methods.',
                  use='A quick sattu drink, parathas or a filling meal.'),
    'oats': dict(why=['High protein oats', 'Ready in about 30 seconds', 'Made for busy mornings'],
                 about="Prepared to give good protein and fibre support, and ready to eat on the go. It takes about 30 seconds to make.",
                 use='Breakfast at home, at work or on the go.'),
    'nutbutter': dict(why=['Almonds, peanuts and cashews', 'No unnecessary additives, fillers or preservatives', '27 g protein per 100 g (as per lab report)'],
                      about='A blend of almonds, peanuts and cashews, crafted without unnecessary additives, fillers or preservatives.',
                      use='On toast, in smoothies, with fruit or straight from the jar.'),
    'almond': dict(why=['Made with 100% roasted almonds', 'No added sugar or preservatives', 'Crunchy texture'],
                   about='Crafted from premium roasted almonds for a rich, nutty flavour and a crunch in every bite.',
                   use='On toast, smoothies, desserts or as a snack.', ing='Almonds'),
    'pickle': dict(why=['Naturally sun-dried', 'Traditional Indian spices', 'No added vinegar or preservatives'],
                   about='Made from farm-fresh produce, slow sun-dried and blended with traditional spices, the way homemade pickles are made.',
                   use='With parathas, dal-chawal, khichdi and every Indian meal.'),
    'pickle2': dict(why=['Natural sun-dried', 'Traditional Indian spices', 'Made the way pickles are made at home'],
                    about='A sun-dried pickle made with traditional Indian spices, for that homemade taste.',
                    use='With parathas, dal-chawal, khichdi and every Indian meal.'),
    'oats2': dict(why=['High protein oats', 'Made for busy mornings'],
                  about="Part of Rosier's High Protein Oats range, made so you never have to skip breakfast.",
                  use='Breakfast at home, at work or on the go.'),
    'oilbasic': dict(why=['Stone pressed', 'Unrefined', 'Lab report published'],
                     about='Stone pressed the traditional way, part of our range of unrefined cooking oils.',
                     use='Everyday Indian cooking.'),
    'generic': dict(why=['Traditional methods', 'No refined oils, no additives', 'Delivered across India'],
                    about="Part of Rosier Foods' range of pure, traditional foods.",
                    use=''),
}
def info_key(h):
    if h.startswith('a2-desi'): return 'ghee'
    if h == 'amlaprash': return 'amla'
    if 'honey' in h: return 'honey'
    if 'olive' in h: return 'olive'
    if 'sesame' in h: return 'oilbasic'
    if 'oil' in h: return 'oil'
    if 'khapli-emmer' in h: return 'khapli'
    if 'multigrain' in h: return 'multigrain'
    if 'ragi' in h: return 'ragi'
    if 'jowar' in h: return 'jowar'
    if 'sattu' in h: return 'sattu'
    if h in ('instant-oats-banana-cinnamon', 'instant-oats-cafe-mocha', 'instant-oats-oats-double-chocolate', 'high-protein-oats-mango-tango'): return 'oats'
    if 'oats' in h: return 'oats2'
    if 'almond' in h: return 'almond'
    if 'nut-butter' in h: return 'nutbutter'
    if h.startswith(('mango-pickle', 'green-chilly-pickle', 'red-chilly-pickle')): return 'pickle'
    if 'pickle' in h: return 'pickle2'
    return 'generic'

# Live variant lists (sold-out sizes shown as unavailable)
VARIANTS = {
    'amlaprash': [('500 g', 494.25, 659, 1), ('1000 g', 936.75, 1249, 0), ('350 g', 494.25, 659, 0)],
    'khapli-emmer-wheat-atta-stoneground-high-fiber-for-gut-health': [('2 kg', 399.20, 499, 1), ('5 kg', 899.25, 1199, 1)],
    'gond-laddoo': [('200 g', 297.50, 350, 1), ('500 g', 624.00, 780, 1)],
}

# Shop by need: plain, non-medical labels
NEEDS = [
    ('staples', 'Daily staples', 'Bilona ghee and stone-ground Khapli atta', ['a2-desi-cow-ghee-hand-churned-from-curd', 'khapli-emmer-wheat-atta-stoneground-high-fiber-for-gut-health', 'multigrain-atta-5kg', 'jowar-atta-1kg']),
    ('winter', 'Winter favourites', 'Amlaprash, raw honey and gond laddoo', ['amlaprash', 'wild-flower-honey', 'gond-laddoo', 'wild-forest-honey-pack-of-2']),
    ('protein', 'Protein breakfast', 'High protein oats and nut butters', ['high-protein-oats-assorted-pack', 'instant-oats-cafe-mocha', 'nut-butter-dark-chocolate', 'almond-butter-crunchy']),
    ('cooking', 'Everyday cooking', 'Stone pressed oils, never refined', ['wood-pressed-black-mustard-oil', 'groundnut-oil', 'stone-pressed-yellow-mustard-oil', 'wood-pressed-coconut-oil']),
    ('millets', 'Millets & heritage grains', 'Ragi, jowar, bajra and sattu', ['ragi-atta-1kg', 'jowar-atta-1kg', 'bajra-atta', 'sattu-atta-1kg']),
    ('taste', 'Ghar jaisa taste', 'Sun-dried pickles, made like home', ['pickle-tasting-set', 'mango-pickle', 'green-chilly-pickle', 'sweet-lemon-pickle']),
]

A = 'https://www.rosierfoods.com/cdn/shop/articles/'
GUIDES = [
    ('A2 Ghee vs Regular Ghee: What Is A2 Ghee and How Is It Different?', '/blogs/news/a2-ghee-vs-regular-ghee', A + 'blog-banner.png?format=webp&v=1790145891', 'Buying guide'),
    ("A1 vs A2 Ghee: What's the Primary Difference?", '/blogs/news/a1-vs-a2-ghee', A + 'blog-b1_68fea786-1e6c-4a35-b1d0-6cd62b6def6a.png?format=webp&v=1790594121', 'Buying guide'),
    ('Benefits of Khapli Atta: Why This Ancient Wheat Should Be in Your Kitchen', '/blogs/news/benefits-of-khapli-atta', A + 'blog_1.png?format=webp&v=1791274212', 'Ingredient guide'),
    ('Breaking Down Your Favourite Oil: What You Need to Know', '/blogs/news/black-mustard-oil-guide', A + 'oil_mustard_black_djwchudbc_jpg.jpg?format=webp&v=1792581835', 'Ingredient guide'),
    ('Gajar Ka Halwa', '/blogs/lets-cook/gajar-ka-halwa-1', A + 'GAJAR_KA_HALWA_b06f51df-ac70-42a0-bf12-61e8d4825e60.png?format=webp&v=1790243856', 'Recipe'),
    ('Eggless Ghee Cake', '/blogs/lets-cook/indian-tacos', A + 'eggless_ghee.png?format=webp&v=1712257622', 'Recipe'),
]
