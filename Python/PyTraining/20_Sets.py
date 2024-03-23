#Set
#Sets are mutable unordered, unindexed, collection objects
#duplicate values are not allowed in a set

#FrozenSet
#FrozenSets are immutable collection objects

mySet1 = {11, 22, 33, 44, 55, 11, 22}

print(type(mySet1))
print(mySet1)

mySet2 = {"one", "two", "three"}

mylist = [77, 88, 99, 11, 22, 33, 44, 55, 11, 22, 33, 99]

mySet3 = set(mylist)    #duplicates will be remove,  list(set(mylist))
print(mySet3)

print(list(set(mylist)))   #produce a new unsorted list
print(sorted(list(set(mylist))))  #produce a new sorted list

for val in mySet1:
  if val > 30:
    print(val)

#Set based operation

set1 = {11, 22, 33}
set2 = {33, 44, 55}

s1 = set1 | set2    #union of both sets, all items from both sets, remove duplicates
print(s1)

s2 = set1 & set2    #intersection of both sets, all common items from both sets
print(s2)

s3 = set1 ^ set2    #uncommon items from both sets, completely remove the common itmes
print(s3)

s4 = set1 - set2    #items in set1 but not in set2
print(s4)

s5 = set2 - set1   #items in set2 but not in set1
print(s5)


#inbuilt methods for set

set1 = {"a", "b", "c"}
set2 = {11, 22}

set3 = set1.union(set2)     # include all items from both sets and returns a new set
print(set3)

set1.update(set2)           # in-place updation, set1 will be updated from items of set2

print(set1)


#remove set items

mySet2 = {"one", "two", "three", "four", "five" }

mySet2.remove("three")   #remove "three" from this set object

print(mySet2)

# mySet2.remove("three")    #error, if "three" is not present in this set, it will throw error

mySet2.discard("two")        #remove "three" from this set object

print(mySet2)

mySet2.discard("two")      # no error here, if "two" is not present in this set, it will not throw any error

mySet2.pop()               #it can remove any random item from this set

print(mySet2)

mySet2.clear()     #all items are gone from this set, now we have an empty set object

mySet2.add("nine")
print(mySet2)

lst1 = [10, 25, 35]

mySet2.update(lst1)
print(mySet2)

del mySet2       # delete the object itself


#FrozenSet

tuple1 = (10, 20, 30)

fSet = frozenset(tuple1)   #fset is an immutable object


#Set Comprehension

new_set = { val for val in range(3, 31, 3) }
print(type(new_set))
print(new_set)


#List, Dictionary, and Set Comprehensions are possible because these are mutable.
#Tuple Comprehension is not possible because tuple is immutable.
