import streamlit as st

# ==========================================
# 1. PAGE CONFIGURATION
# ==========================================
st.set_page_config(
    page_title="HK Cha Chaan Teng Order & Personality Test",
    page_icon="🍳",
    layout="wide",
)

st.title("🧋 HK Cha Chaan Teng Breakfast Order & Personality Test")
st.write(
    "Step inside a classic Hong Kong *Cha Chaan Teng* (茶餐廳). Place your exact morning order—"
    "from Set A–H and conditional noodle bases to egg styles, Zero Sugar rules, and add-ons—"
    "to see your live waiter's order ticket  and reveal your Hong Kong personality archetype."
)

# ==========================================
# 2. MENU DATA & PERSONALITY ARCHETYPES
# ==========================================
MENU_SETS = {
    "Set A ($42) — 鮮味仿鮑魚絲火腿 (Imitation Abalone & Ham)": {
        "price": 42,
        "has_noodle": True,
        "default_noodle": "通粉 (Macaroni)",
        "default_egg": "太陽蛋 / 煎雙蛋 (Sunny-Side Up / Double Fried Egg)",
        "default_bread": "自家製鮮油餐包 (Homemade Butter Bun)",
        "side_mode": "standard",
    },
    "Set B ($42) — 招牌沙爹牛肉 (Signature Satay Beef)": {
        "price": 42,
        "has_noodle": True,
        "default_noodle": "公仔麵 (Standard Instant Noodle)",
        "default_egg": "嫩滑炒蛋 (Smooth Scrambled Egg)",
        "default_bread": "Top One 丹麥酥 (Top One Danish Toast)",
        "side_mode": "standard",
    },
    "Set C ($42) — 秘製榨菜肉絲 (Pickled Mustard Greens & Shredded Pork)": {
        "price": 42,
        "has_noodle": True,
        "default_noodle": "米粉 (Rice Vermicelli)",
        "default_egg": "嫩滑炒蛋 (Smooth Scrambled Egg)",
        "default_bread": "Top One 丹麥酥 (Top One Danish Toast)",
        "side_mode": "standard",
    },
    "Set D ($42) — 雙拼粉麵餐 (Custom Double-Combo Noodle Set)": {
        "price": 42,
        "has_noodle": True,
        "default_noodle": "通粉 (Macaroni)",
        "default_egg": "嫩滑炒蛋 (Smooth Scrambled Egg)",
        "default_bread": "牛油多士・烘底 (Toasted Butter Bread)",
        "side_mode": "standard",
    },
    "Set E ($40) — 北海道牛乳麥米粥 (Hokkaido Milk Oatmeal Porridge)": {
        "price": 40,
        "has_noodle": False,
        "side_mode": "oatmeal_sandwich",
    },
    "Set F ($47) — 歐陸套餐：脆脆魚柳伴德國腸 (Crispy Fish Fillet & German Sausage)": {
        "price": 47,
        "has_noodle": False,
        "default_egg": "嫩滑炒蛋 (Smooth Scrambled Egg)",
        "default_bread": "Top One 丹麥酥 (Top One Danish Toast)",
        "side_mode": "standard",
    },
    "Set G ($48) — 歐陸套餐：西冷牛扒伴德國腸 (Sirloin Steak & German Sausage)": {
        "price": 48,
        "has_noodle": False,
        "default_egg": "嫩滑炒蛋 (Smooth Scrambled Egg)",
        "default_bread": "Top One 丹麥酥 (Top One Danish Toast)",
        "side_mode": "standard",
    },
    "Set H ($60) — 全日早餐 All-Day Breakfast (吉列魚柳、紐倫堡腸、黑松露炒蛋、煙肉、茄汁豆)": {
        "price": 60,
        "has_noodle": False,
        "side_mode": "all_day_fixed",
    },
}

