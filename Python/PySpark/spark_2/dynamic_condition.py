import re
from functools import reduce
from pyspark.sql.functions import col

# Sample DataFrame dictionary (replace this with your actual DataFrames)
dataframes = {
    'dxCounterParty': ...,
    'dxTrade': ...,
    # Add more DataFrames as needed
}

# Given string value
conditions_string = "dxCounterParty.ctrptyType=BANK|FININST;dxCounterParty.counterParty<>INTERNAL|SC_FXGB_GFX01;dxTrade.productSubType<>FUT;dxTrade.venue<>TRAIANA*;dxTrade.possDupFlag<>Y;dxTrade.executingID<>S2BXTPS1|S2BXTPS1_S2BXTPS1|S2BXCAL1|S2BXCAL1_S2BXTPS1|S2BXOMS1|S2BXOMS1_S2BXTPS1;dxTrade.account<>SCA-LE*;dxTrade.secondaryTrdType<>Drawdown;dxTrade.actorTyp<>Sales|Support,sym,100000,0.05,0D00:15:00.000000000,0D00:10:00.000000000,0D00:10:00.000000000"

for ss in conditions_string.split(";"):
    print(ss)
    for s in ss.split("."):
        print(s)

# Adjusted regular expression to capture < > operators
condition_pattern = re.compile(r'(\w+)\.(\w+)(<>|=)([^;]+)')

# Create a dictionary to store combined conditions for each table
combined_conditions = {}

# Iterate through individual conditions
for condition in conditions_string.split(';'):
    match = condition_pattern.match(condition)
    if match:
        table_name, column_name, operator, values_str = match.groups()
        
        # Split values separated by pipe (|)
        values = values_str.split('|')
        
        # Convert values to PySpark column expressions with 'or' condition if needed
        column_expression = reduce(lambda x, y: x | y, [col(column_name) == value for value in values]) if '|' in values_str else col(column_name) == values_str
        
        # Apply the NOT condition if the operator is <>
        if operator == '<>':
            column_expression = ~column_expression
        
        # Add the condition to the corresponding table's combined conditions
        if table_name in combined_conditions:
            combined_conditions[table_name] &= column_expression
        else:
            combined_conditions[table_name] = column_expression

# Apply the combined conditions to the respective DataFrames
for table_name, condition in combined_conditions.items():
    # if table_name in dataframes:
    #     dataframes[table_name] = dataframes[table_name].filter(condition)
    # else:
    #     print(f"DataFrame for table '{table_name}' not found.")
    print(table_name, condition)

# Now 'dataframes' dictionary contains filtered DataFrames based on the specified conditions
