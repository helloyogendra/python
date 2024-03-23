#Pandas
#Data Cleaning

import pandas as pd

df = pd.read_csv("data.csv")
print(df.info())

#Removing thw rows - dropna() - return a new dataframe object with no empty cells

newDF = df.dropna()   #to modify the original dataframe, which is df here, we can call it like - df.dropna(inplace=True)

# df.dropna(inplace=True)

print(newDF.info())

#replacing the null or empty values using -  fillna()

df.fillna(111, inplace=True)
print(df.info())

df2 = df["Calories"].fillna(115)  #target the "Calories" column only, replace empty values with 115


#Mean=average, Median=mid point, Mode=most common

median_result = df.median()   #returns a series with the median value fo each column
print(median_result)

mode_result = df.mode()   
print(mode_result)

mean_result = df.mean()   
print(mean_result)


f2 = df["Calories"].fillna(mean_result)  #target the "Calories" column only, replace empty values with the "mean_result"



