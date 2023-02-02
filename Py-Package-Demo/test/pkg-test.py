#we are using our custom python package here

from Pkg.Clear import clear
from Pkg.div import divide

clear()

print("Python Custom Package Demo")

result = divide(25, 5, "z")
print(result)

result = divide(27, 2, "i")
print(result)

