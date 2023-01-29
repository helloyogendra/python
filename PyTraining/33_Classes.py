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


