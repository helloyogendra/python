#String - Strings are character arrays and all characters are indexed
#Strings are immutable data types

# String Slicing

name = "Alex Hopkins"
Country = 'Poland'

result = name[1:6]    #start reading at index=1, stop at index=6-1
print(result)

result = name[:5]    #if staring index is not available that means start at 0
print(result)

result = name[5:]    #if stop index is not available that means read till last index
print(result)

result = name[-4:-1] 
print(result)

greeting = "Morning"

result = greeting[0:7:2]      #start -index: stop-index: jump/step
print(result)


result = greeting[1:7:2]      #start -index: stop-index: jump/step
print(result)

result = greeting[::-1]       #reverse a string
print(result)
