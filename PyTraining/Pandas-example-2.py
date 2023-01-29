#Pandas

import pandas as pd

dataset = {
    'fruits' : ['apple', 'banana', 'cherry'],
    'calories' : [57, 65, 25]
}

df = pd.DataFrame(dataset)   #creating a pandas dataframe object(like a table data), passing a dictionary object to pandas-function

print(df)


# loc() = Locate Row - it can return one or more specified row/rows

row = df.loc[1]
print(row)
print(type(row))            #we are getting a series here

rows = df.loc[ [0, 1] ]     #it will return data from row 0 and 1, we are passing index like a list
print(rows)
print(type(rows))           #dataframe object


#We can define labels for dataframe index also

df1 = pd.DataFrame(dataset, index=["Mon", "Tue", "Wed"])
print(df1)

row = df1.loc["Wed"]  #use the named index to locate a row
print(row)

