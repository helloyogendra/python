#Dictionary

list1 = ["abc", "xyz", "123", "python"]
list2 = [100, 150, 222, 555]

myDictionary = { keys:values  for (keys, values) in zip(list1, list2) }  #Dictionary Comprehension

print(type(myDictionary))
print(myDictionary)

print(myDictionary["123"])

newDictionary = dict(zip(list1, list2))

print(type(newDictionary))
print(newDictionary)

dict1 = { "name": "John", "Age": 32, "Scores": [58, 69, 75]}

#Removing items

dict1.pop("name")    #mention the key to remove, it will remove that key:value pair

print(dict1)

dict1.popitem()       #it will remove the last key:value pair (py=3.7)

print(dict1)

del dict1["Age"]   # using the 'del' to remove a key:value pair

print(dict1)

del dict1        #delete the whole dictionay object


dict1 = { "name": "John", "Age": 32, "Scores": [58, 69, 75]}

dict1.clear()  #delete everything, now dictionary is empty but it exists


#Nested Dictionary

nestedDict = { 
    "name" : "Alex", 
    "Address": { 
        "City" : "London", 
        "Country" : "UK",
        "Zip" : 12345
        } 
    }

#When we will pass the address key we will get a dictionay object

result = nestedDict["Address"]
myCity = result["City"]
print(myCity)


#Copying Dictionary Objects

new_dict1 = nestedDict    #not a good way to copy, they both are referenced with the same object

new_dict2 = nestedDict.copy()    #use the copy() method to create a new object

new_dict3 = dict(nestedDict)     # or we can copy using this way

#Adding new items

dict1 = { "name": "John", "Age": 32, "Scores": [58, 69, 75]}

print(dict1)

dict1["country"] = "America"    #adding a new key:value pair to dictionary

print(dict1)

dict1.update( { "city" : "DC" } )  #adding a new key:value pair to dictionary

print(dict1)

dict1["name"] = "Alex"   #update the value which is associated with key=name