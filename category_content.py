"""Category-specific content for the 6 generic pitch deck templates.

Each category dict contains:
- label: display name
- competitors_global: slide 3 left column — (bold_name, description) tuples
- competitors_india: slide 3 right column
- text_swaps: dict of slide_index -> [(old, new), ...] for slides 4, 5, 8, 12
- slide10_offerings: list of {title_match, desc_match, title, desc}
- comparison_examples: dict of row_index -> query string for slide 13
- graph_definition: dict for the knowledge graph image generator (slide 11)
"""

# ---------------------------------------------------------------------------
# Clothing
# ---------------------------------------------------------------------------
# The master template already defaults to fashion, so most text stays as-is.
# We only genericize the competitor lists and fine-tune a couple of examples.

CLOTHING = {
    "label": "Clothing",
    "competitors_global": [
        (
            "Amazon Rufus",
            " — 250M shoppers, +$10B downstream sales, 60% higher "
            "purchase likelihood.",
        ),
        (
            "H&M",
            " — 18% conversion lift, 12% cart abandonment drop with "
            "conversational AI.",
        ),
        (
            "ASOS",
            " — AI stylist trained on 100K+ outfits for personalised "
            "fashion discovery.",
        ),
        (
            "Zalando",
            " — 18% YoY profitability lift partly credited to its "
            "conversational shopping assistant.",
        ),
        (
            "Klarna",
            " — AI shopping assistant across 5.6M+ products, live on "
            "ChatGPT.",
        ),
    ],
    "competitors_india": [
        (
            "Myntra (Maya / MyFashionGPT)",
            " — in-app conversational stylist, users 3x more likely to "
            "purchase.",
        ),
        (
            "Meesho (Vaani)",
            " — 1.5M users, 22% higher conversion, lower returns on "
            "the AI assistant.",
        ),
        (
            "Nykaa Fashion",
            " — rolling out AI-led discovery and style recommendations "
            "across the marketplace.",
        ),
        (
            "Flipkart",
            " — generative-AI product search integrated into the "
            "fashion storefront.",
        ),
        (
            "Ajio, Tata CLiQ",
            " — visual search and AI recommendations across fashion "
            "storefronts.",
        ),
    ],
    "text_swaps": {
        3: [
            (
                "“I need an outfit under 20000 for myself, size medium, "
                "for my sister’s beach wedding, I like sequins”",
                "“I need an outfit for myself, size medium, "
                "for my sister’s beach wedding, I like sequins, "
                "within budget”",
            ),
        ],
        4: [
            ("in the next slide", "on slide 11"),
            ('"16GM RAM"', '"cotton kurta"'),
        ],
        7: [
            ('"plan my meals"', '"complete look for a festive season"'),
        ],
    },
    "slide10_offerings": [
        {
            "title_match": "Virtual Try On",
            "desc_match": "Enable buyers to see how various sizes",
            "title": "Virtual Try-On",
            "desc": (
                "Let shoppers visualize fit, drape, and styling across sizes "
                "— see how a kurta falls at their height, how a blazer "
                "sits on their shoulders, or how a lehenga’s flare looks "
                "in motion.\n\n"
                "Brands using virtual try-on have seen return rates drop by "
                "up to 40%.\n\n"
                "Higher conversion, fewer returns, and the confidence to buy "
                "without visiting a store."
            ),
        },
        {
            "title_match": "Multilingual queries",
            "desc_match": "regional languages to search",
            "title": "Vernacular + natural-language queries",
            "desc": (
                "Hindi, Tamil, Telugu and Bengali queries mapped to the "
                "English catalog — “salwar suit” \u2192 salwar kameez, "
                "“dupatta” \u2192 stole, “pattu pudavai” "
                "\u2192 silk saree.\n\n"
                "Natural-language queries like “what should I wear to "
                "a sangeet if I’m plus-size” resolve to curated outfits "
                "instead of 0 results.\n\n"
                "Unlocks tier-2 and tier-3 buyers for whom vernacular and "
                "conversational phrasing are the first language of search."
            ),
        },
        {
            "title_match": "App Storefront on ChatGPT",
            "desc_match": "40% of shoppers now start their buying journey",
            "title": "App Storefront on ChatGPT",
            "desc": (
                "40% of buyers now start their fashion research on "
                "ChatGPT / Gemini / Perplexity before visiting a brand "
                "site.\n\n"
                "Your catalog surfaces when shoppers ask “what should "
                "I wear to a Goa beach wedding” — alongside Myntra, "
                "ASOS, and Zalando.\n\n"
                "H&M, ASOS, Zalando and Klarna are already live on "
                "ChatGPT. Indian fashion retail is still wide open."
            ),
        },
    ],
    "comparison_examples": {
        1: "blue shirt",
        2: "dupatta / stole / scarf",
        3: "outfit for a summer wedding in Goa",
        4: "what to wear to a formal dinner date",
        6: "red, sleeveless, v-neck, medium dress, within budget",
    },
    "graph_definition": {
        "query": "Outfit for my cousin's beach\nwedding in July",
        "intents": ["beach", "July", "wedding"],
        "keywords": {
            "beach": ["pastel", "boho"],
            "July": ["summer"],
            "wedding": ["lehenga", "sharara", "kurta"],
        },
        "sub_keywords": {
            "summer": ["cotton", "chiffon"],
        },
        "results": [
            "pastel pink chiffon\nlehenga",
            "boho cotton\njacket",
            "light blue net\nsaree",
            "yellow sequinned\nsharara",
        ],
    },
}


