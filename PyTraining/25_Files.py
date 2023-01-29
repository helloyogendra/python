# File Handling::

import os

data = "this is just a sample data for file"
fileName = "C:\\Users\\hello\\temp\\one.txt"

#defined a function to create a file and write data into this file
def fileFunction(data, fileName):
  try:

    file = open(fileName, "w")
    file.write(data)

  except Exception as ex:
    print(ex)
  finally:
    file.close()      #once done, we must call this method to close the file object/handle
    print("done")



#uncomment below function to call it
#fileFunction(data, fileName)   #calling this function to create a file and write data into this file


#function to open the existing file and append some new data into this file::
def appendFile(fileName):
  file = open(fileName, "a")    #filemode is "a" here means apppend
  file.write("\n adding a new line in my old file")
  file.write("\n one more line in my old file")
  file.close()
  print("append done")


#appendFile(fileName)

#function to read the data of an existing file and print that data to console
def readFile(fileName):
  try:
    file = open(fileName, "r")
    fileContents = file.read()
    print(fileContents)
  except Exception as ex:
    print(ex)
  finally:
    file.close()
    


#readFile(fileName)


#define a function to delete a file
def deleteFile(fileName):
  if os.path.exists(fileName):
    yesNo = input("are you sure to delete this file? press-y/Y to proceed else anything else to cancel- ")
    if(yesNo == "Y" or yesNo == "y"):
      os.remove(fileName)
      print(f" {fileName} file is deleted")
    else:
      print("delete cancelled by user")
  else:
    print("file not found")


#deleteFile(fileName)


def fileChoice(fileName):
  i = input("File Operation: Enter a choice: \n w to write \n r to read \n a to append \n d to delete: ")

  if i.lower() == "w":
    fileFunction(data, fileName)
  elif i.lower() == "a":
    appendFile(fileName)
  elif i.lower() == "r":
    readFile(fileName)
  elif i.lower() == "d":
    deleteFile(fileName)
  else:
    print("incorrect choice, no matches")



fileChoice(fileName)


fileName = r"C:\Users\hello\temp\YogendraSingh.pdf"   #for path based string with single slash start string with 'r'
deleteFile(fileName)

