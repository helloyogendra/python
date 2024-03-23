# Exception Handling are runtime errors

#As of now this function can generate exceptions
def myFunction():
  a = int(input("enter 1st value: "))
  b = int(input("enter 2nd value: "))
  result = a/b
  return result


try:
  print("Before function call")
  result = 0
  result = myFunction()     #if any exceptions will come here, it will jump to the except block and continue

  print(f"your result is {result}")
  print("after function call")

except Exception as ex:
  print(ex)                                #these two line will only execute if any exception comes under try block code
  print("Looks like some issue came")



#Exception handling inside a function
def myFunction2():
  try:
    a = int(input("enter 1st value: "))
    b = int(input("enter 2nd value: "))
    result = a/b
    return result
  except ZeroDivisionError:
    print("trying to divide by zero?")
  except Exception as ex:
    print(ex)                               
    print("Looks like some issue came, please check!!")
  finally:
    print("inside finally")     #finally block code will execute always


myFunction2()


#raise/throw an exception
def myFunction3():
  print("----my function-3---")
  try:
    a = input("enter 1st value: ")
    b = input("enter 2nd value: ")
    x = 0
    y = 0

    if str.isdigit(a) and str.isdigit(b):
      x = int(a)
      y = int(b)
    else:
      raise Exception("check values, looks like incorrect")   #raise an exception

    result = x / y
    return result
  
  except Exception as ex:
    print(ex)                               
    print("Looks like some issue came, please check!!")



myFunction3()
