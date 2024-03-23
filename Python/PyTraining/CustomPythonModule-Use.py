#We are importing our custom module in this file and using it

import CustomPythonModule as cp

a = 50
b = 75
cp.myFunction1(50, 75)

c = 9
rs = cp.myFunction2(c)
print(rs)


#just to import only one method we can use below import statement

from CustomPythonModule import myFunction2


print(myFunction2(10))