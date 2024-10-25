#Pandas - incorrect data format

import pandas as pd

df = pd.read_csv("data2.csv")
print(df.info())

df['Date'] = pd.to_datetime(df['Date'])

# print(df.to_string())

new_df = df.dropna(subset=["Date"])  #remove rows with a null value in the 'Date' column

df.loc[3, 'Duration'] = 60

print(df.index)

#updating multiple records, conditional update
def df_update(df):
    for idx in df.index:
        if df.loc[idx, 'Duration'] > 60:
            df.loc[idx, 'Duration'] = 60
    print(df.to_string())


#dropping records
def df_drop(df):
    for idx in df.index:
        if df.loc[idx, 'Duration'] > 60:
            df.drop(idx, inplace=True)
    print(df.to_string())



#get duplicate row info 
df2 = df.duplicated()
print(df2)

#removing duplicates

df.drop_duplicates(inplace=True)