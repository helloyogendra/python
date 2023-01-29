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