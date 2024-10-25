def check_result(lst):
    return "Passed" if all(item == "Passed" for item in lst) else "Failed"

# Example list
lst1 = ["Passed", "Passed", "Failed"]
result = check_result(lst1)
print("Overall result:", result)

lst2 = ["Failed", "Failed", "Failed"]
result = check_result(lst2)
print("Overall result:", result)

lst3 = ["Passed", "Passed", "Passed"]
result = check_result(lst3)
print("Overall result:", result)
