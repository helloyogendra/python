#Loops in Python

country = "america"

for tmp in country:
  print(tmp)

print("below loop will start at 0 and it will run till 10-1")

#below loop will start at 0 and it will run till 10-1
for val in range(10):
  print(val * val)

print("below loop will start at 2 and it will run till 10-1")

#below loop will start at 2 and it will run till 10-1
for val in range(2, 10):
  print(val + val)

print("below loop will start at 3 and it will run till 16-1, step/jump is 3")

#below loop will start at 3 and it will run till 16-1, step/jump is 3, with each cycle of loop increase the item by 3
for item in range(3, 16, 3):
  print(item)


print("we can store the range objects value and we can loop through that later like below example")

mySequence = range(2, 21, 2)   #we can store the range objects value and we can loop through that later

for i in mySequence:
  print(i)

#Can we print series of odd or even numbers by controlling the range function parameters - range(1, 100, 2)

#break and continue keyword::

#break will break the cycle of loop and come out of loop and continue with the next line of code
#continue will skip the current cycle of loop and pick the next item from target/sequence/collection/list/array/string

print("------------------")

greeting = "morning is good"

for val in greeting:
  if val == "n":
    continue
    print(val)
  elif val == "g":
    break
    print(val)
  else:
    print(val)

print("next line outside of loop")


