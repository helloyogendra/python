import os
import sys

import pandas as pd
import numpy as np

import datetime as dt


clear = lambda : os.system('cls')
clear()

# 1
# 1.1
# DataFrame
#
def dataframe_1():
    file = "Data\\marvels.csv"
    df = pd.read_csv(file)

    print("Loaded Pandas DataFrame from a CSV file : ", type(df))
    print(df)

    series = df['Names']

    print("Extracted a Series from Pandas DataFrame : ", type(series))
    print(series)
    print()

    print("Series vs Dataframes attributes and methods:")
    print()

    print(f"Series Index: {series.index}")
    print(f"Dataframe Index: {df.index}")
    print()

    print(f"Series values: {series.values}")
    print(f"Dataframe values: {df.values}")
    print()

    print(f"Series dtypes: {series.dtypes}")
    print(f"Dataframe dtypes: {df.dtypes}")
    print()

    print(f"Series Shape: {series.shape}")      # get number of items, tuple
    print(f"Dataframe Shape: {df.shape}")       # get number of rows and columns, tuple
    print()

    print(f"Series Size: {series.size}")         # get number of items, scalar/single numeric value
    print(f"Dataframe Index: {df.size}")         # get total number of items (row * column), scalar/single numeric value
    print()

    print(f"Series Count: {series.count()}")
    print(f"Dataframe Count: {df.count()}")     # count per column
    print()

    print(f"Series HasNanS: {series.hasnans}")
    print(f"Dataframe HasNanS: Not available for dataframe")
    print()

    print(f"Series Axes: {series.axes}")
    print(f"Dataframe Axes: {df.axes}")
    print()

    print(f"Series Columns: Not available for Series")
    print(f"Dataframe Columns: {df.columns}")
    print()

    print(f"Series Info: {series.info()}")
    print(f"Dataframe Info: {df.info()}")
    print()

    print(f"Series Head: {series.head()}")
    print(f"Dataframe Head: {df.head()}")
    print()

    print(f"Series Tail: {series.tail()}")
    print(f"Dataframe Tail: {df.tail()}")
    print()


#
dataframe_1()
print()

# 1.2
# DataFrame - get sum, column-wise, row-wise, sum of sum (atomic value)
#
def dataframe_2():
    file = "Data\\revenue.csv"
    dataframe = pd.read_csv(file, index_col='date')

    print(dataframe.head(1))
    print()

    series = dataframe['pune']
    print(series.head(1))

    print("Series vs Dataframe : ")

    print(f"series.sum() = {series.sum()}")
    print(f"series.sum(axis='index') = {series.sum(axis='index')}")  # same like above line
    print(f"series.sum(axis='columns') = ValueError: No axis named columns for object type Series.")
    print()

    print(f"dataframe.sum() = {dataframe.sum()}")   # separate sum for each column
    
    # above code => get column-wise sum for numerical columns and for string-column, values will be concatenated (no errors)
    
    
    print(f'dataframe.sum(axis="index") = {dataframe.sum(axis="index")}')          # same like print(dataframe.sum()), sum for each column
    print(f'dataframe.sum(axis="columns") = {dataframe.sum(axis="columns")}')      # row-wise sum
    print()

    # sum of sum across all columns for that index, single/atom/scalar value result
    print(f'dataframe.sum(axis="columns").sum() = {dataframe.sum(axis="columns").sum()}')  

    # Note - 
    # For sum across all columns for that index, horizontal sum [across columns], row-wise sum
    # if columns data type is mixed like number and string, error will be thrown


#
dataframe_2()
print()

# 1.3
# DataFrame - select a column or extract a series from a dataframe
#
def dataframe_3():
    file = "Data\\comics.csv"
    df = pd.read_csv(file)

    print(df.head(1))
    print()

    print(df.Age)                   # get a series from a dataframe, works if no space in column-name

    print(type(df.Age))

    print(df["Hero Name"])          # get a series from a dataframe, works if space in column-name

    print(type(df["Hero Name"]))    # column-names are case sensitive

    # Note-
    # Extracting a series will be a 'view' in memory and it is not a true copy.
    # any changes to the series will change the dataframe

    name_series = df["Hero Name"]      # a series will be created like a view

    # For below line there are no errors, but pandas will generate a warning, because indirectly we are modifying the dataframe also
    # name_series.iloc[0] = "New Hero"   
    print()

    name_series = df["Hero Name"].copy()      # a new series will be created, true copy
    name_series.iloc[0] = "New Hero"          # way to go, pandas will not generate a warning because we are not modifying the dataframe
    print(df)                                 # Dataframe is not modified

