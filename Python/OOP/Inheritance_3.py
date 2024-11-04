# OOP - Inheritance
# Demo for Inheritance between Classes

# Multiple Inheritance and MRO


# Parent - 1
class A:
    def function(self):
        print('function from class-A')


# Parent - 2
class B:
    def function(self):
        print('function from class-B')


# Child class is inheriting from Parent class A and parent class B
class Child(A, B):

    # if we implement 'function' aagain in the Child class then it will use local version of 'function'
    # it will override the function from class A and class B

    def function_1(self):
        print('function from class-c')



child = Child()

child.function()        # because inheritance order is - class Child(A, B), it will call 'function' from class A

print(Child.mro())
