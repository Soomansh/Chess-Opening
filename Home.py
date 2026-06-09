import streamlit as st

st.set_page_config(
    page_title="Chess Hub",
    page_icon="♟️",
    layout="wide"
)

# ---------------- SESSION NAV ----------------
if "page" not in st.session_state:
    st.session_state.page = "Home"


def go(page_name):
    st.session_state.page = page_name
    st.rerun()


# ---------------- HOME PAGE ----------------
if st.session_state.page == "Home":

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

    # ---------------- NAVIGATION ----------------
    st.header("Open Tools")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Learning")

        st.button("♟️ Chess Quiz", on_click=go, args=("Chess_Quiz",))
        st.button("Opening Explorer", on_click=go, args=("Opening_Explorer",))
        st.button("📊 Guess the Elo", on_click=go, args=("Guess_Elo",))

    with col2:
        st.subheader("Training & Analysis")

        st.button("Board Visualizer", on_click=go, args=("Board_Visualizer",))
        st.button("Play vs AI", on_click=go, args=("Play_AI",))
        st.button("Chess Games Review", on_click=go, args=("Game_Review",))
        st.button("Endgame Puzzles", on_click=go, args=("Endgames",))
        st.button("Learn Endgames", on_click=go, args=("Learn_Endgames",))


# ---------------- CHESS QUIZ ----------------
elif st.session_state.page == "Chess_Quiz":
    st.title("♟️ Chess Quiz")

    st.write("Your Chess Quiz app goes here.")

    st.button("⬅ Back Home", on_click=go, args=("Home",))


# ---------------- OPENING EXPLORER ----------------
elif st.session_state.page == "Opening_Explorer":
    st.title("📖 Opening Explorer")

    st.write("Your Opening Explorer app goes here.")

    st.button("⬅ Back Home", on_click=go, args=("Home",))


# ---------------- BOARD VISUALIZER ----------------
elif st.session_state.page == "Board_Visualizer":
    st.title("📊 Board Visualizer")

    st.write("Your Board Visualizer goes here.")

    st.button("⬅ Back Home", on_click=go, args=("Home",))


# ---------------- PLAY VS AI ----------------
elif st.session_state.page == "Play_AI":
    st.title("♜ Play vs AI")

    st.write("Your AI chess game goes here.")

    st.button("⬅ Back Home", on_click=go, args=("Home",))


# ---------------- GAME REVIEW ----------------
elif st.session_state.page == "Game_Review":
    st.title("📊 Game Review")

    st.write("Your Game Review goes here.")

    st.button("⬅ Back Home", on_click=go, args=("Home",))


# ---------------- ENDGAMES ----------------
elif st.session_state.page == "Endgames":
    st.title("🧩 Endgame Puzzles")

    st.write("Your Endgame Puzzles go here.")

    st.button("⬅ Back Home", on_click=go, args=("Home",))


# ---------------- LEARN ENDGAMES ----------------
elif st.session_state.page == "Learn_Endgames":
    st.title("📚 Learn Endgames")

    st.write("Your Endgame lessons go here.")

    st.button("⬅ Back Home", on_click=go, args=("Home",))


# ---------------- GUESS ELO ----------------
elif st.session_state.page == "Guess_Elo":
    st.title("📊 Guess The Elo")

    st.write("Your Guess the Elo game goes here.")

    st.button("⬅ Back Home", on_click=go, args=("Home",))
