import pandas as pd
import numpy as np

# 1
# 1.1
# iloc, loc attributes and get() method
#
def series_1():
    file = "C:\\Users\\hello\\pandas\\births1880.csv"

    dataframe = pd.read_csv(file, index_col="Names")
    series = pd.read_csv(file, index_col="Names").squeeze('columns')

    print(series.iloc[0])                   # iloc = index-location, error if index not found

    print(series.loc['Mel'])                # use 'loc' to access by location (index-label)
    print(series.loc[['Mel', 'Mary']])      # use 'loc' to access by multiple index-label, get values where index in ['Mel', 'Mary']

    print(series.get('Melo'))                   # no error if key/label-index not found, it will simply print 'None
    print(series.get('Melo', 'not exists'))     # no error if key/label-index not found, customize to print custom value instead of 'None'

    print(series.loc['Mel'])                    # error if key/label-index not found


#
series_1()
print()


# 1.2
# vector (series) vs scalar(atom) operation
#
def series_2():

    gen = np.random.default_rng(0)
    arr = gen.integers(40, 60, 10)

    months = 'sept oct nov dec jan feb mar apr may jun'.split()

    series = pd.Series(arr, index=months)

    print("Original Series is:\n",series)
    print("Now series values increased by 10:\n",series + 10)                 # increase all values of series by 10

    print(f'\nMean is {series.mean()}\n')
    print(series + (80 - series.mean()))


#
series_2()
print()

# 1.3
# 'in' operator and sort_values() function
#
def series_3():
    fruits = ['apple', 'cherry', 'kiwi', 'mango', 'banana']
    series = pd.Series(fruits)

    print('car' in 'racecar')                   # true

    print('kiwi' in series)                     # false
    print(1 in series)                          # true, because it is checking in index
    print('kiwi' in series.values)              # true, checking in values of pandas-series and not in index

    print(series.sort_values())                 # Default order is ascending order
    print(series.sort_values(ascending=False))
    print()

    print(series.sort_values(ascending=False).head(2))
    print(series.sort_values().tail(2))

#
series_3()
print()

# 1.4
# sort_index() function
#
def series_4():
    file = "C:\\Users\\hello\\pandas\\births1880.csv"
    dataframe = pd.read_csv(file, index_col="Names")
    print(type(dataframe))

    series = pd.read_csv(file, index_col="Names").squeeze('columns')
    print(type(series))

    series = series.sort_index(ascending=False)   # because it will not change the original object, so we need to save it
    print(series)


#
series_4()
print()

# 1.5
# iloc and loc attribute
#
def series_5():
    file = "C:\\Users\\hello\\pandas\\births1880.csv"
    series = pd.read_csv(file, index_col="Names").squeeze('columns')

    print("iloc---------")
    print(series.iloc[0])           # read by first index location
    print(series.iloc[-1])          # read by last index location

    print(series.iloc[[0,2,3]])     # read by multiple index location, get values where index in [0, 2, 3]
    print(series.iloc[1:4])         # read by slicing, get values between index 1 and index 4, but index 4 itself will be excluded

    print(series.iloc[:3])          # read by slicing, between index=0 to index=3, but index 3 itself will be excluded
    print(series.iloc[1:])          # read by slicing, from index=1 to last index
    print()
    print(series['Mel'])

    print("loc---------")
    print(series.index)
    print(series.loc[['Mel', 'Mary', 'John']])      # read by multiple index labels
    print(series.loc['Bob':'John'])                 # read by slicing, between index='Bob' & index='John', and index='John' is included

    print(series.loc[:'John'])                      # read by slicing, index='John' is included
    print(series.loc['Jessica':])                   # read by slicing

   
#
series_5()
print()

# 1.6
# overwrite values of a series
#
def series_6():
    file = "C:\\Users\\hello\\pandas\\births1880.csv"
    series = pd.read_csv(file, index_col="Names").squeeze('columns')

    # Overwrite series value
    print("series.iloc[0] = ", series.iloc[0])
    print("series.loc['Mel] = ", series.loc['Mel'])

    series.iloc[0] = 125        # modify value at index position '0'
    series.loc['Mel'] = 777     # modify value where index label =  'Mel'

    print("series.iloc[0] = ", series.iloc[0])
    print("series.loc['Mel] = ", series.loc['Mel'])

    series.iloc[[0, 1, 3]] = [222, 333, 444]     # modify value at multiple indexes

    print(series)


#
series_6()
print()