#
dataframe_3()
print()


# 1.4
# DataFrame - select multiple columns and create a new DataFrame
# DataFrame - Adding new and computed columns to a DataFrame
#
def dataframe_4():
    file = "Data\\comics.csv"
    df = pd.read_csv(file)

    print(df.head(1))
    print()

    new_df_1 = df[["Hero Name", "Power"]]                   # Extract two columns in a new dataframe (separate copy)
    # or
    columns_to_select = ["Hero Name", "Power", "Height"]
    new_df_2 = df[columns_to_select]                        # Extract two columns in a new dataframe (separate copy)

    print(f"Identity Check = {id(new_df_1)} : {id(new_df_2)} : {df is new_df_1} : {new_df_1 is new_df_2}")

    df["country"] = "USA"                                   # add a new column - 'country' and populate this column with 'USA'
    print(df.head(1))
    print()

    # Add a new column to a dataframe at specified position/index, other columns will be pushed to right side
    df.insert(loc=0, column="sport", value="Basketball")
    print(df.head(1))
    print()

    # Add a computed column to the dataframe
    df["Double Grade"] = df["Grade"].mul(2)         # or we can also use -  df["Double Grade"] = df["Grade"] * 2
    print(df.head(1))
    print()

#
dataframe_4()
print()


# 1.5
# DataFrame - value_count(), dropna(), fillna()
#
def dataframe_5():

    file1 = "Data\\revenue2.csv"
    df = pd.read_csv(file1)

    file2 = "Data\\comics2.csv"
    comics_df = pd.read_csv(file2)

    print(comics_df.head(1))
    print()

    print(df["date"].value_counts())                        # extract a series/column and count occurrences for each value/item of series

    print(df["date"].value_counts(normalize=True))  
    print(df["date"].value_counts(normalize=True) * 100)    # extract a series and show percentage for each value/item of series

    comics_df.dropna()              # drop a row if any missing values are present, 'Nan'

    comics_df.dropna(how='all')     # drop a row only if all values are missing for that row, 'Nan'
    comics_df.dropna(how='any')     # drop a row if any missing values are present, 'Nan', it it similar to - comics_df.dropna()

    # subset
    # Check the 'Height' column, and if missing values are here, remove that row
    print('comics_df.dropna(subset=["Height"]) : ')
    print(comics_df.dropna(subset=["Height"]))  
    print()

    print('comics_df.dropna(subset=["Age", "Height"]) : ')
    print(comics_df.dropna(subset=["Age", "Height"]))
    print()

    # fill the missing values
    comics_df.fillna(0)               # it will target all column and it will replace 'NaN' with '0', not a good idea

    comics_df['Grade'].fillna(0)      # it will target 'Grade' column and it will replace 'NaN' with '0', fillna() will make a true copy

    comics_df['Grade'] = comics_df['Grade'].fillna(0)                                   # overwriting the 'Grade' column in original df

    comics_df['Hero Name'] = comics_df['Hero Name'].fillna(value="Unknow SuperHero")    # overwriting the 'Grade' column in original df
    print(comics_df)

#
dataframe_5()
print()