# ---------------------------------------------------------------------------
# Electronics
# ---------------------------------------------------------------------------
# Ported from build_croma_deck.py with brand-specific references removed.

ELECTRONICS = {
    "label": "Electronics",
    "competitors_global": [
        (
            "Best Buy",
            " — GenAI shopping assistant (Google Cloud + Accenture, 2024), "
            "agentic AI expansion in 2025, catalog live on ChatGPT via the "
            "Agentic Commerce Protocol.",
        ),
        (
            "MediaMarktSaturn",
            " — Smart Manual chatbot for ~1,900 private-label SKUs plus "
            "MyBuddy in-store voice agent on Azure OpenAI.",
        ),
        (
            "Amazon Rufus",
            " — live across Amazon India and globally, 250M shoppers, "
            "+$10B downstream sales, 60% higher purchase likelihood.",
        ),
        (
            "Walmart Sparky",
            " — live in ChatGPT and Google Gemini with integrated "
            "checkout.",
        ),
        (
            "Home Depot, Lowe’s, Wayfair",
            " — all with ChatGPT storefronts and native AI advisors "
            "for complex-catalog verticals.",
        ),
    ],
    "competitors_india": [
        (
            "Amazon India (Rufus)",
            " — rolled out to all India customers on app and desktop in "
            "late 2025, now answering spec and use-case questions natively.",
        ),
        (
            "Flipkart (Flippi / SLAP)",
            " — Flippi live; SLAP, the next-gen conversational assistant, "
            "announced for early 2026.",
        ),
        (
            "Ajio (Reliance Retail)",
            " — visual search via Rezolve live across the storefront.",
        ),
        (
            "Tata Neu / Croma",
            " — multilingual chatbot in the Tata super-app; exploring "
            "conversational product discovery.",
        ),
        (
            "Reliance Digital, Vijay Sales, Poorvika",
            " — no on-site conversational assistants today. The category "
            "is still wide open in Indian consumer electronics.",
        ),
    ],
    "text_swaps": {
        # Slide 4 — gap narrative
        3: [
            ("scarf and dupatta", "phone and smartphone"),
            ("“Jaipur in May”",
             "“humid Bengaluru summer”"),
            (" to summer and summer to cotton",
             " to low-noise and low-noise to inverter"),
            ("“blazer”", "“laptop for coding”"),
            ("“light pink lehenga”",
             "“5-star 1.5 ton inverter AC”"),
            ("“for an office party”",
             "“for a small 10x12 bedroom”"),
            ("“for a wedding in India in May”",
             "“that doesn’t spike my summer bill”"),
            (
                "“I need an outfit under 20000 for myself, size medium, "
                "for my sister’s beach wedding, I like sequins”",
                "“I need a laptop with Intel i5, 16GB RAM and "
                "SSD for college coding and light gaming, within budget”",
            ),
            (
                "it maps beach to : pastels/boho, wedding to lehenga/"
                "sharara/gown, adds the conditions for sequins",
                "it maps college coding to: Intel i5 / 16GB RAM / SSD / "
                "integrated GPU, adds the conditions for price",
            ),
        ],
        # Slide 5 — three challenges
        4: [
            ("in the next slide", "on slide 11"),
            ("fit/cut", "processor/energy-rating"),
            ("“summer” or “polka”",
             "“inverter” or “copper coil”"),
            ("“outfit for 90’s themed bachelorette”",
             "“laptop for a college coder”"),
            ("“polka saree”",
             "“i5 16GB SSD within budget”"),
            ("“for a Christian wedding”",
             "“for a small bedroom”"),
            ("“non white gown”",
             "“5-star copper-coil inverter AC”"),
            ("“red dress”",
             "“smart TV 55 inch 4K”"),
            ("“16GM RAM”",
             "“16GB RAM”"),
            ("“I want an outfit for my birthday”",
             "“I want appliances for my new flat”"),
            ("“I want a laptop good for Photoshop”",
             "“I want a laptop good for Photoshop and light gaming”"),
        ],
        # Slide 8 — current offerings
        7: [
            ("“outfit for Ladakh trip”",
             "“appliances for a new flat”"),
            ("“plan my meals”",
             "“quiet washing machine that fits my bathroom”"),
        ],
        # Slide 9 — future of e-commerce
        8: [
            ("virtual try-on", "AR room visualization"),
        ],
        # Slide 12 — cross-sell
        11: [
            ("a complete look instead of a single SKU",
             "a matched bundle — TV plus soundbar, camera plus lens plus "
             "mic — instead of a single SKU"),
            ("Single-item sessions become full outfits",
             "Single-item sessions become full set-ups"),
            ("Stylist-grade cross-sell", "Expert-grade bundling"),
            ("size/fit", "specs/compatibility"),
        ],
    },
    "slide10_offerings": [
        {
            "title_match": "Virtual Try On",
            "desc_match": "Enable buyers to see how various sizes",
            "title": "AR Room Visualization",
            "desc": (
                "See the 55-inch TV on your actual wall, the 1.5 ton split AC "
                "above your bed, or the double-door fridge in your kitchen via "
                "AR before you commit.\n\n"
                "The #1 return reason in large appliances is “doesn’t "
                "fit the space.” AR fit tools cut this dramatically in "
                "furniture and are now moving into appliances.\n\n"
                "Higher conversion, fewer returns, lower reverse-logistics "
                "cost on high-ticket SKUs."
            ),
        },
        {
            "title_match": "Multilingual queries",
            "desc_match": "regional languages to search",
            "title": "Vernacular + natural-language queries",
            "desc": (
                "Hindi, Tamil, Telugu and Bengali queries mapped to the "
                "English catalog — “geyser” → water heater, "
                "“cooler” → air cooler, “chimney” "
                "→ kitchen chimney, “fridge” → "
                "refrigerator.\n\n"
                "Natural-language queries like “its too hot in my room "
                "but i cant afford an ac what are my options” resolve to "
                "budget coolers and fans instead of expensive split ACs.\n\n"
                "Unlocks tier-2 and tier-3 buyers for whom vernacular and "
                "conversational phrasing are the first language of search."
            ),
        },
        {
            "title_match": "App Storefront on ChatGPT",
            "desc_match": "40% of shoppers now start their buying journey",
            "title": "App Storefront on ChatGPT",
            "desc": (
                "40% of buyers now start their electronics research on "
                "ChatGPT / Gemini / Perplexity before visiting a retailer "
                "site.\n\n"
                "Your catalog becomes shoppable inside the AI conversation "
                "— specs, prices, energy ratings and compatibility surfaced "
                "natively.\n\n"
                "Best Buy, Walmart, Home Depot, Lowe’s and Wayfair are "
                "already live on ChatGPT via OpenAI’s Agentic Commerce "
                "Protocol. Indian electronics retail is still wide open."
            ),
        },
    ],
    "comparison_examples": {
        1: "smart tv 55 inch 4K",
        2: "geyser / chimney / cooler",
        3: "appliances for a new 2bhk flat",
        4: "quiet washing machine that fits my bathroom",
        6: "inverter, 1.5 ton, 5 star, copper coil, split ac, within budget",
    },
    "graph_definition": {
        "query": "Laptop for college coding and\nlight gaming within budget",
        "intents": ["college coding", "light gaming", "within budget"],
        "keywords": {
            "college coding": ["i5 / Ryzen 5", "16GB RAM", "SSD"],
            "light gaming": ["dedicated GPU"],
            "within budget": ["budget filter"],
        },
        "sub_keywords": {},
        "results": [
            "Acer Nitro 5\ni5 16GB SSD",
            "Lenovo IdeaPad\nGaming 3",
            "HP Victus\ni5 GTX 1650",
            "ASUS VivoBook\nPro 15",
        ],
    },
}


