#Pandas

import pandas as pd

dataset = {
    'fruits' : ['apple', 'banana', 'cherry'],
    'calories' : [57, 65, 25]
}

my_dataframe = pd.DataFrame(dataset)   #creating a pandas dataframe object(like a table data), passing a dictionary object to pandas-function

print(type(my_dataframe))
print(my_dataframe)


list1 = [55, 45, 56, 76, 23]

my_series = pd.Series(list1)         #creating a pandas series object(like a 1D array or a single column), passing a list object to pandas-function

print(type(my_series))
print(my_series)

print(my_series[1])   #pass the index to access a value

#we can create labels for our series
series1 = pd.Series(list1, index=["A", "B", "C", "D", "E"])

print(series1["B"])   #now we can pass the label to access a value from a pandas-series


#we can create a series using a python-dictionary

daily_stuff = { "mon": 50, "tue": 100, "wed": 200, "thu" : 300, "fri": 400}

series2 = pd.Series(daily_stuff)  # keys from dictionary object will be treated like labels

print(series2)
print(series2[0])   #inside series we passed a dictioanry, this index will produce the value only at index 0, not the key

print(series2["wed"])    #passing a label/key


series3 = pd.Series(daily_stuff, index=["mon", "wed", "fri"])  # just select some of the dictionary items to create a series and not everything
print(series3)
