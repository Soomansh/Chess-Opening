import streamlit as st
import chess
import chess.svg
import json
import random

PUZZLE_PATH = r"C:\Users\**************\OneDrive\Desktop\Python\Raji Test\Basic\chess\puzzles.json"

@st.cache_data
def load_puzzles():
    with open(PUZZLE_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

puzzles = load_puzzles()

if "puzzle" not in st.session_state:
    st.session_state.puzzle = random.choice(puzzles)

if "board" not in st.session_state:
    st.session_state.board = chess.Board(st.session_state.puzzle["fen"])

st.title("♟ Chess Puzzle Viewer (V1)")

board = st.session_state.board

svg = chess.svg.board(board=board, size=550)
st.image(svg)

st.write("Puzzle Rating:", st.session_state.puzzle.get("rating", "N/A"))

move_text = st.text_input("Enter move (UCI format)")

if st.button("Play Move"):
    try:
        move = chess.Move.from_uci(move_text)

        if move in board.legal_moves:
            board.push(move)
            st.success("Move played.")
        else:
            st.error("Illegal move.")

    except:
        st.error("Invalid move format.")

if st.button("Next Puzzle"):
    st.session_state.puzzle = random.choice(puzzles)
    st.session_state.board = chess.Board(st.session_state.puzzle["fen"])
    st.rerun()
