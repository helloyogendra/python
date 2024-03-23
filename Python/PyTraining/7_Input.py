#Input Function - Collecting the user input

value1 = input("input something: ")  #default input type is string
value2 = input("input something: ")  #default input type is string

print("total of value1 and value2 is", value1 + value2)

#by using the inbuilt function str.isdigit() we can check if a string is having valid number value 

#a better way to check and convert
if str.isdigit(value1) and str.isdigit(value2):
  print("total of value1 and value2 is", int(value1) + int(value2))
else:
  print("please check, looks like invalid input for this operation")


#below will also work but not a good idea, why

val1 = int(input("input first value: "))  #default input type is string we are converting that to integer/number
val2 = int(input("input second value: ")) #default input type is string we are converting that to integer/number

print(f"first value={val1} & second value={val2} and sum is={val1 + val2}")


# we have used int() function here
# try to use the float(), bool(), str() functions


