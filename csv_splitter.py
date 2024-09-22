import pandas as pd
import math

# input fil
input_file_path = 'C:\\Users\\vetle\\OneDrive\\Dokumenter\\Skole\\BigData\\raw\\psam_ca2.csv'
output_file_base = 'psam_ca2_part_'  # output fil

# leser csv fil
df = pd.read_csv(input_file_path)

# teller antall rader og deler på 8 
num_rows = len(df)
num_pieces = 8
rows_per_piece = math.ceil(num_rows / num_pieces)

# Splitter csvfilen i 8 deler
for i in range(num_pieces):
    start_row = i * rows_per_piece
    end_row = start_row + rows_per_piece
    piece_df = df[start_row:end_row]
    output_file_path = f"{output_file_base}{i+1}.csv"
    piece_df.to_csv(output_file_path, index=False)
    print(f"Saved {output_file_path}")

print("CSV file has been split into 8 pieces.")