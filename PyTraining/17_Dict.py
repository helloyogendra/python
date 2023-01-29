#Dictionary
#Key Value Pairs - mutable object/collection
#A Dictionary object should not have duplicate keys
#A Dictionary can only use immutable type to define it's keys 

myFirstDict = { "name": "Alex", "Age": 30, "Mobile": 22335, "City": "Warsaw"}

value1 = myFirstDict["name"]   #access/get a value from dictionary by passing a key
print(value1)

value1 = myFirstDict["Age"]
print(value1)

myFirstDict["Age"] = 32       #modify a value from dictionary by passing a key
myFirstDict["name"] = "Bob"    #modify a value from dictionary by passing a key

print(myFirstDict)

allKeys = myFirstDict.keys()
allValues = myFirstDict.values()

print(type(allKeys))
print(allKeys)

print(type(allValues))
print(allValues)

print(type(list(allValues)))   #convert the allValues to list object and get type
print(list(allValues))         #convert the allValues to list object and print that list

#loop dictionary:
for k, v in myFirstDict.items():
  print(f" for key = {k} the associated value is {v} ")

#like the myFirstDict.items(), we can also loop through myFirstDict.keys() or myFirstDict.values()

dict1 = { 10: "Ten", 20: "Twenty"}
