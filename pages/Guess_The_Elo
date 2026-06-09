import streamlit as st
import chess
import chess.pgn
import chess.svg
import random

st.set_page_config(page_title="Guess The Elo", layout="wide")

PGN_PATH = r"C:\Users\********\Downloads\lichess_db_standard_rated_2026-05.pgn\lichess_db_standard_rated_2026-05.pgn"
MAX_GAMES = 500


@st.cache_data
def load_games(path, max_games=500):
    games = []
    with open(path, encoding="utf-8", errors="ignore") as pgn:
        count = 0
        while count < max_games:
            game = chess.pgn.read_game(pgn)
            if game is None:
                break

            try:
                white_elo = int(game.headers.get("WhiteElo", 0))
                black_elo = int(game.headers.get("BlackElo", 0))
            except:
                continue

            moves = list(game.mainline_moves())
            if len(moves) < 10:
                continue

            games.append({
                "moves": moves,
                "white_elo": white_elo,
                "black_elo": black_elo,
                "avg_elo": (white_elo + black_elo) // 2,
                "opening": game.headers.get("Opening", "Unknown Opening"),
                "result": game.headers.get("Result", "Unknown"),
                "event": game.headers.get("Event", "Unknown Event"),

                # NEW: Time control field
                "time_control": game.headers.get("TimeControl", "Unknown"),
            })
            count += 1

    return games


def elo_bucket(elo):
    if elo < 800:
        return "400-800"
    elif elo < 1200:
        return "800-1200"
    elif elo < 1600:
        return "1200-1600"
    elif elo < 2000:
        return "1600-2000"
    return "2000+"


# NEW: classify time control
def classify_time_control(tc):
    if tc == "Unknown":
        return "Unknown"

    try:
        base = int(tc.split("+")[0])

        if base < 180:
            return "Bullet"
        elif base < 600:
            return "Blitz"
        elif base < 1800:
            return "Rapid"
        else:
            return "Classical"

    except:
        return "Unknown"


games = load_games(PGN_PATH, MAX_GAMES)

if not games:
    st.error("No games loaded.")
    st.stop()

if "game" not in st.session_state:
    st.session_state.game = random.choice(games)

if "move_index" not in st.session_state:
    st.session_state.move_index = 0

if "revealed" not in st.session_state:
    st.session_state.revealed = False

if "score" not in st.session_state:
    st.session_state.score = 0

if "questions" not in st.session_state:
    st.session_state.questions = 0


game = st.session_state.game
moves = game["moves"]

board = chess.Board()
for move in moves[:st.session_state.move_index]:
    board.push(move)

left, right = st.columns([2, 1])

with left:
    st.title("Guess The Elo - Full Game")

    svg = chess.svg.board(board=board, size=700)
    st.components.v1.html(svg, height=720)

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        if st.button("<< Start"):
            st.session_state.move_index = 0
            st.rerun()

    with c2:
        if st.button("< Previous"):
            st.session_state.move_index = max(0, st.session_state.move_index - 1)
            st.rerun()

    with c3:
        if st.button("Next >"):
            st.session_state.move_index = min(len(moves), st.session_state.move_index + 1)
            st.rerun()

    with c4:
        if st.button("End >>"):
            st.session_state.move_index = len(moves)
            st.rerun()

    st.write(f"Move: {st.session_state.move_index}/{len(moves)}")

    move_text = []
    temp = chess.Board()

    for i, mv in enumerate(moves):
        san = temp.san(mv)
        temp.push(mv)

        if i % 2 == 0:
            move_text.append(f"{i//2+1}. {san}")
        else:
            move_text[-1] += f" {san}"

    st.text_area(
        "Moves",
        " ".join(move_text),
        height=200
    )

with right:

    # NEW: Game information shown before guessing
    st.subheader("Game Information")

    time_type = classify_time_control(game["time_control"])

    st.write(f"• Time Control Type: {time_type}")
    st.write(f"• Time Control: {game['time_control']}")

    guess = st.radio(
        "Guess Elo Range",
        ["400-800", "800-1200", "1200-1600", "1600-2000", "2000+"],
    )

    if st.button("Submit Guess"):
        st.session_state.questions += 1
        st.session_state.revealed = True

        if guess == elo_bucket(game["avg_elo"]):
            st.session_state.score += 1
            st.success("Correct!")
        else:
            st.error("Incorrect")

    if st.session_state.revealed:
        st.subheader("Results")
        st.write("Actual Range:", elo_bucket(game["avg_elo"]))
        st.write("Average Elo:", game["avg_elo"])
        st.write("White Elo:", game["white_elo"])
        st.write("Black Elo:", game["black_elo"])
        st.write("Opening:", game["opening"])
        st.write("Result:", game["result"])
        st.write("Event:", game["event"])

    st.divider()

    accuracy = 0
    if st.session_state.questions:
        accuracy = (st.session_state.score / st.session_state.questions) * 100

    st.metric("Score", st.session_state.score)
    st.metric("Questions", st.session_state.questions)
    st.metric("Accuracy", f"{accuracy:.1f}%")

    if st.button("Random New Game"):
        st.session_state.game = random.choice(games)
        st.session_state.move_index = 0
        st.session_state.revealed = False
        st.rerun()
