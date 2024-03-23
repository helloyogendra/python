#global scope - function

y = 10
def myFunction1():
  y = 9
  return y*y

print(myFunction1())


def myFunction2():
  global y
  return y*y

print(myFunction2())


#String - Strings are character arrays and all characters are indexed
#Strings are immutable data types

name = "Alex Hopkins"
Country = 'Poland'
Address = "23 A #305 East Street, Warsaw, Poland"
myzip = 11225

final_string = name + ", " + Country + ", " + Address + ", " + str(myzip)
print(final_string)

formatted_string = f"Candidate name is {name} and he lives in {Country}"
print(formatted_string)

poem = """ allow me to fly high
            it is sunny or cloudy sky """


print(name[0])   #get the value at first index
print(name[-1])   #get the value at last index

# name[0] = "P"   # error, not allowed for string

print(len(name))    #get the length of string

#loop through an string variable because it is an array only
for val in Address:
  if str.isdigit(val):
    print(val)


# 'in' operator in string = check if one string is present in another string

print("London" in Address)
print(Country in Address)

if "Poland" in Address:
  print("Yes, found it")

if "Poland" not in Address:
  print("Yes, not present ")
else:
   print("Yes, found it")

str1 = "My fav color is 'blue' "  #observe the output - 'blue'
print(str1)

str2 = 'My fav color is "yellow" '  #observe the output - "yellow"
print(str2)


