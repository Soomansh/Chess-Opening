import streamlit as st

st.set_page_config(
    page_title="Chess Hub",
    page_icon="♟️",
    layout="wide"
)

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

st.success("""
Use the sidebar on the left to navigate between all Chess Hub tools.

Available pages:
• Chess Quiz
• Opening Explorer
• Board Visualizer
• Play vs AI
• Endgame Puzzles
• Learn Endgames
• Guess The Elo
• Review Chess Games
""")

st.markdown("---")

st.header("What this platform does")

st.info("""
1. Opening learning system
2. Quiz-based training
3. Board practice tools
4. AI opponent (Stockfish)
5. Full game review system
6. Endgame puzzles
7. Endgame learning system
8. Guess the Elo training
""")

st.markdown("---")

st.write("Streamlit version:", st.__version__)

st.caption("♟️ Chess Hub • Python • Streamlit • Stockfish")
