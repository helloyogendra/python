#Pandas

import pandas as pd

df = pd.read_csv("data.csv")

print(type(df))
print(df.loc[0])
#print(df)

print(pd.options.display.max_rows)  #it is 60, so if "total rows" > 60 then the print will print 5 first rows and 5 last rows
pd.options.display.max_rows = 200   #change the display

#head() - returns the headesr and number of rows from top

result = df.head(7)
print(result)

result = df.head()  #if the number of rows to return is not specified, it will select first 5 rows
print(result)


result = df.tail()  #get last 5 rows from this dataframe
print(result)

print(df.info())    #get information about data

print(df)

df = pd.read_json("data.js")
print(type(df))
print(df.loc[0])