# ---------------------------------------------------------------------------
# Furniture
# ---------------------------------------------------------------------------
# Ported from build_urban_ladder_deck.py with brand-specific references removed.

FURNITURE = {
    "label": "Furniture",
    "competitors_global": [
        (
            "Wayfair Muse",
            " — AI visual discovery, type a style and get shoppable "
            "AI-generated room designs (Feb 2025).",
        ),
        (
            "IKEA Kreativ",
            " — mixed-reality design experience, AR room planning "
            "with the full catalog.",
        ),
        (
            "Lowe’s Mylow",
            " — OpenAI-powered home improvement advisor, live since "
            "Mar 2025.",
        ),
        (
            "Home Depot",
            " — AI shopping assistant integrated across the storefront.",
        ),
        (
            "Amazon Rufus",
            " — live across home and furniture, 60% higher purchase "
            "likelihood.",
        ),
    ],
    "competitors_india": [
        (
            "Pepperfry",
            " — piloting AI-led visual discovery and AR room planning "
            "across offline studios.",
        ),
        (
            "Livspace",
            " — AI-powered modular design and interior recommendations "
            "at scale.",
        ),
        (
            "IKEA India",
            " — extending Kreativ globally, already live on ikea.com/in.",
        ),
        (
            "Flipkart",
            " — generative-AI product search integrated into the home "
            "and furniture storefront.",
        ),
        (
            "Nilkamal, Godrej Interio, Wooden Street",
            " — experimenting with conversational discovery in their apps.",
        ),
    ],
    "text_swaps": {
        # Slide 4 — gap narrative
        3: [
            ("scarf and dupatta", "palang and bed"),
            ("“Jaipur in May”",
             "“a small 10x12 bedroom”"),
            (" to summer and summer to cotton",
             " to compact and compact to sofa cum bed"),
            ("“blazer”", "“ergonomic office chair”"),
            ("“light pink lehenga”",
             "“queen storage bed”"),
            ("“for an office party”",
             "“for a new 2BHK apartment”"),
            ("“for a wedding in India in May”",
             "“for a home office that doesn’t wreck my back”"),
            (
                "“I need an outfit under 20000 for myself, size medium, "
                "for my sister’s beach wedding, I like sequins”",
                "“I need a compact sofa for my 10x12 "
                "living room, fabric in earth tones, should double as a "
                "guest bed”",
            ),
            (
                "it maps beach to : pastels/boho, wedding to lehenga/"
                "sharara/gown, adds the conditions for sequins",
                "it maps small living room to compact/2-seater, guest bed "
                "to sofa cum bed, adds the conditions for price and fabric",
            ),
        ],
        # Slide 5 — three challenges
        4: [
            ("in the next slide", "on slide 11"),
            ("fit/cut", "material/finish"),
            ("“summer” or “polka”",
             "“compact” or “sheesham”"),
            ("“outfit for 90’s themed bachelorette”",
             "“furniture for a new 2BHK”"),
            ("“polka saree”", "“compact sofa cum bed”"),
            ("“for a Christian wedding”",
             "“for a home office setup”"),
            ("“non white gown”",
             "“ergonomic WFH chair”"),
            ("“red dress”", "“queen size bed”"),
            ("“16GM RAM”",
             "“6-seater dining table”"),
            ("“I want an outfit for my birthday”",
             "“I want furniture for my new home”"),
            ("“I want a laptop good for Photoshop”",
             "“I want a sofa that fits my 10x12 living room”"),
        ],
        # Slide 8 — current offerings
        7: [
            ("“outfit for Ladakh trip”",
             "“furniture for a new 2BHK”"),
            ("“plan my meals”",
             "“office chair for back pain”"),
        ],
        # Slide 9 — future of e-commerce
        8: [
            ("virtual try-on", "AR room visualization"),
        ],
        # Slide 12 — cross-sell
        11: [
            ("a complete look instead of a single SKU",
             "a complete bedroom or living room instead of a single SKU"),
            ("Single-item sessions become full outfits",
             "Single-item sessions become full room sets"),
            ("Stylist-grade cross-sell", "Room-grade cross-sell"),
            ("size/fit", "room dimensions/style"),
        ],
    },
    "slide10_offerings": [
        {
            "title_match": "Virtual Try On",
            "desc_match": "Enable buyers to see how various sizes",
            "title": "AR Room Visualization",
            "desc": (
                "Let buyers place a sofa, bed, or wardrobe in their actual "
                "room via AR before they commit.\n\n"
                "Furniture’s biggest return reason is “doesn’t "
                "fit the space” — IKEA Place and Wayfair View in "
                "Room 3D have cut this by up to 35%.\n\n"
                "Higher conversion, fewer returns, fewer costly reverse-"
                "logistics hits."
            ),
        },
        {
            "title_match": "Multilingual queries",
            "desc_match": "regional languages to search",
            "title": "Vernacular + natural-language queries",
            "desc": (
                "Hindi, Tamil, Telugu and Bengali queries mapped correctly "
                "to the English catalog — palang → bed, almirah "
                "→ wardrobe, diwan → daybed, mandir → pooja "
                "unit.\n\n"
                "Natural-language queries like “just moved into a new "
                "2BHK, what do I need” resolve to a curated shortlist "
                "instead of 0 results.\n\n"
                "Unlocks tier-2 and tier-3 cities where vernacular and "
                "conversational phrasing are the first language of search."
            ),
        },
        {
            "title_match": "App Storefront on ChatGPT",
            "desc_match": "40% of shoppers now start their buying journey",
            "title": "App Storefront on ChatGPT",
            "desc": (
                "40% of buyers now start their furniture research on "
                "ChatGPT / Gemini / Perplexity before visiting a brand "
                "site.\n\n"
                "Your catalog becomes shoppable inside the AI conversation "
                "— product imagery, dimensions, finishes, and "
                "lifestyle context surfaced natively.\n\n"
                "Wayfair, Home Depot, Lowe’s and IKEA are already "
                "exposing catalogs to AI agents. Works across every "
                "platform, not just one."
            ),
        },
    ],
    "comparison_examples": {
        1: "queen size bed",
        2: "almirah / sofa cum bed",
        3: "furniture for new 2bhk apartment",
        4: "office chair for back pain while WFH",
        6: "sheesham, 6-seater, teak, dining table, within budget",
    },
    "graph_definition": {
        "query": "Compact sofa for a 10x12 living room\nthat doubles as a guest bed",
        "intents": ["compact", "10x12 room", "guest bed"],
        "keywords": {
            "compact": ["2-seater", "loveseat"],
            "10x12 room": ["small dimensions"],
            "guest bed": ["sofa cum bed", "futon"],
        },
        "sub_keywords": {
            "sofa cum bed": ["fabric", "storage"],
        },
        "results": [
            "2-seater fabric\nsofa cum bed",
            "compact futon\nwith storage",
            "loveseat\ndaybed",
            "foldable\nsofa bed",
        ],
    },
}


