import zstandard as zstd

input_file = r"C:\Users\********* \Downloads\lichess_db_puzzle.csv.zst"
output_file = r"C:\chess_data\lichess_db_puzzle.csv"

dctx = zstd.ZstdDecompressor()

with open(input_file, "rb") as f_in:
    with open(output_file, "wb") as f_out:
        dctx.copy_stream(f_in, f_out) 

print("EXTRACTION DONE") 

