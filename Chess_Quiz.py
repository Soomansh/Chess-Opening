elif page == "Chess_Quiz":

    st.title("♟️ Chess Opening Decider")
    st.write("Answer a few questions and get your best chess openings.")

    # =========================================================
    # QUIZ
    # =========================================================

    skill = st.selectbox("Skill level", ["Beginner", "Intermediate", "Advanced"])
    style = st.selectbox("Play style", ["Defensive", "Positional", "Aggressive"])
    color = st.selectbox("Color", ["White", "Black"])
    aggressiveness = st.slider("Aggressiveness level", 0, 10, 5)

    time_control = st.selectbox("Time control", ["Bullet", "Blitz", "Rapid", "Classical"])
    risk = st.selectbox("Risk preference", ["Low", "Medium", "High"])
    goal = st.selectbox("Main goal", ["Tactics", "Strategy", "Endgames", "Opening knowledge"])

    # =========================================================
    # AI SCORING SYSTEM
    # =========================================================

    openings_score = {
        "Italian Game": 0,
        "Queen's Gambit": 0,
        "Sicilian Defense": 0,
        "Scotch Game": 0,
        "Vienna Game": 0
    }

    if aggressiveness >= 7:
        openings_score["Italian Game"] += 3
        openings_score["Scotch Game"] += 3
        openings_score["Sicilian Defense"] += 3
        openings_score["Vienna Game"] += 2

    elif aggressiveness >= 4:
        openings_score["Queen's Gambit"] += 3
        openings_score["Italian Game"] += 2
        openings_score["Vienna Game"] += 2

    else:
        openings_score["Queen's Gambit"] += 3

    if risk == "High":
        openings_score["Sicilian Defense"] += 2
        openings_score["Scotch Game"] += 2

    elif risk == "Low":
        openings_score["Queen's Gambit"] += 2
        openings_score["Italian Game"] += 1

    if style == "Defensive":
        openings_score["Queen's Gambit"] += 2

    elif style == "Aggressive":
        openings_score["Sicilian Defense"] += 2
        openings_score["Scotch Game"] += 2

    if color == "White":
        openings_score["Italian Game"] += 2
        openings_score["Queen's Gambit"] += 2

    else:
        openings_score["Sicilian Defense"] += 2

    # =========================================================
    # RESULTS
    # =========================================================

    if st.button("Get Recommendation"):

        sorted_openings = sorted(openings_score.items(), key=lambda x: x[1], reverse=True)
        top_openings = [x[0] for x in sorted_openings[:3]]

        st.subheader("Your Best Opening Matches")

        for i, opening in enumerate(top_openings, 1):
            st.success(f"{i}. {opening}")

        st.info("Go to Opening Explorer for full breakdowns.")

    st.caption(f"Profile: {style} | Aggression {aggressiveness}/10 | Goal: {goal}")

    st.button("⬅ Back Home", on_click=go, args=("Home",))