# 1.6
# DataFrame - astype()
# Performs datatype conversion for a series - remove NaN first else error
#
def dataframe_6():

    file1 = "Data\\revenue2.csv"
    df = pd.read_csv(file1)

    file2 = "Data\\comics3.csv"
    comics_df = pd.read_csv(file2)

    comics_df.info()                                        # Size in memory = 825.5 KB

    comics_df.dropna(how='all')                             # remove a row if all values are 'NaN'
    comics_df['Grade'] = comics_df['Grade'].fillna(0)       # replace 'Grade' column's 'NaN' with '0' and then overwrite dataframe

    comics_df.info()                                        # Size in memory = 825.5 KB
    print(comics_df.dtypes)

    comics_df['Grade'] = comics_df['Grade'].astype("int")   # a separate copy will be created

    comics_df['Age'] = comics_df['Age'].fillna(0)           # replace 'Age' column's 'NaN' with '0' and then overwrite dataframe
    comics_df['Age'] = comics_df['Age'].astype(int)         # astype method will only work if no 'NaN' in the column.
    print(comics_df.dtypes)
    comics_df.info()                                        # Size in memory = 825.5 KB 


    comics_df.dropna(how='all')             # remove a row if all values are 'NaN'

    comics_df['Gender'].nunique()           # a scalar value will be returned, how many unique value are present in 'Gender' column
    comics_df.nunique()                     # column-wise result, how many unique value are present in each column
    comics_df.info()                        # Size in memory = 825.5 KB
    print()

    # astype method - 2 - perform datatype conversion - good for a column with limited 'unique' values
    comics_df['Gender'] = comics_df['Gender'].astype('category')                 
    comics_df.info()                        # Size in memory = 722.5 KB
    print()

    comics_df['Team'] = comics_df['Team'].astype('category')
    comics_df.info()                        # Size in memory = 619.5 KB 


#
dataframe_6()
print()


# 1.7
# DataFrame - sort_values()
# Performs sorting by mentioning the column name, at least one column name is required, it is same like 'Sql-Order-By'.
#
def dataframe_7():
    file1 = "Data\\revenue2.csv"
    df = pd.read_csv(file1)
    print(df.head(1))

    file2 = "Data\\comics4.csv"
    comics_df = pd.read_csv(file2)
    print(comics_df.head(1))
    comics_df.info()                                        # Size in memory = 1.6 MB

    # comics_df.sort_values()                               # Error - at least one column required to performing sorting, like 'order by'

    print("comics_df['Hero Name'].sort_values():")                    
    print(comics_df['Hero Name'].sort_values().head(10))    # Just sort and return the 'Hero Name' column/series
    print()

    print('comics_df.sort_values(by="Hero Name"):')
    print(comics_df.sort_values(by="Hero Name").head(10))    # Sort and return the dataframe by using the 'Hero Name' 
    print()

    print(comics_df.sort_values(by="Hero Name", ascending=False).head(10))

    # sort by grade in ascending order but keep the 'NaN' at last
    print(comics_df.sort_values(by="Grade", na_position='last', ascending=True).head(5))


    # Sort a dataframe by using multiple columns

    print("comics_df.sort_values(['Hero Name', 'Age', 'Grade']) : ")
    print(comics_df.sort_values(['Hero Name', 'Age', 'Grade']).head(10))
    print()

    print("comics_df.sort_values(['Hero Name', 'Age', 'Grade'], ascending=False) : ")
    print(comics_df.sort_values(['Hero Name', 'Age', 'Grade'], ascending=False).head(10))


    # sort the 'Age' column in ascending order and after that sort the 'Grade' column in descending order

    print("comics_df.sort_values(['Age', 'Grade'], ascending=[True, False]) : ")
    print(comics_df.sort_values(['Age', 'Grade'], ascending=[True, False]).head(25))


#
dataframe_7()
print()


# 1.8
# DataFrame - sort_index()
# Sort a dataframe by index
#
def dataframe_8():
    file1 = "Data\\revenue2.csv"
    df = pd.read_csv(file1)
    print(df.head(1))

    file2 = "Data\\comics4.csv"
    comics_df = pd.read_csv(file2)
    print(comics_df.head(1))
    comics_df.info()                                        # Size in memory = 1.6 MB
    print()

    print("comics_df.sort_values(['Hero Name', 'Age']) : ")
    print(comics_df.sort_values(['Hero Name', 'Age']).head(10))
    print()

    # sort_index
    # if we have numeric index then it will sort by index numbers in ascending order
    print("comics_df.sort_index() = ")
    print(comics_df.sort_index().head(10))   
    print()    

    # rank() method, the rank method assigns a numeric ranking to each Series value.
    # example - give same rank to highest 'Grade' then give another rank to second highest 'Grade'

    comics_df = comics_df.dropna(how='all')
    comics_df['Grade'] = comics_df['Grade'].fillna(0).astype('int')

    print("comics_df['Grade'].rank(ascending=True)")
    print(comics_df['Grade'].rank(ascending=True).head(10))
    
    print("comics_df['Grade'].rank(ascending=False).astype(int)")
    print(comics_df['Grade'].rank(ascending=False).astype(int).head(10))

    comics_df['Grade Rank'] = comics_df['Grade'].rank(ascending=False).astype(int)

    print("comics_df.sort_values('Grade', ascending=False).head(11)")
    print(comics_df.sort_values('Grade', ascending=False).head(11))                  


