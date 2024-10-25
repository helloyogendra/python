
cp = __import__("My Module")         #import a module having spaces in the file name



x = int(input("enter first number- "))
y = int(input("enter second number- "))

cp.myFunction1(x, y)                        #calling function from imported module

z = int(input("enter third number- "))
print(cp.myFunction2(z))                    #calling function from imported module

print("all done, all good")