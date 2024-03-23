# Object Oriented Programming - Class & Objects

# Classes & Objects

class myClass:
  
  def __init__(self, a, b):
    self.x = a
    self.y = b

  
  #class member function, we can call this function using an instance/object of class
  def sum(self):
    result = self.x + self.y
    print(f"sum of x and y is {result}")



#class is a user defined type (complex data type) and object(instance) is like a varibale of class-type

myObj = myClass(10, 20)
myObj.sum()

myObj1 = myClass(100, 200)
myObj1.sum()

myObj2 = myClass(150, 250)
myObj2.sum()