#
dataframe_8()
print()


# 1.9
# DataFrame
# Data Optimization
#
def dataframe_9():
    file = "Data\\employee.csv"
    emp = pd.read_csv(file)

    print(emp.head(1))
    emp.info()          # Size in memory = 625.2 KB
    print()

    emp['Start_Date'] = pd.to_datetime(emp['Start_Date'], format='%d-%m-%Y')
    print(emp.head(2))

    emp['Login_Time'] = pd.to_datetime(emp['Login_Time'], format='%H:%M:%S').dt.time
    print(emp.head(2))

    emp['Is_Senior_Management'] = emp['Is_Senior_Management'].astype(bool)
    emp['Gender'] = emp['Gender'].astype("category")
    emp['Department'] = emp['Department'].astype("category")
    print(emp.head(2))
    emp.info()          # Size in memory = 420.5 KB


#
dataframe_9()
print()


# 1.10
# DataFrame - Applying filters
#
def dataframe_10():
    file = "Data\\employee.csv"
    emp_1 = pd.read_csv(file, parse_dates = ["Start_Date"], date_format = '%d-%m-%Y')  # parsing dates while reading CSV

    emp_1['Login_Time'] = pd.to_datetime(emp_1['Login_Time'], format='%H:%M:%S').dt.time
    emp_1['Is_Senior_Management'] = emp_1['Is_Senior_Management'].astype(bool)

    emp_1['Gender'] = emp_1['Gender'].astype("category")
    emp_1['Department'] = emp_1['Department'].astype("category")

    print(emp_1.head())
    print("")

    print("Applying Filters: ")
    print(emp_1[emp_1['Gender'] == 'Male'])         # filter using 'Gender' column)

    filter_cond = emp_1['Department'] == 'Sales'    # filter condition
    print(emp_1[filter_cond])                       # filter using 'Department' column, used above condition

    # filter using 'Is_Senior_Management' column, this column is aleady a boolean, so check the below condition
    print(emp_1[emp_1['Is_Senior_Management']]) 

    # filter using 'Salary' column, where salary is greater than 75000
    print(emp_1[emp_1['Salary'] > 75000 ])    

    # filter using 'Bonus' column, where Bonus is lower than 10
    print(emp_1[emp_1['Bonus%'] <= 1 ])  

    # filter using 'Start_Date' column, check for proper 'date-time' comparison, below works
    print(emp_1[emp_1['Start_Date'] >= '2020-09-19' ]) 

    # filter using 'Login_Time' column, check for proper 'time' comparison, below works
    print(emp_1[emp_1['Login_Time'] < dt.time(12, 0, 0)])  


#
dataframe_10()
print()


