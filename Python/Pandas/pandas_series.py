import pandas as pd
import numpy as np

# 1
# 1.1
# Pandas Series
# Like an independent column or One-dimensional array
# 
def create_series_1():

    series_1 = pd.Series([30, 40, 35, 47, 20, 25, 20])

    print(type(series_1))
    print(series_1, "\n")

    # Inbuilt methods for Series.
    print("Sum = ", series_1.sum())
    print("Mean = ", series_1.mean())
    print("Median = ", series_1.median())
    print("Mode = ", series_1.mode())

#
create_series_1()
print()


# 1.2
#
def create_series_2():

    fruits = ['apple', 'cherry', 'banana', 'mango', 'apple', None]

    series_2 = pd.Series(fruits)
    print(series_2, "\n")

    # Inbuilt attributes/accessors/properties for a Pandas Series.
    print("Size = ", series_2.size)
    print("Is Unique = ", series_2.is_unique)
    print("hasnans = ", series_2.hasnans)
    print("dtype, dtypes = ", series_2.dtype, ", ", series_2.dtypes)
    print("values = ", series_2.values, " = ", type(series_2.values))
    print("index = ", series_2.index, " = ", type(series_2.index))

#
create_series_2()
print()


# 1.3
#
def create_series_3():
    indian_states = {
        'Karnataka': 'Bengaluru',
        'Maharashtra': 'Mumbai',
        'Gujrat': 'Gandhinagar',
        'Tamilnadu': 'Chennai',
    }
    series_3 = pd.Series(indian_states)

    print(series_3)
    print("index = ", series_3.index, " = ", type(series_3.index))
    print("values = ", series_3.values, " = ", type(series_3.index))

#
create_series_3()
print()


# 1.4
#
def create_series_4():
    # Parameter and arguments

    fruits = ['apple', 'cherry', 'banana', 'mango', 'kiwi']
    recipe = ['juice', 'shake', 'milkshake', 'icecream', 'smoothy']

    s1 = pd.Series(fruits, recipe)    # default order is - data, index
    print(s1, "\n")

    s2 = pd.Series(index=recipe, data=fruits)
    print(s2)


#
create_series_4()
print()


# 1.5
#
def create_series_5():

    gen_obj = np.random.default_rng()       # produce a generator object

    np_arr = gen_obj.integers(70, 101, 10)  # get 10 random number between 71 and 101

    print(np_arr)

    print(np.random.default_rng(0).integers(70, 101, 10).size)

    my_series_1 = pd.Series(np_arr)
    my_series_1.index = 'sept oct nov dec jan feb mar apr may jun'.split()

    months = 'sept oct nov dec jan feb mar apr may jun'.split()
    my_series_2 = pd.Series(np_arr, index=months)

    print(f'average for the year is {my_series_1.mean()}')

    print(f'average for the first half is {my_series_1[:5].mean()}')   # Used standard Python slicing - included index 0 to 4
    print(f'average for the second half is {my_series_1[5:].mean()}')

    print(my_series_1.iloc[:5].mean())                                 # Used iloc slicing - included index 0 to 4

    avg1 = my_series_1.loc['sept':'jan'].mean()                        # Used loc/labeled slicing - included index 'sep' to 'jan'
    avg2 = my_series_1.loc['feb':'jun'].mean()

    print(f'Imrpovements are : {avg1-avg2}')

    print(my_series_1.head().mean())                                   # default behaviour is to select first 5 elements only
    print(my_series_1.head(5).mean())

    print(my_series_1.tail().mean())                                   # default behaviour is to select last 5 elements only
    print(my_series_1.tail(5).mean())

    print(f"std dev. is {my_series_1.std()}")



#
create_series_5()
print()


# 1.6
#
def import_series():
    '''
    Squeeze() will convert a dataframe into a series, only if the dataframe has a single column
    If we have more than one column in our dataframe, squeeze() will not generate any error,
    Instead, it will be a dataframe object only and not a series
    '''

    file_1 = "C:\\Users\\hello\\pandas\\births1880.csv"
    series_1 = pd.read_csv(file_1, usecols=['Names']).squeeze()  # import just one column and Squeeze()

    print(type(series_1))
    print(series_1)
    print()

    # Read the CSV file, using 'Births' as the index column and keeping 'Names'
    df = pd.read_csv(file_1, usecols=['Names', 'Births'], index_col='Births')

    # Extract the 'Names' column as a Series
    series_2 = df['Names']
    print(type(series_2))
    print(series_2)
    print()

    file_2 = "C:\\Users\\hello\\pandas\\Google_Stock_Price.csv"
    series_3 = pd.read_csv(file_2, usecols=['Volume']).squeeze('columns')  # import just one column and Squeeze()

    print(type(series_3))
    print(series_3)

#
import_series()
print()