# ---------------------------------------------------------------------------
# Bags — populated from web research
# ---------------------------------------------------------------------------

BAGS = {
    "label": "Bags",
    "competitors_global": [
        (
            "Michael Kors (Shopping Muse)",
            " — first retailer to ship Mastercard's Dynamic Yield AI "
            "shopping assistant (Jun 2024), 15-20% conversion lift in "
            "initial tests.",
        ),
        (
            "Louis Vuitton",
            " — LV Virtual Advisor chatbot on Messenger and on-site NLP, "
            "60% faster response times, measurable conversion lift.",
        ),
        (
            "Gucci",
            " — AI chatbot handles 83% of inquiries, 22% drive to sales. "
            "AR try-on for bags via Apple Vision Pro.",
        ),
        (
            "Farfetch (iFetch + WANNA)",
            " — multimodal search (text + image), AR bag try-on via WANNA "
            "drove +47% visits and +22% add-to-bag.",
        ),
        (
            "Samsonite / TUMI",
            " — 3D viewer and AR via Fibbl (Nov 2024), virtual luggage "
            "size comparison across all brands.",
        ),
    ],
    "competitors_india": [
        (
            "Myntra (Maya)",
            " — ChatGPT-powered conversational stylist, covers 2.3M "
            "styles across fashion including bags.",
        ),
        (
            "Flipkart (Flippi / SLAP)",
            " — Flippi live; SLAP standalone conversational AI shopping "
            "app launched Jan 2026.",
        ),
        (
            "Amazon India (Rufus)",
            " — live across all categories including bags/luggage, "
            "60% higher purchase likelihood.",
        ),
        (
            "Ajio",
            " — AI-powered personalization and visual search across "
            "fashion and accessories.",
        ),
        (
            "Mokobara, Baggit, Lavie, Hidesign, Wildcraft",
            " — no on-site conversational assistants today. Indian D2C "
            "bags is entirely unserved.",
        ),
    ],
    "text_swaps": {
        # Slide 4 — gap narrative
        3: [
            ("scarf and dupatta", "crossbody and sling bag"),
            ("“Jaipur in May”",
             "“a 2-week European backpacking trip”"),
            (" to summer and summer to cotton",
             " to travel and travel to anti-theft"),
            ("“blazer”", "“laptop bag for office”"),
            ("“light pink lehenga”",
             "“tan leather tote”"),
            ("“for an office party”",
             "“that fits a 15-inch laptop”"),
            ("“for a wedding in India in May”",
             "“that’s airline-compliant for IndiGo cabin”"),
            (
                "“I need an outfit under 20000 for myself, size medium, "
                "for my sister’s beach wedding, I like sequins”",
                "“I need a waterproof laptop backpack with USB charging "
                "port, anti-theft zippers, and a trolley sleeve, within budget”",
            ),
            (
                "it maps beach to : pastels/boho, wedding to lehenga/"
                "sharara/gown, adds the conditions for sequins",
                "it maps waterproof to material/coating, USB port to "
                "tech-enabled, trolley sleeve to travel-compatible, "
                "adds the conditions for price",
            ),
        ],
        # Slide 5 — three challenges
        4: [
            ("in the next slide", "on slide 11"),
            ("fit/cut", "material/closure"),
            ("“summer” or “polka”",
             "“waterproof” or “anti-theft”"),
            ("“outfit for 90’s themed bachelorette”",
             "“bag for a European backpacking trip”"),
            ("“polka saree”",
             "“anti-theft sling bag”"),
            ("“for a Christian wedding”",
             "“that fits IndiGo cabin limits”"),
            ("“non white gown”",
             "“airline-compliant carry-on”"),
            ("“red dress”",
             "“tan leather tote”"),
            ("“16GM RAM”",
             "“crossbody with bottle pocket”"),
            ("“I want an outfit for my birthday”",
             "“I need a bag for gym and work”"),
            ("“I want a laptop good for Photoshop”",
             "“I want a carry-on that fits my 15-inch laptop”"),
        ],
        # Slide 8 — current offerings
        7: [
            ("“outfit for Ladakh trip”",
             "“carry-on for a 2-week Europe trip”"),
            ("“plan my meals”",
             "“bag for gym clothes and work laptop”"),
        ],
        # Slide 9 — future of e-commerce
        8: [
            ("virtual try-on", "AR size visualization"),
        ],
        # Slide 12 — cross-sell
        11: [
            ("a complete look instead of a single SKU",
             "a matched set — backpack plus wallet plus card holder "
             "— instead of a single SKU"),
            ("Single-item sessions become full outfits",
             "Single-item sessions become complete travel kits"),
            ("Stylist-grade cross-sell", "Travel-kit cross-sell"),
            ("size/fit", "dimensions/capacity"),
        ],
    },
    "slide10_offerings": [
        {
            "title_match": "Virtual Try On",
            "desc_match": "Enable buyers to see how various sizes",
            "title": "AR Size Visualization",
            "desc": (
                "See the backpack on your shoulders, compare the carry-on "
                "against your current bag, or check if your 15-inch laptop "
                "fits via AR before you commit.\n\n"
                "Size mismatches cause ~24% of handbag returns. "
                "Farfetch’s WANNA AR drove +47% visits and +22% "
                "add-to-bag. Samsonite/TUMI now offer 3D size comparison "
                "via Fibbl.\n\n"
                "Higher conversion, fewer returns, lower reverse-logistics "
                "cost on premium bags."
            ),
        },
        {
            "title_match": "Multilingual queries",
            "desc_match": "regional languages to search",
            "title": "Vernacular + natural-language queries",
            "desc": (
                "Hindi, Tamil, Telugu and Bengali queries mapped to the "
                "English catalog — “basta” → bag, "
                "“jhola” → tote, “pithu bag” "
                "→ backpack.\n\n"
                "Natural-language queries like “I need something to "
                "carry my gym clothes and work laptop in one bag” "
                "resolve to gym-office hybrids instead of 0 results.\n\n"
                "Unlocks tier-2 and tier-3 buyers for whom vernacular and "
                "conversational phrasing are the first language of search."
            ),
        },
        {
            "title_match": "App Storefront on ChatGPT",
            "desc_match": "40% of shoppers now start their buying journey",
            "title": "App Storefront on ChatGPT",
            "desc": (
                "40% of buyers now start their product research on "
                "ChatGPT / Gemini / Perplexity before visiting a brand "
                "site.\n\n"
                "Your catalog becomes shoppable inside the AI conversation "
                "— dimensions, airline compliance, compartments, and "
                "material details surfaced natively.\n\n"
                "Amazon Rufus is already answering bag queries for 250M "
                "shoppers. Works across every platform, not just one."
            ),
        },
    ],
    "comparison_examples": {
        1: "tan leather tote",
        2: "crossbody / sling bag / messenger",
        3: "bag for a European backpacking trip",
        4: "something to carry gym clothes and work laptop",
        6: "waterproof, laptop sleeve, USB port, anti-theft, backpack, within budget",
    },
    "graph_definition": {
        "query": "Crossbody bag for travel that fits\na water bottle and passport",
        "intents": ["travel", "crossbody", "water bottle\n+ passport"],
        "keywords": {
            "travel": ["durable", "lightweight"],
            "crossbody": ["adjustable strap", "hands-free"],
            "water bottle\n+ passport": ["compartments", "medium size"],
        },
        "sub_keywords": {},
        "results": [
            "canvas crossbody\nwith bottle pocket",
            "anti-theft\ntravel sling",
            "nylon multi-pocket\ncrossbody",
            "leather travel\norganizer",
        ],
    },
}