# 1.11
# DataFrame
# Filtering a pandas dataframe by using multiple conditions
#
def dataframe_11():

    file = "C:\\Users\\hello\\pandas\\employee.csv"
    emp_1 = pd.read_csv(file, parse_dates = ["Start_Date"], date_format = '%d-%m-%Y')  # parsing dates while reading CSV

    emp_1['Login_Time'] = pd.to_datetime(emp_1['Login_Time'], format='%H:%M:%S').dt.time
    emp_1['Is_Senior_Management'] = emp_1['Is_Senior_Management'].astype(bool)

    emp_1['Gender'] = emp_1['Gender'].astype("category")
    emp_1['Department'] = emp_1['Department'].astype("category")

    print(emp_1.head(2))

    # using '&' operator to club multiple conditions and filter a dataframe, 'and' operator

    is_female = emp_1['Gender'] == 'Female'                 # filter_condition_1
    is_in_sales = emp_1['Department'] == 'Sales'            # filter_condition_2

    print(emp_1[is_female & is_in_sales])                   # applying above filter conditions with 'and'

    # using '|' operator to club multiple conditions and filter a dataframe, 'or' operator

    is_male = emp_1['Gender'] == 'Male'                     # filter_condition_1
    is_in_marketing = emp_1['Department'] == 'Marketing'    # filter_condition_2    

    print(emp_1[is_male | is_in_marketing])                 # applying above filter conditions with 'or'


    # using '&' operator to club multiple conditions and filter a dataframe, 'and' operator

    is_female = emp_1['Gender'] == 'Female'
    is_in_sales = emp_1['Department'] == 'Sales'
    is_salary_over_70k = emp_1['Salary'] > 70000

    print(emp_1[is_female & is_in_sales & is_salary_over_70k]) # applying above filter conditions with 'and'

    # combining 'and' with 'or' operator

    is_female = emp_1['Gender'] == 'Female'
    is_in_sales = emp_1['Department'] == 'Sales'

    is_salary_over_70k = emp_1['Salary'] > 70000

    print(emp_1[(is_female & is_in_sales) | is_salary_over_70k])

    # isin method
    print(emp_1[ emp_1['Department'].isin(['Sales', 'Marketing'])])

    # filter using 'isnull()' method
    print(emp_1[emp_1['Department'].isnull()])

    # filter using 'notnull()' method
    print(emp_1[emp_1['Department'].notnull()])

    # between() method
    print(emp_1[emp_1['Salary'].between(65000, 70000)])                         # filter between salary/number range

    print(emp_1[emp_1['Start_Date'].between("2020-01-01", "2021-01-01")])       # filter between date range

    print(emp_1[emp_1['Login_Time'].between(dt.time(8,30), dt.time(12,30))])    # filter between time range


#
dataframe_11()
print()


# 1.12
# DataFrame
# Removing duplicate rows from a dataframe.
#
def dataframe_12():

    file = "Data\\employee2.csv"
    emp = pd.read_csv(file, parse_dates = ["Start_Date"], date_format = '%d-%m-%Y')  # parsing dates while reading CSV

    emp['Login_Time'] = pd.to_datetime(emp['Login_Time'], format='%H:%M:%S').dt.time
    emp['Is_Senior_Management'] = emp['Is_Senior_Management'].astype(bool)

    emp['Gender'] = emp['Gender'].astype("category")
    emp['Department'] = emp['Department'].astype("category")

    print(emp.head(2))

    print(emp[emp['Name'].duplicated()])                    # by default first value will be considered non-duplicate

    print(emp[emp['Name'].duplicated(keep="first")])        # first value will be considered non-duplicate

    print(emp[emp['Name'].duplicated(keep="last")])         # last value will be considered non-duplicate

    print(emp[emp['Name'].duplicated(keep=False)])          # keep every duplicate values

    # Below code = All duplicates (Name) will be excluded.
    print(emp[~emp['Name'].duplicated(keep=False)])         # changing direction using ~ operator (opposite behaviour)

    print(emp.drop_duplicates())                            # get unique rows

    print(emp.drop_duplicates("Department"))                # drop rows having duplicates in the 'Department' column

    # drop rows having duplicates in the 'Department' column, keep first occurrence of duplicate
    print(emp.drop_duplicates("Department", keep='first')) 

    # drop rows having duplicates in the 'Department' column, keep last occurrence of duplicate
    print(emp.drop_duplicates("Department", keep='last')) 

    # subset of columns, looking for duplicates into multiple columns, combination should be duplicate
    print(emp.drop_duplicates(["Is_Senior_Management", "Department"]).sort_values('Department'))

    # unique and unique method
    print(emp['Gender'].unique())
    print(type(emp['Gender'].unique()))

    print(emp['Department'].unique())
    print(type(emp['Department'].unique()))

    print(emp['Name'].unique())
    print(type(emp['Name'].unique()))

    print(emp['Department'].nunique())
    print(type(emp['Department'].nunique()))

    print(emp['Department'].nunique(dropna=True))      # do not include 'NaN' while counting, produce a number for unique values
    print(emp['Department'].nunique(dropna=False))     # include 'NaN' while counting, produce a number for all unique values

    # Error in below line : 'DataFrame' object has no attribute 'unique'
    # emp.unique()  

    print(emp.nunique())        # nunique() available for DataFrame Object.


#
dataframe_12()
print()
