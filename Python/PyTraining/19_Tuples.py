#Tuple
#Tuples are immutable collection objects

#We can not change a tuple object
#if we really want to modify a tuple, first convert this tuple to a list, update/change it
#and convert it back to tuple, refere below 4 lines

# x1 = ("", "", "")
# l1 = list(x1)
# now modify this l1, try to use the append or insert method
# x1 = tuple(l1)

#define a tuple object
fruits = ("apple", "banana", "cherry", "mango", "banana")
print(type(fruits))

f1, f2, f3, f4, f5 = fruits   #unpacking of tuple to variables
print(f2)

#unpacking of tuple to variables
#in below code first two values will be assigned to f1 & f2, 
#and all remaining values will be assigned to fn and fn is now a list
f1, f2, *fn = fruits  
print(f1)
print(type(fn))

f1, *fn, f2 = fruits  #unpacking of tuple to variables  
print(f1)
print(f2)
print(type(fn))
print(fn)

print(len(fruits))  #get the length of tuple objects

print(fruits)

a1 = fruits[0]   #read\access tuple items using index
a2 = fruits[2]

#fruits[0] = "berry"   #modifying tuple object is not allowed, it is immutable

print(a2)

scores = (100, 150, 250, 300, 110)
s1 = scores[2]
print(s1)

tpl1 = (10, 20) + (30, 35, 10)    #join two tuples

for item in tpl1:
  print(item)


#creating a tuple object with a single item

tpl2 = (22)         #this is not a tuple, just an expression for system
print(type(tpl2))

tpl2 = (22,)         #this is a tuple, add comma for single item
print(type(tpl2))