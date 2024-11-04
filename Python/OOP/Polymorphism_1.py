# OOP - Polymorphism
# Operator Overloading - Compile Time
# Method Overiding - Run Time - Inheritance, Abstraction

# 1.
# Implement an Animal class with only 1 method speak()
# Child classes - Cat, Dog etc can also implement speak(), it will override the method from Parent class, that is Animal

# 2.
# We can achieve this using absttract class as well
# Abstract class will have abstract methods where we do not have any default behaviour/implementation for abstract methods
# all the child classes are free to implement the abstract methods as per the requirement/design

# 3.
# Shape Class - having an area() method, do we need an implementation for area if shape is generic [abstract method]
# Circle Class - area()
# Traingle class - area()
# Rectangle class - area()



# Example of operator overloading
# We can overload operator like +, -, * to use these mostly with objects

import os


a1 = 10
b1 = 25
c1 = a1 + b1


class A:
    def __init__(self, aa):
        self.aa = aa



obj1 = A(11)  # instance of class A

obj2 = A(22)  # instance of class A


# result = obj1 + obj2      # TypeError: unsupported operand type(s) for +: 'A' and 'A'


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y


    # overloading the + operator, it will be called automatically if try to add objects of Vector class
    def __add__(self, object):
        return Vector(self.x + object.x, self.y + object.y)
    
    def __str__(self) -> str:
        return f'Vector class x = {self.x} and y = {self.y}'


v_obj1 = Vector(11, 22)

v_obj2= Vector(33, 44)

result_object = v_obj1 + v_obj2         # add two objects and store that in a new object (x + x, y + y)

print(result_object)



# by default we have a 'len' method in Python - does it support polymorphism ?

print(len("Hello"))                         # string

print(len(["Hello", "Hi", "How"]))          # list of string

print(len((10,)))                           # tuple

print(len([1, 2]))                          # list of integer


# to clean console from previous execution

os.system('cls')                    # 'cls' for dos and 'clear' for powershell/linux

# looks like above line of code is not cleaning the console, please google and fix it

# Abstract class Example
# Employee
## Full Time Employee
## Part Time Employee
## Interns

from abc import ABC, abstractmethod

class Employee(ABC):

    @abstractmethod
    def bonus_calculate(self):
        pass


# Implement for FTE
class FTE_Employees(Employee):

    def bonus_calculate(self):
        # bonus 25%
        print("Employee is eligible for 25% Bonus amount")


# Implement for PTE
class PTE_Employees(Employee):

    def bonus_calculate(self):
        # bonus 10%
        print("Employee is eligible for 10% Bonus amount")


# Implement for Interns
class Intern_Employees(ABC):

    def bonus_calculate(self):
            # bonus 2%
            print("Employee is eligible for 2% Bonus amount")


# driver
def get_bonus_amount(emp: Employee):
    emp.bonus_calculate()



emp_fte = FTE_Employees()

emp_pte = PTE_Employees()

emp_intern = Intern_Employees()


get_bonus_amount(emp_pte)       # pass any object from above


get_bonus_amount(emp_fte)