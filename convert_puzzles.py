import csv
import json

INPUT = r"C:\chess_data\lichess_db_puzzle.csv"
OUTPUT = r"C:\Users\********\OneDrive\Desktop\Python\******** Test\Basic\chess\puzzles.json"

INPUT = r"C:\chess_data\lichess_db_puzzle.csv"
MAX_PUZZLES = 10000

puzzles = []

with open(INPUT, "r", encoding="utf-8") as f:
    reader = csv.reader(f)

    for i, row in enumerate(reader):

        if i == 0:
            continue

        try:
            puzzles.append({
                "id": row[0],
                "fen": row[1],
                "moves": row[2].split(" "),
                "rating": int(row[3]),
                "themes": row[7] if len(row) > 7 else ""
            })

        except:
            continue

        if len(puzzles) >= MAX_PUZZLES:
            break

with open(OUTPUT, "w", encoding="utf-8") as f:
    json.dump(puzzles, f)

print("DONE:", len(puzzles), "puzzles saved")
