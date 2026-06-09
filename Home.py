import streamlit as st

st.set_page_config(
    page_title="Chess Hub",
    page_icon="♟️",
    layout="wide"
)

# ---------------- SESSION STATE ----------------
if "page" not in st.session_state:
    st.session_state.page = "Home"


def go(page_name):
    st.session_state.page = page_name


page = st.session_state.page


# ================= HOME =================
if page == "Home":

    st.title("♟️ Chess Hub")
    st.subheader("Learn • Train • Analyze • Improve")

    st.markdown("---")

    st.write("""
    Welcome to your chess platform.

    Everything is connected here:
    - Learn openings in depth
    - Practice positions on a board 
    - Play against Stockfish AI
    - Review full games like Chess.com
    """)

    st.markdown("---")

    st.header("Open Tools")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Learning")

        if st.button("♟️ Chess Quiz"):
            go("Chess_Quiz")
            st.rerun()

        if st.button("Opening Explorer"):
            go("Opening_Explorer")
            st.rerun()

        if st.button("📊 Guess the Elo"):
            go("Guess_Elo")
            st.rerun()

    with col2:
        st.subheader("Training & Analysis")

        if st.button("Board Visualizer"):
            go("Board_Visualizer")
            st.rerun()

        if st.button("Play vs AI"):
            go("Play_AI")
            st.rerun()

        if st.button("Chess Games Review"):
            go("Game_Review")
            st.rerun()

        if st.button("Endgame Puzzles"):
            go("Endgames")
            st.rerun()

        if st.button("Learn Endgames"):
            go("Learn_Endgames")
            st.rerun()


# ================= CHESS QUIZ =================
elif page == "Chess_Quiz":
    st.title("♟️ Chess Quiz")

    st.write("Your Chess Quiz app goes here.")

    if st.button("⬅ Back Home"):
        go("Home")
        st.rerun()


# ================= OPENING =================
elif page == "Opening_Explorer":
    st.title("📖 Opening Explorer")

    st.write("Your Opening Explorer app goes here.")

    if st.button("⬅ Back Home"):
        go("Home")
        st.rerun()


# ================= GUESS ELO =================
elif page == "Guess_Elo":
    st.title("📊 Guess The Elo")

    st.write("Your Guess The Elo app goes here.")

    if st.button("⬅ Back Home"):
        go("Home")
        st.rerun()


# ================= BOARD =================
elif page == "Board_Visualizer":
    st.title("📊 Board Visualizer")

    st.write("Your Board Visualizer goes here.")

    if st.button("⬅ Back Home"):
        go("Home")
        st.rerun()


# ================= AI =================
elif page == "Play_AI":
    st.title("♜ Play vs AI")

    st.write("Your AI chess game goes here.")

    if st.button("⬅ Back Home"):
        go("Home")
        st.rerun()


# ================= REVIEW =================
elif page == "Game_Review":
    st.title("📊 Game Review")

    st.write("Your Game Review goes here.")

    if st.button("⬅ Back Home"):
        go("Home")
        st.rerun()


# ================= ENDGAMES =================
elif page == "Endgames":
    st.title("🧩 Endgame Puzzles")

    st.write("Your Endgame Puzzles go here.")

    if st.button("⬅ Back Home"):
        go("Home")
        st.rerun()


# ================= LEARN ENDGAMES =================
elif page == "Learn_Endgames":
    st.title("📚 Learn Endgames")

    st.write("Your Endgame Lessons go here.")

    if st.button("⬅ Back Home"):
        go("Home")
        st.rerun()
