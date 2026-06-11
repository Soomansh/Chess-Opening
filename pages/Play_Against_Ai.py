import streamlit as st
import chess
import chess.svg
import chess.engine

# ==================================================================================================================
# STOCKFISH SETUP
# ============================================================================================================================
 
STOCKFISH_PATH = "stockfish/stockfish"

def load_engine():
    return chess.engine.SimpleEngine.popen_uci(STOCKFISH_PATH)

if "engine" not in st.session_state:
    st.session_state.engine = load_engine()

engine = st.session_state.engine

# ==================================================================================================================================
# BOARD STATE
# ===========================================================================================================================================================================

if "board" not in st.session_state:
    st.session_state.board = chess.Board()

board = st.session_state.board

# =================================================================================================================================================
# OPENINGS
# ===========================================================================================================================================================================

openings = {
    "Italian Game": ["e4","e5","Nf3","Nc6","Bc4","Bc5"],
    "Queen's Gambit": ["d4","d5","c4","e6"],
    "London System": ["d4","d5","Bf4","Nf6","e3"],
    "Sicilian Defense": ["e4","c5","Nf3","d6"],
    "French Defense": ["e4","e6","d4","d5"]
}

st.title("♟️ Board Trainer + Stockfish Analyzer")

# =========================================================================================================================================================
# OPENING SELECTOR
# ===============================================================================================================================================================

opening = st.selectbox("Choose Opening", list(openings.keys()))

if "current_opening" not in st.session_state:
    st.session_state.current_opening = opening

if st.session_state.current_opening != opening:
    st.session_state.current_opening = opening
    st.session_state.board = chess.Board()

board = st.session_state.board

# =========================================================================================================================================
# CONTROLS
# ==================================================================================================================

col1, col2 = st.columns(2)

with col1:
    if st.button("⬅ Undo"):
        if board.move_stack:
            board.pop()
        st.session_state.board = board
        st.rerun()

with col2:
    if st.button("♻ Reset"):
        st.session_state.board = chess.Board()
        st.rerun()

# ==============================================================================================================================================
# OPENING TRAINER
# ===============================================================================================================================================

st.subheader("Opening Trainer")

moves = openings[opening]
step = len(board.move_stack)

if step < len(moves):
    st.write(f"Next Move: **{moves[step]}**")

    if st.button("▶ Play Next Move"):
        board.push_san(moves[step])
        st.session_state.board = board
        st.rerun()

# ============================================================================================================================================
# USER MOVE SECTION
# =====================================================================================================================================================

st.markdown("---")
st.subheader("Play Your Move")

legal_moves = list(board.legal_moves)
move_options = [board.san(m) for m in legal_moves]

user_move = st.selectbox("Select your move", move_options)

if st.button("Make Move"):
    try:
        # Player move
        board.push_san(user_move)

        # Stockfish response
        result = engine.play(board, chess.engine.Limit(time=0.2))
        board.push(result.move)

        st.session_state.board = board
        st.rerun()

    except Exception as e:
        st.error(f"Move error: {e}")

# ==================================================================================================================================
# STOCKFISH ANALYSIS
# ==================================================================================================================

st.markdown("---")
st.subheader("Stockfish Analysis")

level = st.selectbox("Engine Strength", ["400","800","1200","1600","2000"])

depth_map = {
    "400": 1,
    "800": 2,
    "1200": 5,
    "1600": 10,
    "2000": 15
}

depth = depth_map[level]

def get_best_move(board):
    info = engine.analyse(board, chess.engine.Limit(depth=depth))
    return info["pv"][0]

# =============================================================================================================
# BOARD DISPLAY
# ==================================================================================================================

arrows = []

if not board.is_game_over():
    try:
        best = get_best_move(board)
        arrows = [(best.from_square, best.to_square)]
    except:
        pass

svg = chess.svg.board(board=board, size=600, arrows=arrows, coordinates=True)
st.components.v1.html(svg, height=650)

# ==================================================================================================================
# MOVE HISTORY
# ================================================================================================================

st.subheader("Move History")

temp = chess.Board()
history = []

for move in board.move_stack:
    history.append(temp.san(move))
    temp.push(move)

st.write(" ".join(history))

# =============================================================================================================================
# ANALYZE BUTTON
# =====================================================================================================================================================

if st.button("Analyze Position"):
    try:
        info = engine.analyse(board, chess.engine.Limit(depth=depth))
        best = info["pv"][0]
        st.success(f"Best Move: {board.san(best)}")
    except:
        st.error("Analysis failed")

# ============================================================================================================================================
# STATUS
# ==============================================================================================================================================

if board.is_checkmate():
    st.error("Checkmate!")
elif board.is_stalemate():
    st.warning("Stalemate!")
elif board.is_check():
    st.info("Check!")
