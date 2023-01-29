#Context Manager
#Context Manager can perform the resource clean-up automatically.
#Example - if we are opening a file and creating a file object, once done, we must call the close() method to close that file object/handle.


#example-closing a file manually by calling the file.close() method
data = "this is just a sample data for file"
fileName = "C:\\Users\\hello\\temp\\test.txt"
f = open(fileName, "w")
f.write(data)
f.close()     
print("done")


#example-closing a file automatically without calling the file.close() method, here 'context-manager' will close the file for us
#note - with clause is required to open a context manager

data = "this is my sample data to write that in a  file"
fileName = "C:\\Users\\hello\\temp\\test1.txt"

with open(fileName, "w") as file_Object:
    file_Object.write(data)

print("done")