# ---------------------------------------------------------------------------
# Shoes — populated from web research
# ---------------------------------------------------------------------------

SHOES = {
    "label": "Shoes",
    "competitors_global": [
        (
            "Puma (AI Shopping Assistant)",
            " — 7x higher conversion for AI-assisted shoppers vs "
            "non-users, 8x higher revenue per visitor. 42% of queries "
            "are about sizing/fit.",
        ),
        (
            "Nike (Nike Fit)",
            " — AR foot-scanning in the Nike App, 13-point measurement "
            "system for personalized size recommendations. 500K+ sizing "
            "calls/year eliminated.",
        ),
        (
            "Zappos",
            " — AI-rebuilt search engine using genetic algorithms, "
            "personal shopping assistant on Sneakers tab, conversational "
            "chatbot for size recommendations.",
        ),
        (
            "Steve Madden",
            " — AI shopping optimization via Fast Simon across 25 stores "
            "on 5 continents (Sep 2024).",
        ),
        (
            "Volumental (New Balance, Hoka, On, Adidas)",
            " — 3D foot scanning + AI fit engine, 25% return reduction, "
            "32.5% basket size increase across retailers.",
        ),
    ],
    "competitors_india": [
        (
            "Myntra (Maya)",
            " — ChatGPT-powered conversational stylist, covers 2.3M "
            "styles across fashion and footwear.",
        ),
        (
            "Flipkart (Flippi / SLAP)",
            " — Flippi live; SLAP standalone conversational AI shopping "
            "app launched Jan 2026.",
        ),
        (
            "Amazon India (Rufus)",
            " — live across all categories including footwear, "
            "but only 32% accuracy on product matching.",
        ),
        (
            "Ajio",
            " — AI-powered personalization and visual search across "
            "fashion and footwear.",
        ),
        (
            "Bata, Metro, Woodland, Campus, Relaxo",
            " — no on-site conversational assistants or AI fit tools "
            "today. Indian footwear D2C is entirely unserved.",
        ),
    ],
    "text_swaps": {
        # Slide 4 — gap narrative
        3: [
            ("scarf and dupatta", "sneakers and trainers"),
            ("“Jaipur in May”",
             "“standing all day at work”"),
            (" to summer and summer to cotton",
             " to cushioned and cushioned to memory foam"),
            ("“blazer”", "“formal shoes for office”"),
            ("“light pink lehenga”",
             "“white cushioned running shoes”"),
            ("“for an office party”",
             "“with arch support for flat feet”"),
            ("“for a wedding in India in May”",
             "“that won’t hurt my plantar fasciitis”"),
            (
                "“I need an outfit under 20000 for myself, size medium, "
                "for my sister’s beach wedding, I like sequins”",
                "“I need white cushioned running shoes with arch "
                "support for flat feet, wide toe box, within budget”",
            ),
            (
                "it maps beach to : pastels/boho, wedding to lehenga/"
                "sharara/gown, adds the conditions for sequins",
                "it maps flat feet to arch support/stability, wide toe "
                "box to wide-fit, adds the conditions for price and "
                "cushioning",
            ),
        ],
        # Slide 5 — three challenges
        4: [
            ("in the next slide", "on slide 11"),
            ("fit/cut", "arch/cushioning"),
            ("“summer” or “polka”",
             "“cushioned” or “breathable”"),
            ("“outfit for 90’s themed bachelorette”",
             "“shoes for standing all day at work”"),
            ("“polka saree”",
             "“memory foam arch support shoe”"),
            ("“for a Christian wedding”",
             "“for a beach wedding in Goa”"),
            ("“non white gown”",
             "“embellished block-heel sandal”"),
            ("“red dress”",
             "“white running shoes”"),
            ("“16GM RAM”",
             "“wide-fit walking shoes”"),
            ("“I want an outfit for my birthday”",
             "“I need shoes for my bad knees”"),
            ("“I want a laptop good for Photoshop”",
             "“I want running shoes for overpronation”"),
        ],
        # Slide 8 — current offerings
        7: [
            ("“outfit for Ladakh trip”",
             "“running shoes for flat feet”"),
            ("“plan my meals”",
             "“comfortable heels for a 12-hour office day”"),
        ],
        # Slide 9 — future of e-commerce
        8: [
            ("virtual try-on", "AR fit prediction"),
        ],
        # Slide 12 — cross-sell
        11: [
            ("a complete look instead of a single SKU",
             "a matched set — running shoes plus socks plus insoles "
             "plus care kit — instead of a single SKU"),
            ("Single-item sessions become full outfits",
             "Single-item sessions become complete activity kits"),
            ("Stylist-grade cross-sell", "Activity-kit cross-sell"),
            ("occasion, budget, use-case, size/fit",
             "activity, budget, terrain, size/fit"),
        ],
    },
    "slide10_offerings": [
        {
            "title_match": "Virtual Try On",
            "desc_match": "Enable buyers to see how various sizes",
            "title": "AR Fit Prediction",
            "desc": (
                "Scan your feet with your phone camera, get AI-powered "
                "size recommendations matched to each shoe model.\n\n"
                "67% of shoe returns are due to sizing issues, costing "
                "$12-19 per return. Volumental’s 3D scanning cuts returns "
                "25-38%, and Puma reports 42% of AI queries are about "
                "sizing/fit.\n\n"
                "Higher conversion, dramatically fewer returns, lower "
                "reverse-logistics cost."
            ),
        },
        {
            "title_match": "Multilingual queries",
            "desc_match": "regional languages to search",
            "title": "Vernacular + natural-language queries",
            "desc": (
                "Hindi, Tamil, Telugu and Bengali queries mapped to the "
                "English catalog — “joota” → shoes, "
                "“chappal” → sandal, “sports ka joota” "
                "→ sports shoes.\n\n"
                "Natural-language queries like “shoes that won’t hurt "
                "my plantar fasciitis” resolve to arch-support shoes "
                "instead of 0 results.\n\n"
                "Unlocks tier-2 and tier-3 buyers for whom vernacular and "
                "conversational phrasing are the first language of search."
            ),
        },
        {
            "title_match": "App Storefront on ChatGPT",
            "desc_match": "40% of shoppers now start their buying journey",
            "title": "App Storefront on ChatGPT",
            "desc": (
                "40% of buyers now start their product research on "
                "ChatGPT / Gemini / Perplexity before visiting a brand "
                "site.\n\n"
                "Your catalog becomes shoppable inside the AI conversation "
                "— size, cushioning, arch support, and activity fit "
                "surfaced natively.\n\n"
                "Puma’s AI assistant drives 7x conversion. Indian "
                "footwear e-commerce ($5B, growing 9.7% CAGR) is ready "
                "for the same."
            ),
        },
    ],
    "comparison_examples": {
        1: "white running shoes",
        2: "sneakers / trainers / sports shoes",
        3: "shoes for a beach wedding in Goa",
        4: "comfortable heels for standing all day at work",
        6: "cushioned, wide toe box, arch support, running shoe, within budget",
    },
    "graph_definition": {
        "query": "Comfortable heels for an all-day\nwedding that won’t hurt",
        "intents": ["comfortable", "heels", "all-day wedding"],
        "keywords": {
            "comfortable": ["cushioned insole", "arch support"],
            "heels": ["block heel", "kitten heel"],
            "all-day wedding": ["formal", "durable"],
        },
        "sub_keywords": {},
        "results": [
            "block heel sandal\nwith cushion",
            "kitten heel\npump",
            "wedge heel with\narch support",
            "embellished\nblock heel",
        ],
    },
}


