#List
#List Comprehension - write code within list notation = [code] to produce a new list
# [code/logic for-loop conditions/if]
# [expression iteration conditions]
#example-1

result = [val for val in range(1, 11)]
print(type(result))
print(result)

result = [val**2 for val in range(1, 11)]
print(result)

result = [val + val for val in range(1, 11)]
print(result)


new_list1 = []
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

#access/filter list using for loop
for items in fruits:
  if "a" in items:
    new_list1.append(items)

print(new_list1)


#access/filter list using for loop
new_list2 = [items for items in fruits if "a" in items]
print(new_list2)

#write a one line program to produce a list of even numbers upto 50.
print([num for num in range(1, 51) if num % 2==0 ])
print([num for num in range(2, 51, 2)])

#Assignment:
#Convert the above program to standard for loop, no list Comprehension

#Assignment:
#write a one line program to produce a list of odd numbers upto 50.


#Can we use the else part inside a list Comprehension?
#example

a=10
b=20
yy = a if a > b else b          #ternary ? operator kind of behaviour
print(yy)


list1 = [0, 1, 0, 3, 0, 5, 7]

result = [x if x else 9 for x in list1]
print(result)

result = [x if x > 3 else 1 for x in list1]
print(result)


#example - list comprehension with two loops
lst1 = [10, 20, 30, 40]
lst2 = [11, 22, 33, 44]

result = [(a, b) for a in lst1 for b in lst2]  #two loops are like nested loops
print(result)
print(type(result))

y1 = result[0]

print(type(y1))
print(y1)

result = [[a, b] for a in lst1 for b in lst2]  #two loops are like nested loops
print(result)

result = [[a, b] for a, b in zip(lst1, lst2)]  
print(result)

result = [a * b for a, b in zip(lst1, lst2)]  
print(result)