# 1.7
# true copy vs reference
#
def series_7():
    file = "Data\\superheroes.csv"
    heroes_df = pd.read_csv(file, usecols=["Names"])

    heroes_series = heroes_df.squeeze('columns')        # this series is a view of above dataframe and not a copy
                                                        # modifying the 'heroes_series' will modify the dataframe = 'heroes_df'
    print("Original Series is : ")
    print(heroes_series)
    print()

    heroes_series.iloc[0] = "wonderwoman"               # modified the series, it will modify the dataframe = 'heroes_df'

    print("Modified Series is : ")
    print(heroes_series)

    print("Now the dataframe is : ")
    print(heroes_df)                                    # dataframe is now modified because we modified the series.
    print()

    heroes = heroes_df.squeeze('columns').copy()        # using copy() method to create a true 'copy' and not a 'view'

    heroes.iloc[0] = "antman"                           # modified the true series

    print("Modified Series is : ")
    print(heroes)

    print("Now the dataframe is : ")
    print(heroes_df)                                    # dataframe is now not modified because we modified the true copy of series.
    print()

#
series_7()
print()

# 1.8
# series methods - sum, mean, median, mode, std, count, info
# series attributes - series.size, series.index, series.values
# 
def series_8():
    file = "Data\\births1880.csv"
    df = pd.read_csv(file, usecols=["Births"])

    my_series = df.squeeze('columns')     

    print(f"total count is {my_series.count()}")  # function
    print(f"total size is {my_series.size}")      # attribute   

    print(f"product of this series is - {pd.Series([1, 2, 3, 4, 5]).product()}") 

    print(f"mean/avg of this series is - {my_series.mean()}") 
    print(f"median of this series is - {my_series.median()}") 
    print(f"mode of this series is - {pd.Series([11, 21, 11, 41, 51]).mode()}") 

    print(f"sum of this series is - {my_series.sum()}") 
    print(f"max of this series is - {my_series.max()}") 
    print(f"min of this series is - {my_series.min()}") 

    print(f"std dev of this series is - {my_series.std()}") 
    print(f"describe the series - {my_series.describe()}") 
    print(f"Info of series - {my_series.info()}") 


#
series_8()
print()


# 1.9
# broadcasting
# adding a scalar value to the whole series - this is also known as broadcasting
# 
def series_9():
    file = "Data\\births1880.csv"
    df = pd.read_csv(file, usecols=["Births"])

    my_series = df.squeeze('columns').copy() 

    print(my_series, "\n")

    print(my_series.add(10), "\n")   # original series is not modified, we can store/get a new series or use 'my_series + 10'
    print(my_series.sub(10), "\n")   # original series is not modified, we can store/get a new series or use 'my_series - 10'

    print(my_series, "\n")

    print(my_series * 100)              # multiply all values from series with 100  or use 'my_series.mul(100)'
    print(my_series - 50)               # subtract all values from series with 50

    print(my_series.div(10), "\n")      # original series is not modified, we can store/get a new series or use 'my_series / 10'

    print(my_series.value_counts())     # how many time a value is repeated, that count will be shown

    print(f"Value Count:\n{pd.Series([11, 21, 11, 41, 51, 61, 11, 21]).value_counts()}")

    print(f"Value Count:\n{pd.Series([11, 21, 11, 41, 51, 61, 11, 21]).value_counts()}")

    print(f"Value Count Normalize (proportions/frequencies):\n{pd.Series([11, 21, 11, 41, 51, 61, 11, 21]).value_counts(normalize=True)}")

    print(f"Value Count Normalize * 100 (%) :\n{pd.Series([11, 21, 11, 41, 51, 61, 11, 21]).value_counts(normalize=True) * 100}")

#
series_9()
print()


# 1.10
# apply()
# apply method - accepts a function and applies this function on every Series value.
# 
def series_10():
    file = "Data\\superheroes.csv"
    df = pd.read_csv(file, usecols=["Names"])

    heroes_series = df.squeeze('columns').copy() 

    print(heroes_series, "\n")

    print(heroes_series.apply(len))         # get length of every series value, we stored string values in name column

    upper = lambda x: x.upper()             # apply this lambda on every value of our series.

    print(heroes_series.apply(upper))


#
series_10()
print()


# 1.11
# map()
# map method - map each series value to another value.
# 
def series_11():
    file = "Data\\superheroes.csv"
    df = pd.read_csv(file, usecols=["Names"])

    heroes = df.squeeze('columns').copy() 
    print(heroes, "\n")

    # Python dictionary vs Series mapping.

    special_powers = {
            "Spiderman" : "Building_Jumping",
            "dr" : "magic",
            "captain" : "super",
            "man" : "man-of-man",
            "Batman" : "Bat_Powers",
            "Superman" : "Can_Fly",
        }

    print(heroes.map(special_powers))              # matching dictionary keys will be mapped with the values of series, 1-0-1 mapping


#
series_11()
print()
