# Python Math Library Examples::

import math

tpl1 = (10, 35, 85, 98, 25, 21)
lst1 = [44, 67, 78, 97, 12, 43]


print(f"from this tuple= {tpl1} biggest value is {max(tpl1)} ")
print(f"from this list= {lst1} smallest value is {min(lst1)} ")


print(f"if power of 2 is 4 the result would be {2**4} ")
print(f"if power of 2 is 4 the result would be {pow(2, 4)} ")

print(f"the square root for 625 is = { math.sqrt(625) } ")

x = math.ceil(11.25)
print(f"11.25 after ceil is = { x } ")

x = math.floor(11.75)
print(f"11.75 after floor is = { x } ")