import pandas as pd
import os

os.system("cls")

df = pd.read_csv("Book1.csv")
print("data loaded")

# Function to fill missing "abcd" values for all IDs
def fill_missing_values(df):
    unique_ids = df['id'].unique()
    
    for id in unique_ids:
        mask = (df['id'] == id)

        abcd_values = df.loc[mask, 'abcd'].replace('', pd.NA)
        abcd_values = abcd_values.bfill().ffill().fillna('')

        val_values = df.loc[mask, 'val'].replace('', pd.NA)
        val_values = val_values.bfill().ffill().fillna('')

        df.loc[mask, 'abcd'] = abcd_values.values
        df.loc[mask, 'val'] = val_values.values
    
    return df

# Example usage
df = fill_missing_values(df)

# Show the resulting DataFrame
print(df)