ADDON_PRICES = {
    "餐蛋治烘底 (+$24) — Toasted Luncheon Meat & Egg Sandwich": 24,
    "腿蛋治 (+$22) — Ham & Egg Sandwich": 22,
    "公司三文治 (+$38) — Loaded Club Sandwich": 38,
    "招牌酥皮蛋撻 (+$12) — Signature Puff Pastry Egg Tart": 12,
    "脆脆奶油豬 (+$22) — Crispy Condensed Milk Bun": 22,
    "單加太陽蛋 (+$8) — Extra Sunny-Side Up Egg": 8,
}

ARCHETYPES = {
    "DemaePerfectionist": {
        "title": "出前一丁執著派 · The Detail Perfectionist",
        "tagline": "You never settle for factory defaults when a better upgrade exists.",
        "desc": (
            "Paying +$5 to upgrade to Demae Iccho (出前一丁), specifying toasted or no ice, and ordering "
            "strictly zero sugar(走甜) says everything: you know exact flavor balance, refuse artificial "
            "shortcuts, and happily invest in getting details right."
        ),
        "trait_label": "99% Standards",
    },
    "CentralSpeedrunner": {
        "title": "中環快狠準戰神 · The Efficiency Strategist",
        "tagline": "Seated, fed, caffeinated, and out the door in 11 minutes flat.",
        "desc": (
            "You pick fast-serving classics like Macaroni or Rice Vermicelli, quick-to-eat buns or boiled/fried eggs, "
            "and sharp iced lemon tea. Practical, decisive, and focused, you treat breakfast like precision fuel "
            "before conquering a packed schedule."
        ),
        "trait_label": "97% Efficiency",
    },
    "DanishRomantic": {
        "title": "丹麥酥儀式感生活家 · The Aesthetic Brunch Romantic",
        "tagline": "Even at 8:30 AM in a bustling cafe, you protect your morning calm.",
        "desc": (
            "Whether it's Hokkaido Milk Oatmeal with Smooth Scrambled Egg Sandwich or crispy Top One Danish Toast "
            "paired with velvety scrambled eggs, you refuse to rush your morning. You appreciate texture, "
            "comfort, and savoring small daily rituals."
        ),
        "trait_label": "96% Aesthetics",
    },
    "KowloonPurist": {
        "title": "懷舊港式靈魂 · The Old-School Heritage Purist",
        "tagline": "Timeless classics became classics for a reason.",
        "desc": (
            "Imitation Abalone & Ham Macaroni, sunny-side up eggs, a homemade butter bun, and hot silk-stocking "
            "milk tea—you value authenticity, loyalty, and grounded reliability over passing trends. "
            "People come to you when they want honest, steady advice."
        ),
        "trait_label": "95% Authenticity",
    },
    "QueueMaximizer": {
        "title": "紅茶排隊王・精明算計家 · The Value & Combo Tactician",
        "tagline": "You know how to extract 120% value out of every breakfast ticket.",
        "desc": (
            "You love Double-Combo (雙拼) sets, Yuanyang, and smart add-ons so every dollar hits maximum satisfaction. "
            "Resourceful and street-smart, you always know the best seats, fastest queues, and smartest combinations."
        ),
        "trait_label": "98% Street Smarts",
    },
    "ComfortHedonist": {
        "title": "歐陸重裝享樂派 · The Unapologetic Comfort Hedonist",
        "tagline": "Life is hard enough—breakfast should be a full celebration.",
        "desc": (
            "Crispy fish fillet, sirloin steak with German sausage, All-Day Breakfast, or loaded sandwiches and egg tarts "
            "on the side. You work hard, play hard, and believe strongly in rewarding yourself from the very first meal."
        ),
        "trait_label": "96% Joy",
    },
}

# ==========================================
# 3. MAIN LAYOUT: TABS
# ==========================================
tab_order, tab_guide = st.tabs(["🧾 Place Your Order ", "📖 The 6 HK Archetypes"])

