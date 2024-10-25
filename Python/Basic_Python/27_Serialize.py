#Serialization: saving an object in a file
#Saving data/object in a file is Serialization, reading it back is De-Serialization (file contect is mostly binary)
#Pickling
#Shelving

#Pickling example

import pickle

#Writing the data
myList = ["one", 100, 250, 35.35, "London", 10000]
fileName = r"C:\Users\hello\temp\data"                  #file path and file name to write our object data

fileObject = open(fileName, 'wb')                       #create a file object in 'write-binary' mode, file-path is mentioned
pickle.dump(myList, fileObject)                         #pickle.dump() method will use the file object and data/variable to write this file
print("writing done!!")


#reading back the data
fileObject = open(fileName, 'rb')                        #use a file object in 'read-binary' mode, file-path is mentioned
result = pickle.load(fileObject)

print(type(result))
print(result)
fileObject.close()

##
##


#Serialization: saving an object in a file
#Saving data/object in a file is Serialization, reading it back is De-Serialization (file contect is mostly binary)

#Shelving - it is using a key:value pair kind of storage, like a database to write a file content

#Shelving example

import shelve

#Writing
mySet = { "mango", "cherry", "banana", "berry" }
myList = [1000, 20000, 3456, 8765]
myTuple = ("Poland", "India", "USA", "UK")

fileName = r"C:\Users\hello\temp\shelved-data"  

shelve_object = shelve.open(fileName)

shelve_object["setData"] = mySet
shelve_object["listData"] = myList
shelve_object["tplData"] = myTuple

shelve_object["text"] = "Stop the global warming asap"


shelve_object.close()
print("data flushed to file")


shelve_object = shelve.open(fileName)

set1 = shelve_object["setData"]
list1 = shelve_object["listData"]
tpl1 = shelve_object["tplData"]
txt1 = shelve_object["text"] 

print(set1)
print(txt1)

shelve_object.close()

