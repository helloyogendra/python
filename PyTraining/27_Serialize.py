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