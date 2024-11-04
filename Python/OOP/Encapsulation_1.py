# OOP - Encapsulation - Data Hiding
# Demo for Private Attributes
# Use Double Underscore before name of a attribute or method to mark it private
# Private members (attributes or methods) are not available outside of the class -or- we can not access these using an object

class Employees:

    def __init__(self, emp_name, emp_salary):
        self.name = emp_name                        # Public attribute/variable
        self.__salary = emp_salary                  # Private attribute/variable, starts with double underscore
                                                    # Private attribute/variable we can not access using an object/instance

    
    def get_salary(self):
        return self.__salary
    

    # Private method - useful for helper functionality - can not call from outside/object
    def __get_salary(self):
        return self.__salary


    def set_salary(self, new_salary):
        if new_salary > 0:
            self.__salary = new_salary
        else:
            print('invalid salary, change and try again') 

    def __str__(self):
        return f'Class: Employees, Name: {self.name}, Salary: {self.__salary}'



# creating object/instance of the Employees class

emp1 = Employees("John", 5500)

print(emp1)

emp1.set_salary(0)

emp1.get_salary()


print(emp1.name)

# print(emp1.__salary)                  # AttributeError, Why, because __salary attribute is private

# emp1.__get_salary()                   # AttributeError, Why, because __get_salary() function is private



# Question:
# Can we have some work around to access a private variable
# Answer - yes, we can access using name mangling but it is not recommended
# refer to below code-

print("accessing private method - ", emp1._Employees__get_salary())

print("accessing private variable - ", emp1._Employees__salary)

# Explore and read about name mangaling

