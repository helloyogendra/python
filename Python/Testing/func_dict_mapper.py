# Example functions
result_dict = []

def func_name(name):
    print(f"Name: {name}")
    result_dict.append(True)

def func_age(age):
    print(f"Age: {age}")
    result_dict.append(False)

def func_mobile(mobile):
    print(f"Mobile: {mobile}")
    result_dict.append(True)

# Define a dictionary with functions mapped to keys
function_map = {
    "name": func_name,
    "age": func_age,
    # Add more mappings as needed
}

# Example dictionary
my_dict = {"name": "John", "age": 20}

# Iterate over the keys of the dictionary
for key in my_dict:
    # Check if the key is in the function map
    if key in function_map:
        # Get the corresponding function and call it with the value from the dictionary
        function = function_map[key]
        value = my_dict[key]
        function(value)


print("Final result = ", all(result_dict))