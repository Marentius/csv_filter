import pandas as pd

# Yo peeps. Dette skriptet leser inn en csv-fil og filtrerer ut de kolonnene vi vil bruke.

# For å bruke scriptet må dere huske å endre input_file_path tilpasset deres lokale filsti. 
input_file_path = 'C:\\Users\\vetle\\OneDrive\\Dokumenter\\Skole\\BigData\\raw\\psam_p06.csv'
output_file_path = 'filtrert.csv'  # Dette er output-fila 

# Her kan dere definere hvilke kolonner dere vil beholde 
columns_to_keep = ['SCHL', 'SCHG', 'POVPIP', 'WKL', 'FOD1P']

# Ikke rør noe under her
df = pd.read_csv(input_file_path)

# Filtrer kolonnene og fyll NA-verdier med 0 før konvertering til int
filtered_df = df[columns_to_keep].fillna(0).astype(int)

filtered_df.to_csv(output_file_path, index=False)

print(f"Filtered data saved to {output_file_path}")