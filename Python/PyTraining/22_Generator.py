# Generator Functions
# A standard function will return the complete result after its execution is completed
# Generator Function will return the result one by one, like a series or sequence
# Generator Functions are memory efficient and they support concept of lazy evaluation
# A Generator Function will not use the 'return' keyword it will use the 'yield' keyword.


#this is a standard function
def stdFunction(x):
  result = x*x*x
  return result

res = stdFunction(10)   #calling our standard function, res will hold the returned value, here that is 1000


#Generator Function-exmaple-1-
def genFunc1():
  n = 10
  yield n

  n+=1
  yield n

  n+=1
  yield n


#calling the generator function
result = genFunc1()
print(result)

for vals in result:
  print(vals)

#we can loop through a generator function
for x in genFunc1():
  print(x)

print("-----------------------------------")

#Generator Function-exmaple-2-
def genFunc2(num):
  for tmp in range(num, (num*10+1), num):
    yield tmp



#we can loop through a generator function
for x in genFunc2(5):
  print(x)


result = genFunc2(3)

print(next(result))
print(next(result))
print(next(result))
print(next(result))
