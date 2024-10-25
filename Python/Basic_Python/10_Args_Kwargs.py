#Functions
#Functions with documentation : 

def myFunction(name):
  """
    use this line to generate documentation for a function
    documentation should be added immediately after function name
    we need to follow the standard indentation
  """
  name = "Hello " + name
  print(name)


myFunction("Alex")

print(myFunction.__doc__)   #get the associated documentation for this function


#Functions with variable number of arguments = *args

def doSum(*args):
  print(type(args))

  a=0
  for item in args:
    a = a + item
  return a


result = doSum(10, 20, 30)
print(result)

result = doSum(10, 20, 30, 40, 50)
print(result)


result = doSum(10, 20, 30, 40, 50, 77, 32, 1)
print(result)


#Functions with variable number of arguments with names = **kwargs

def greetings(**kwargs):
  print(type(kwargs))

  if kwargs is not None:
    for key, value in kwargs.items():
      print(f"{key} is {value}")
  else:
    print("nothing to process")


greetings(singer="singing")

greetings(bird="flying", kid="dancing", monkey="jumping")