# ---------------------------------------------------------------------------
# Jewellery — populated from web research
# ---------------------------------------------------------------------------

JEWELLERY = {
    "label": "Jewellery",
    "competitors_global": [
        (
            "Pandora (Gemma)",
            " — AI personal shopper on Salesforce Agentforce (Sep 2025), "
            "understands occasions, preferences, budgets. Clara AI handles "
            "60% of service cases (+10% NPS).",
        ),
        (
            "Tiffany & Co.",
            " — AI recommendations drove 25% conversion rise, 40% AOV "
            "increase. AR try-on for rings, bracelets, necklaces: 22% "
            "conversion jump, 19% fewer returns.",
        ),
        (
            "Cartier",
            " — Google Cloud AI image recognition identifies any product "
            "from 174-year archive in <2 seconds. “Looking Glass” "
            "in-store AR (Jan 2025).",
        ),
        (
            "Signet (Kay, Zales, Jared)",
            " — world’s largest diamond jeweller, AI personalization "
            "across all brands. AR try-on: 67% adoption, 27% higher "
            "conversion.",
        ),
        (
            "Blue Nile / James Allen / Brilliant Earth",
            " — AI diamond recommendation engines, AR ring try-on, "
            "360° diamond video. 20-25% conversion lift across platforms.",
        ),
    ],
    "competitors_india": [
        (
            "CaratLane (Tata/Tanishq)",
            " — pioneer AR virtual try-on since 2015, 200% app usage "
            "increase, 40% of business from AR app. $100M+ quarterly "
            "revenue.",
        ),
        (
            "Tanishq",
            " — 1,000+ chats/day, Sherpa AI for personalization, "
            "Endless Aisle kiosks. 107% uplift in click-to-conversion "
            "during Akshay Tritiya.",
        ),
        (
            "BlueStone",
            " — AI/ML for UX, AR try-on, blockchain authentication. "
            "SEBI-approved $120M IPO.",
        ),
        (
            "Kalyan (Candere), Malabar Gold",
            " — Candere uses AI for behavior analysis. Malabar partnered "
            "with Accenture for AI-driven operations. Neither has "
            "conversational search.",
        ),
        (
            "GIVA, Melorra, PC Jeweller",
            " — GIVA has selective AR try-on. No Indian jewellery brand "
            "has conversational AI product discovery today.",
        ),
    ],
    "text_swaps": {
        # Slide 4 — gap narrative
        3: [
            ("scarf and dupatta", "necklace and mangalsutra"),
            ("“Jaipur in May”",
             "“a South Indian wedding”"),
            (" to summer and summer to cotton",
             " to bridal and bridal to temple jewellery"),
            ("“blazer”", "“engagement ring”"),
            ("“light pink lehenga”",
             "“22kt BIS hallmark gold choker”"),
            ("“for an office party”",
             "“for daily wear to office”"),
            ("“for a wedding in India in May”",
             "“that’s hypoallergenic for sensitive ears”"),
            (
                "“I need an outfit under 20000 for myself, size medium, "
                "for my sister’s beach wedding, I like sequins”",
                "“I need a lightweight gold necklace within budget, "
                "22kt BIS hallmark, minimalist for daily wear, "
                "that won’t tangle”",
            ),
            (
                "it maps beach to : pastels/boho, wedding to lehenga/"
                "sharara/gown, adds the conditions for sequins",
                "it maps lightweight to under 10g, daily wear to "
                "minimalist/durable, adds the conditions for karat, "
                "hallmark, and price",
            ),
        ],
        # Slide 5 — three challenges
        4: [
            ("in the next slide", "on slide 11"),
            ("fit/cut", "karat/purity"),
            ("“summer” or “polka”",
             "“hallmark” or “antique finish”"),
            ("“outfit for 90’s themed bachelorette”",
             "“jewellery for a South Indian wedding”"),
            ("“polka saree”",
             "“22kt temple gold jhumka”"),
            ("“for a Christian wedding”",
             "“for sensitive ears that won’t react”"),
            ("“non white gown”",
             "“22kt Maharashtrian black-bead mangalsutra”"),
            ("“red dress”",
             "“gold choker necklace”"),
            ("“16GM RAM”",
             "“antique kundan bridal set”"),
            ("“I want an outfit for my birthday”",
             "“I need jewellery for my wedding”"),
            ("“I want a laptop good for Photoshop”",
             "“I want earrings that won’t irritate sensitive ears”"),
        ],
        # Slide 8 — current offerings
        7: [
            ("“outfit for Ladakh trip”",
             "“jewellery for a South Indian wedding”"),
            ("“plan my meals”",
             "“lightweight earrings for daily wear”"),
        ],
        # Slide 9 — future of e-commerce
        8: [
            ("virtual try-on", "AR jewellery try-on"),
        ],
        # Slide 12 — cross-sell
        11: [
            ("a complete look instead of a single SKU",
             "a complete bridal set — necklace plus matching earrings "
             "plus bangles — instead of a single piece"),
            ("Single-item sessions become full outfits",
             "Single-item sessions become complete jewellery sets"),
            ("Stylist-grade cross-sell", "Jeweller-grade set-building"),
            ("occasion, budget, use-case, size/fit",
             "occasion, budget, metal/purity, style"),
        ],
    },
    "slide10_offerings": [
        {
            "title_match": "Virtual Try On",
            "desc_match": "Enable buyers to see how various sizes",
            "title": "AR Jewellery Try-On",
            "desc": (
                "See the necklace on your neck, the jhumkas on your ears, "
                "or the ring on your hand via AR before you commit.\n\n"
                "CaratLane pioneered this — 200% app usage increase, 40% "
                "of business from AR. Tiffany reports 22% conversion jump "
                "and 19% fewer returns. Signet’s VTO has 67% adoption "
                "among mobile users.\n\n"
                "Higher conversion, fewer returns, and the confidence "
                "bridge that brings offline jewellery buyers online."
            ),
        },
        {
            "title_match": "Multilingual queries",
            "desc_match": "regional languages to search",
            "title": "Vernacular + natural-language queries",
            "desc": (
                "Hindi, Tamil, Telugu and Bengali queries mapped to the "
                "English catalog — “mangalsutra” vs “thali” "
                "vs “minnu”, “nath” vs “mukkuthi”, "
                "“jhumka” vs “jhumki”.\n\n"
                "Natural-language queries like “something lightweight "
                "I can wear daily to office” resolve to minimalist "
                "daily-wear pieces instead of 0 results.\n\n"
                "India’s $95B jewellery market is only 4% online. "
                "Vernacular conversational search bridges the trust gap."
            ),
        },
        {
            "title_match": "App Storefront on ChatGPT",
            "desc_match": "40% of shoppers now start their buying journey",
            "title": "App Storefront on ChatGPT",
            "desc": (
                "40% of buyers now start their product research on "
                "ChatGPT / Gemini / Perplexity before visiting a brand "
                "site.\n\n"
                "Your catalog becomes shoppable inside the AI conversation "
                "— karat, hallmark, gemstone, weight, and occasion "
                "details surfaced natively.\n\n"
                "Jewellery has the highest AOV ($436) but lowest "
                "conversion (0.87%) of any online category. Conversational "
                "AI can close this gap."
            ),
        },
    ],
    "comparison_examples": {
        1: "gold choker necklace",
        2: "mangalsutra / thali / minnu",
        3: "jewellery for a South Indian wedding",
        4: "lightweight daily-wear earrings for sensitive ears",
        6: "22kt, BIS hallmark, antique, temple choker, within budget",
    },
    "graph_definition": {
        "query": "Lightweight gold necklace for\ndaily wear within budget",
        "intents": ["lightweight", "gold", "daily wear", "within budget"],
        "keywords": {
            "lightweight": ["under 10g"],
            "gold": ["22kt", "18kt"],
            "daily wear": ["minimalist", "durable"],
            "within budget": ["budget filter"],
        },
        "sub_keywords": {},
        "results": [
            "18kt delicate\nchain necklace",
            "22kt thin gold\npendant",
            "gold-plated\nlayered chain",
            "hallmarked\ngold choker",
        ],
    },
}


# ---------------------------------------------------------------------------
# Registry
# ---------------------------------------------------------------------------

CATEGORIES = {
    "clothing": CLOTHING,
    "electronics": ELECTRONICS,
    "bags": BAGS,
    "shoes": SHOES,
    "jewellery": JEWELLERY,
    "furniture": FURNITURE,
}
