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


##
##


# Object Oriented Programming - Class & Objects
# A class has members - member variable/instance variables and member functions/instance methods

# init method
# instance variables
# instance methods
# class methods
# static methods
# Destructor
# Properties
# bu default all classes are inherited from "object" class

class Exmaple:
    val = 100       #this is a class variable

    #this is an initializer method, instance variable here are 'name' and 'age'
    def __init__(self, n, a):
        self.name = n           #instance variable - name is defined here
        self.age = a            #instance variable - age is defined here


    #instance method
    def instMethod(self):
        print(f"accessing instance variables - name is {self.name} and age is {self.age} ")


    @staticmethod
    def staticMethod(x):
        print(f"we can access instance variables here, means self is not available")
        print(f"we can access a class variable {Exmaple.val * x}")


    @classmethod
    def classMethod(cls, n, a):
        print(f"we can access a class variable {Exmaple.val}")
        return cls(n, a)   #return a new instance/object of this class, cls we can not use in a static-Method

    def __del__(self):
        print("destructor got called!!")

    #it will be called automatically if we try to print the object/instance of this class
    def __str__(self):
        return f"name = {self.name} and age = {self.age} for this instance of Example Class"

    


#code to create instance/object of that class and use the functionality of that class

inst1 = Exmaple("Alex", 32)  #we created an object/instance
inst1.instMethod()           # we are calling the a member function of class(instance method), this method is pointing to different copy of member variables

obj1 = Exmaple("Bob", 35)                       #again we created an object/instance
obj1.instMethod()

del inst1                                       #cleanup the object - destructor will be called

Exmaple.staticMethod(10)                        #calling the static method of class by using the className

new_obj = Exmaple.classMethod("John", 28)        #calling the class method of class by using the className
new_obj.instMethod()

print(new_obj)                                  #it will automaticallly call the - def __str__(self): (if we have implemented it)


##
##


#Inheritance:
#Extending the functionality of an existing class::

#Base/Super/Parent  <-- Derived/Sub/Child

#Syntax - class child(Parent):
#Below code we have two classes with a relation of inheritance, and that is simple inheritance

class Parent:
    def __init__(self, n, c):
        self.num = n
        self.count = c

    def instanceMethod(self):
        print("instance method from class")



class Child(Parent):
    pass



obj1 = Child(100, 255)     #initializing the variables, 'num' and 'count' using the object/instance of child class because of inheritance
obj1.instanceMethod()


########################### Next Program for multilevel inheritance


class A:
    def __init__(self, n, c):
        self.num = n
        self.count = c

    def instanceMethod(self):
        print("instance method from class")
        print(f"{self.num + self.count} ")



class B(A):
    def __init__(self, n, c, name):
        super().__init__(n ,c)          #by using the super method we are calling the init method of parent class(class-A)
        self.name = name                #we are adding one instance variable for class B



class C(B):
    def __init__(self, n, c, name):
        super().__init__(n, c, name)



obj2 = C(10, 20, 'Alex')    #creating instance of class C
obj2.instanceMethod()



########################### Next Program for multiple inheritance - for a single child class there could be two or more parent classes


class Parent_A:
    def __init__(self, pa):
        self.pa = pa
        

    def method_A(self):
        print("instance method from class-Parent_A")
        print(f"{self.pa} ")



class Parent_B:
    def __init__(self, pb):
        self.pb = pb    

    def method_B(self):
        print("instance method from class-Parent_B")
        print(f"{self.pb} ")            



class Child_C(Parent_A, Parent_B):
    def __init__(self, pa, cc):
        super().__init__(pa)
        self.cc = cc


obj3 = Child_C(10, 12)

obj3.pa = 11
obj3.pb = 500
obj3.cc = 44.44

obj3.method_A()
obj3.method_B()



########################### Next Program for Hierarchical  inheritance - for a single parent class there could be two or more child classes


class Base_A:
    def __init__(self, pa):
        self.pa = pa
        

    def method_A(self):
        print("instance method from class-Base_A")
        print(f"{self.pa} ")



class Derived_B(Base_A):
    def __init__(self, pa):
        super().__init__(pa)         



class Derived_C(Base_A):
    def __init__(self, pa):
        super().__init__(pa)
        


obj4 = Derived_B(111)
obj5 = Derived_C(333)

obj4.method_A()
obj5.method_A()


########################### Abstract classes
# object/instance creation is not allowed for an Abstract classe
# in order to use an Abstract classe we must inherit this class and we can create/use a child class object
# abstract class we have abstract methods and child class must implement this abstract method
# abstract methods don't have any definition in the base class

import abc

class AbstractBaseClass(abc.ABC):

    @abc.abstractmethod
    def absFunction(self):
        pass


class childForAbstractClass(AbstractBaseClass):

    def absFunction(self):
        print("implemented the abstract method from AbstractBaseClass")


object1 = childForAbstractClass()
object1.absFunction()