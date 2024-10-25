#string formatting/patching
#formatted strings

name = "Alex"
age = 28
greeting = "morning is good"

print("Hello" + " " + name + " " + greeting)
print("Python Training who is not present", name)

#using the inbuilt function - format to format or patch a string
print("The name of participant is {0} and his age is {1} ".format(name, age))

my_string = "The name of the candidate is {0} and he is {1} years old "
name = "Bob"
age = 27
print(my_string.format(name, age))

print(f"The name of the candidate is {name} and he is {age} years old")


print("--------------------------")

#Loops in Python
#While Loop

count = 1

while(count < 10):
  print("The count is= ", count)
  count +=1                         # count = count + 1
else:
  print("while loop completed, count is now=", count) 



print("next line of code, outside of loop")

print("--using for loop to traverse through a list items below example--")

#using for loop to traverse through a list items

myList1 = [60, 70, 85, 10, 20, 30, 40, 50]   # a python list object / list variable

for val in myList1:
  if val > 30:
    print(val)
else:
  print("done with the loop")

print("------enumerate function example below------------")

#inbuilt function - enumerate will produce the items of a list and index as well

for index, val in enumerate(myList1):
  print(f"At index={index} the list item values is={val}")


#using for loop to traverse through a list items

print("------zip function example below------------")

#zip function - we can use zip function to loop through multiple targets/sequences

myList2 = [60, 70, 85, 10, 20, 30, 40, 50] 
myList3 = [2, 2, 5, 3, 4, 1, 5, 2] 

for val1, val2 in zip(myList2, myList3):
  print(f"value from myList2={val1} and value from myList3={val2} and sum is {val1 + val2} ")


#example of zip function if lists have different lengths 
#it will run till the length of the smallest list (list with minimum number of items)

list1 = [60, 70, 85, 10]
list2 = [60, 70, 85, 10, 20]
list3 = [60, 70, 85, 10, 20, 30]

for val1, val2, val3 in zip(list1, list2, list3):
  print(f"Sum is {val1 + val2 + val3} ")