with tab_order:
    # Two-column layout: Left = Interactive Order Counter, Right = Live Waiter Order Chit
    col_menu, col_ticket = st.columns([1.7, 1], gap="large")

    with col_menu:
        customer_name = st.text_input("Customer Name  (Optional)", placeholder="e.g., Ben")

        # ------------------------------------------
        # STEP 1: CHOOSE SET A–H
        # ------------------------------------------
        st.subheader("1️⃣ Choose Your Breakfast Set ")
        selected_set = st.radio(
            "Select one set from the menu:",
            list(MENU_SETS.keys()),
        )
        set_info = MENU_SETS[selected_set]
        total_bill = set_info["price"]
        ticket_lines = [f"• {selected_set.split(' — ')[0]}: {selected_set.split(' — ')[1]} (${set_info['price']})"]

        # Conditional toppings for Set D (雙拼粉麵餐)
        double_toppings = []
        if "Set D" in selected_set:
            double_toppings = st.multiselect(
                "Choose 2 toppings for Set D (雙拼自選兩款配料):",
                [
                    "五香肉丁 / 午餐肉 (Luncheon Meat)",
                    "招牌沙爹牛肉 (Satay Beef)",
                    "秘製榨菜肉絲 (Pickled Mustard Greens & Pork)",
                    "煎雙蛋 (Fried Egg)",
                    "脆皮腸仔 (Sausage)",
                    "火腿片 (Ham)",
                ],
                default=["五香肉丁 / 午餐肉 (Luncheon Meat)", "招牌沙爹牛肉 (Satay Beef)"],
                max_selections=2,
            )
            if double_toppings:
                ticket_lines.append(f"  └ 雙拼配料: {' + '.join([t.split(' (')[0] for t in double_toppings])}")

        st.divider()

        # ------------------------------------------
        # STEP 2: CONDITIONAL NOODLE / MACARONI BASE
        # ------------------------------------------
        st.subheader("2️⃣ Noodle / Macaroni Base")
        noodle_choice = None

        if set_info["has_noodle"]:
            noodle_options = [
                "通粉 (Macaroni)",
                "米粉 (Rice Vermicelli)",
                "公仔麵 (Standard Instant Noodle)",
                "轉配出前一丁 (+$5) (Upgrade to Demae Iccho)",
            ]
            default_idx = noodle_options.index(set_info["default_noodle"])
            noodle_choice = st.selectbox(
                "Choose your noodle/macaroni base for this set:",
                noodle_options,
                index=default_idx,
            )
            if "+$5" in noodle_choice:
                total_bill += 5
                ticket_lines.append("• 轉配出前一丁 (+$5)")
            else:
                ticket_lines.append(f"•  {noodle_choice.split(' (')[0]}")
        else:
            st.info(
                "🚫 **No noodle selection needed for this set!** "
                "(Sets E, F, G, and H are Oatmeal or Continental platters served directly with bread/toast and eggs.)"
            )
            ticket_lines.append("• 粉麵底: 不適用 (Set excludes noodles)")

        st.divider()

        # ------------------------------------------
        # STEP 3: SIDE DISH (EGG + BREAD)
        # ------------------------------------------
        st.subheader("3️⃣ Side Dish: Egg & Bread Pairing")
        egg_choice = None
        bread_choice = None
        sandwich_toast_opt = None

        if set_info["side_mode"] == "standard":
            c_egg, c_bread = st.columns(2)
            with c_egg:
                egg_options = [
                    "嫩滑炒蛋 (Smooth Scrambled Egg)",
                    "太陽蛋 / 煎雙蛋 (Sunny-Side Up / Double Fried Egg)",
                    "烚蛋 / 全熟煎蛋 (Boiled / Well-Done Egg)",
                ]
                egg_choice = st.selectbox(
                    "Egg Style :",
                    egg_options,
                    index=egg_options.index(set_info["default_egg"]),
                )
            with c_bread:
                bread_options = [
                    "Top One 丹麥酥 (Top One Danish Toast)",
                    "自家製鮮油餐包 (Homemade Butter Bun)",
                    "牛油多士 (Butter Toast)",
                    "牛油多士・烘底 (Toasted Butter Bread)",
                    "嫩滑炒蛋三文治 (Scrambled Egg Sandwich)",
                ]
                bread_choice = st.selectbox(
                    "Bread / Toast :",
                    bread_options,
                    index=bread_options.index(set_info["default_bread"]),
                )
            ticket_lines.append(f"• {egg_choice.split(' (')[0]} + {bread_choice.split(' (')[0]}")

        elif set_info["side_mode"] == "oatmeal_sandwich":
            st.write("Set E includes **嫩滑炒蛋三文治 (Smooth Scrambled Egg Sandwich)**.")
            sandwich_toast_opt = st.radio(
                "How would you like your sandwich bread?",
                ["唔烘底 (Soft White Bread)", "烘底 (Toasted Crispy Bread)"],
                horizontal=True,
            )
            ticket_lines.append(f"•嫩滑炒蛋三文治 ({sandwich_toast_opt.split(' (')[0]})")

        elif set_info["side_mode"] == "all_day_fixed":
            st.success("Set H automatically includes **黑松露炒蛋 (Black Truffle Scrambled Egg) + Top One 丹麥酥**.")
            ticket_lines.append("• 黑松露炒蛋 + Top One 丹麥酥")

        st.divider()

        # ------------------------------------------
        # STEP 4: DRINKS + HOT/ICED + SWEETNESS
        # ------------------------------------------
        st.subheader("4️⃣ Morning Drink, Temperature & Sweetness")
        c_drink, c_temp = st.columns(2)

        with c_drink:
            drink_choice = st.selectbox(
                "Choose Drink :",
                [
                    "招牌檸茶 (Signature Lemon Tea)",
                    "香濃絲襪奶茶 (Milk Tea)",
                    "鴛鴦 (Yuanyang — Coffee & Tea)",
                    "香濃港式咖啡 (Coffee)",
                    "檸水 (Lemon Water)",
                    "阿華田 / 好立克 (Ovaltine / Horlicks)",
                    "西洋菜蜜 (Watercress Honey)",
                    "紅豆冰 / 特色特飲 (+$6) (Red Bean Ice / Special Drink)",
                ],
            )

        with c_temp:
            temp_choice = st.selectbox(
                "Hot or Iced :",
                [
                    "熱飲 (Hot — $0)",
                    "凍飲 (+$3) (Iced)",
                    "凍飲・少冰 (+$3) (Iced — Less Ice)",
                    "凍飲・走冰 (+$3) (Iced — No Ice)",
                ],
            )

        sweetness_choice = st.radio(
            "Sweetness & Milk Modifier :",
            [
                "走甜 (Zero Sugar — pure tea/lemon, zero syrup)",
                "少甜 (Less Sweet — lightly balanced)",
                "正常甜 (Regular — standard sweetness)",
                "飛砂走奶 (Black — no sugar, no milk)",
                "茶走 / 啡走 (Condensed Milk instead of sugar & evaporated milk)",
            ],
        )

        drink_extra = 0
        if "+$6" in drink_choice:
            drink_extra += 6
        if "+$3" in temp_choice:
            drink_extra += 3
        total_bill += drink_extra

        drink_short = drink_choice.split(" (")[0]
        temp_short = temp_choice.split(" (")[0]
        sweet_short = sweetness_choice.split(" (")[0]
        extra_str = f" (+${drink_extra})" if drink_extra > 0 else ""
        ticket_lines.append(f"•  {temp_short}・{drink_short} [{sweet_short}]{extra_str}")

        st.divider()

        # ------------------------------------------
        # STEP 5: EXTRA ADD-ONS & SANDWICHES
        # ------------------------------------------
        st.subheader("5️⃣ Extra Add-Ons & Sandwiches ")
        addons_selected = st.multiselect(
            "Want anything extra on the table? (Optional)",
            list(ADDON_PRICES.keys()),
        )
        for item in addons_selected:
            item_price = ADDON_PRICES[item]
            total_bill += item_price
            ticket_lines.append(f"• {item.split(' (+$')[0]} (+${item_price})")

        st.divider()

        # Dining Pace Slider
        pace_slider = st.slider(
            "⏱️ Your Cha Chaan Teng Table Pace (1 = Slow weekend brunch, 10 = 10-minute MTR dash):",
            min_value=1,
            max_value=10,
            value=5,
        )

    # ------------------------------------------
    # RIGHT COLUMN: LIVE WAITER ORDER CHIT 
    # ------------------------------------------
    with col_ticket:
        st.markdown("### 🧾 Live Order Ticket")
        with st.container(border=True):
            st.caption("TABLE #12 · 醒晨早餐 (7:00AM – 11:30AM)")
            if customer_name.strip():
                st.write(f"Guest: {customer_name.strip()}")
            st.divider()
            for line in ticket_lines:
                st.write(line)
            st.divider()
            st.metric(label="Total Bill ", value=f"HK$ {total_bill}")
            st.caption("Cash / Octopus / AlipayHK accepted")

        reveal_btn = st.button(
            "🔍 Analyze My Order & Reveal Personality",
            type="primary",
            use_container_width=True,
        )
        st.caption("Scroll down to check the result!")

    # ==========================================
    # 4. SCORING ENGINE & RESULT DISPLAY
    # ==========================================
    if reveal_btn:
        scores = {key: 0 for key in ARCHETYPES}

        # 1. Score Set Selection
        if "Set A" in selected_set:
            scores["KowloonPurist"] += 4
            scores["QueueMaximizer"] += 3
        elif "Set B" in selected_set:
            scores["DemaePerfectionist"] += 2
            scores["QueueMaximizer"] += 3
            scores["KowloonPurist"] += 4
        elif "Set C" in selected_set:
            scores["CentralSpeedrunner"] += 2
            scores["KowloonPurist"] += 2
        elif "Set D" in selected_set:
            scores["QueueMaximizer"] += 4
        elif "Set E" in selected_set:
            scores["ComfortHedonist"] += 4
        elif any(x in selected_set for x in ["Set F", "Set G", "Set H"]):
            scores["ComfortHedonist"] += 4
            if "Set H" in selected_set:
                scores["DanishRomantic"] += 2

        # 2. Score Conditional Noodle Choice
        if noodle_choice:
            if "出前一丁" in noodle_choice:
                scores["DemaePerfectionist"] += 8
            elif "通粉" in noodle_choice:
                scores["KowloonPurist"] += 3
                scores["CentralSpeedrunner"] += 2
            elif "米粉" in noodle_choice:
                scores["CentralSpeedrunner"] += 4
                scores["KowloonPurist"] += 3
            elif "公仔麵" in noodle_choice:
                scores["QueueMaximizer"] += 3

        # 3. Score Egg & Bread / Sandwich
        if egg_choice:
            if "嫩滑炒蛋" in egg_choice:
                scores["KowloonPurist"] += 2
                scores["CentralSpeedrunner"] += 2
            elif "太陽蛋" in egg_choice:
                scores["KowloonPurist"] += 2
                scores["CentralSpeedrunner"] += 2
                scores["QueueMaximizer"] += 3
            elif "烚蛋" in egg_choice:
                scores["ComfortHedonist"] += 2

        if bread_choice:
            if "丹麥酥" in bread_choice:
                scores["DanishRomantic"] += 4
            elif "鮮油餐包" in bread_choice:
                scores["KowloonPurist"] += 3
            elif "烘底" in bread_choice:
                scores["DemaePerfectionist"] += 2
                scores["KowloonPurist"] += 2
            elif "三文治" in bread_choice:
                scores["QueueMaximizer"] += 2


        # 4. Score Drink, Temperature & Sweetness
        if "檸茶" in drink_choice or "檸水" in drink_choice:
            scores["KowloonPurist"] += 2
            scores["CentralSpeedrunner"] += 3
            scores["QueueMaximizer"] += 3
        elif "絲襪奶茶" in drink_choice:
            scores["KowloonPurist"] += 3
            scores["CentralSpeedrunner"] += 3
        elif "鴛鴦" in drink_choice:
            scores["KowloonPurist"] += 4
        elif "咖啡" in drink_choice:
            scores["CentralSpeedrunner"] += 3
        elif "阿華田" in drink_choice or "西洋菜蜜" in drink_choice:
            scores["KowloonPurist"] += 4
        elif "紅豆冰" in drink_choice:
            scores["ComfortHedonist"] += 4

        if "走冰" in temp_choice:
            scores["QueueMaximizer"] += 2
            scores["CentralSpeedrunner"] += 1
        elif "少冰" in temp_choice:
            scores["QueueMaximizer"] += 1
            scores["CentralSpeedrunner"] += 1

        if "走甜" in sweetness_choice:
            scores["DemaePerfectionist"] += 1
            scores["KowloonPurist"] += 2
            scores["CentralSpeedrunner"] += 1
        elif "少甜" in sweetness_choice:
            scores["DanishRomantic"] += 2
            scores["QueueMaximizer"] += 2
        elif "正常甜" in sweetness_choice:
            scores["ComfortHedonist"] += 2
            scores["KowloonPurist"] += 2
        elif "飛砂走奶" in sweetness_choice:
            scores["CentralSpeedrunner"] += 3
            scores["DemaePerfectionist"] += 3
        elif "茶走" in sweetness_choice:
            scores["KowloonPurist"] += 3
            scores["ComfortHedonist"] += 2

        # 5. Score Add-ons
        if addons_selected:
            scores["ComfortHedonist"] += len(addons_selected) * 2
            if any("公司三文治" in a or "餐蛋治" in a for a in addons_selected):
                scores["ComfortHedonist"] += 2

        # 6. Score Pace
        if pace_slider >= 8:
            scores["CentralSpeedrunner"] += 3
        elif pace_slider <= 3:
            scores["DanishRomantic"] += 3
            scores["ComfortHedonist"] += 2

        # Winner Calculation
        winner_key = max(scores, key=scores.get)
        result = ARCHETYPES[winner_key]
        display_name = customer_name.strip() if customer_name.strip() else "Fellow Foodie"

        st.divider()
        st.balloons()
        st.success(f"## 🎉 {display_name}, you are: **{result['title']}**")
        st.caption(f"*{result['tagline']}*")

        res_col1, res_col2 = st.columns([2.2, 1])
        with res_col1:
            st.write(result["desc"])
        with res_col2:
            st.metric(label="Signature Trait", value=result["trait_label"])
            st.metric(label="Breakfast Bill", value=f"HK$ {total_bill}")

        st.markdown("#### 📊 Your Cha Chaan Teng Trait Breakdown")
        max_score = max(scores.values()) or 1
        for key, info in ARCHETYPES.items():
            pct = min(int((scores[key] / max_score) * 100), 100)
            st.write(f"**{info['title'].split(' · ')[0]}** ({pct}%)")
            st.progress(pct / 100)

with tab_guide:
    st.markdown("### The 6 Hong Kong Cha Chaan Teng Archetypes")
    st.write("Explore all six personality types derived from authentic Hong Kong breakfast ordering habits:")
    for info in ARCHETYPES.values():
        with st.expander(info["title"]):
            st.write(f"**Motto:** *{info['tagline']}*")
            st.write(info["desc"])