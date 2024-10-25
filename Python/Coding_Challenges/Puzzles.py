import os
import sys

clear = lambda : os.system('cls')
clear()


# 1
# Dictionary Yes, they must be unique and immutable/hashable

def check_correct_dict():
    dct = { 1: 1, '1': 2, True: 3, (1, 2): 4,       
        # [1, 2]: 5,     # not allowed, TypeError: unhashable type: 'list'
    }
    print(dct[1])


check_correct_dict()


# 2
# List copy operation

def list_copy_operations():
    l1 = [10, 20, 30]
    l2 = l1
    l1.append(40)

    print("l1 ", " = ", id(l1), " = ", l1)
    print("l2 " , " = ", id(l2), " = ", l2)
    print("Identity Comparison for l1 and l2 : ", l1 is l2)

    ls1 = [10, 20, 30]
    ls2 = ls1.copy()
    ls1.append(40)

    print("")
    print("ls1 ", " = ", id(ls1), " = ", ls1)
    print("ls2 " , " = ", id(ls2), " = ", ls2)

    lst1 = [[10, 20, 30], [40, 50, 60]]
    lst2 = lst1.copy() 
    lst1[0][0] = 100
    
    print("")
    print("lst1 ", " = ", id(lst1), " = ", lst1)    # address of lst1 and lst2 are different but still lst2 values got modified
    print("lst2 " , " = ", id(lst2), " = ", lst2)

    from copy import deepcopy
    list1 = [[10, 20, 30], [40, 50, 60]]
    list2 = deepcopy(list1)
    list1[0][0] = 100
    
    print("")
    print("list1 ", " = ", id(list1), " = ", list1)   # after modifying list1 values, now list2 values will not get modified
    print("list2 " , " = ", id(list2), " = ", list2)


list_copy_operations()


# 3
# Formatted Strings

def format_strings():
    fruit = 'Apple'
    color = 'Red'
    weight = 150.8765
    unit = 'grams'

    result = f'\nThe fruit is {fruit} and its color is {color} and has a weight of {weight: .2f} {unit}'
    print(result)


format_strings()


# 4
# Magic Method __add__
# __radd__ right add is called either when:
# the first object is a builtin type and the second is a user type - so __add__ returns (not raises !) NotImplemented.
# So Python will try __radd__ from the second object). 
# This can be generalized as "if the first object returns NotImplemented, then Python uses __radd__ from the second"
# the first object does not have __add__ implemented at all - so Python tries to use __radd__ from the second

def add_magic_method():
    class class1:
        val1 = 10

        def __add__(self, other):
            return self.val1 + other.val2
        
        def __radd__(self, other):
            return self.val1 + other.val2

    class class2:
        val2 = 20

        def __radd__(self, other):
            return self.val2 + other.val1
        
    print(class1() + class2())   # this line works because we implemented __radd__ in class2 else error
    print(class2() + class1())   # this line works because we implemented __radd__ in class1 else error
    

add_magic_method()


# 5
# __slots__ : Limit the extendability of a class to explicitly allow only certain attributes.
#             The advantages are memory size and execution speed of the code.

def slots_sexample():
    class MyClassWithoutSlots:

        def __init__(self, name, age):
            self.name = name
            self.age = age
            self.grade = 30   # this line works

        def __str__(self):
            return f"Name = {self.name} and Age = {self.age} where Grade is {self.grade}"   # this line works
            

    obj1 = MyClassWithoutSlots("John", 38)
    print(obj1)

    obj1.hair_color = "Brown"                     # this line works
    print(f"Hair Color is {obj1.hair_color}")     # this line works
    
    print("MyClassWithoutSlots - Object - Attribute Dictionary", obj1.__dict__)
    print("")

    class MyClassWithSlots:
        __slots__ = ['name', 'age']

        def __init__(self, name, age):
            self.name = name
            self.age = age
            #self.grade = 30     # this line will not work now because we limited/fixed the attributes using __slots__

        def __str__(self):
            # return f"Name = {self.name} and Age = {self.age} where Grade is {self.grade}"   # this line will not work now - 'grade
            return f"Name = {self.name} and Age = {self.age}"

    obj2 = MyClassWithSlots("Tony", 38)
    print(obj2)

    #obj2.hair_color = "Black"                                                  # Error, this line will not work now
    #print(f"Hair Color is {obj2.hair_color}")                                  # Error, this line will not work now
    
    #print("MyClassWithSlots - Object - Attribute Dictionary", obj2.__dict__)   # Error, this line will not work now, 
    

slots_sexample()


# 6
# __eq__ : Implement in a class to perform object comparison.
       
def eq_magic_method():
    class Class_without_eq:
        def __init__(self, x, y):
            self.x = x
            self.y = y


    p1 = Class_without_eq(1, 2)
    p2 = Class_without_eq(1, 2)
    p3 = Class_without_eq(3, 4)

    print("")
    print(f"Class_without_eq - Result of p1 == p2 is {p1 == p2}")  # Output: False, 
    print(f"Class_without_eq - Result of p1 == p3 is {p1 == p3}")  # Output: False,


    class Class_with_eq:
        def __init__(self, x, y):
            self.x = x
            self.y = y

        def __eq__(self, other):
            if isinstance(other, Class_with_eq):
                return self.x == other.x and self.y == other.y
            return NotImplemented

    p11 = Class_with_eq(1, 2)
    p21 = Class_with_eq(1, 2)
    p31 = Class_with_eq(3, 4)

    print("")
    print(f"Class_with_eq - Result of p11 == p21 is {p11 == p21}")  # Output: True, 
    print(f"Class_with_eq - Result of p11 == p31 is {p11 == p31}")  # Output: False,
    

eq_magic_method()


# 7
# global 

name = 'Tony'       
def global_variable():
    global name
    name = 'Peter'

global_variable()
print(name)         # Peter


# 8
# Context Manager - Resource Managers to release memory for Database connection, file handles etc.
# We can call it using a 'With' clause which offer an automated 'setup' and 'teardown' by using the '__enter__' and '__exit__' methods
 
def context_mamager_example():
    class FileHandler:
        def __init__(self, filename, mode='r'):
            self.filename = filename
            self.mode = mode
            self.file = None

        def __enter__(self):
            self.file = open(self.filename, self.mode)
            return self.file

        def __exit__(self, exc_type, exc_value, traceback):
            """
            Close the file when done.
            
            :param exc_type: The type of exception (if any).
            :param exc_value: The exception value (if any).
            :param traceback: The traceback object (if any).
            :return: False to propagate exceptions; True to suppress them.
            """
            if self.file:
                self.file.close()
            # If an exception occurred, let it propagate; return False
            return False


    # Writing to a file
    with FileHandler('example.txt', 'w') as file:
        file.write("Hello, world!\n")
        file.write("This is a test.")

    # Reading from a file
    with FileHandler('example.txt', 'r') as file:
        content = file.read()
        print(content)


context_mamager_example()


# 8
# Guess the output

def func(a):
    x = [i for i in range(a)]
    return (a // 2) or x

print(func(0))      # []
print(func(1))      # [0]
print(func(2))      # 1
print(func(-1))     # -1

# 9
# Guess the output

def func_dict():
    l1 = [1, 3, 5, 7, 9]
    l2 = [0, 2, 4, 6, 8]

    output = {x: y for x in l1 for y in l2}   
    print(output)                               # {1: 8, 3: 8, 5: 8, 7: 8, 9: 8}
func_dict()


# 10
# Guess the output

def recursive_function(n, sum):
    if n < 1:
        return sum
    else:
        return recursive_function(n-1, sum+n)


# print(recursive_function(10000, 11))     # RecursionError: maximum recursion depth exceeded in comparison

print("Current Recursion limit is - ", sys.getrecursionlimit())

sys.setrecursionlimit(500)

print(recursive_function(100, 11))


# 11
# Guess the output

def empty_class_print():
    class House:
        pass

    print(House)    # Class name/info
    print(House())  # Object Address


    class House1:
        def __repr__(self):
            return "House 1 class"


    print(House1)    # Class name/info
    print(House1())  # print from __repr__ implementation


empty_class_print()


# 11
# 11.1
# Guess the output - What will the value of N be?
# Threading

def threading_output_guess_no_lock():
    from threading import Thread, Lock

    N = 0
    def alter(quant, delta):
        # This method is not thread safe
        nonlocal N
        for _ in range(quant):
            N = N + delta
            print(f"Without a lock N is - {N}")

    this = [Thread(target=alter, args=(5, d) ) for d in [-1, 1]]

    [t.start() for t in this]
    [t.join() for t in this]


threading_output_guess_no_lock()


# 11.2
def threading_output_guess_with_lock():
    from threading import Thread, Lock
    N = 0
    lock = Lock()  # Create a lock for thread-safe operations

    def alter(quant, delta):
        nonlocal N
        for _ in range(quant):
            with lock:  # Acquire the lock before modifying N
                N = N + delta
                print(f"With a lock N is - {N}")

    threads = [Thread(target=alter, args=(5, d)) for d in [-1, 1]]

    for t in threads:
        t.start()

    for t in threads:
        t.join()


threading_output_guess_with_lock()


# 12
# 12.1
# Guess the output
# List Binding

def add_to_list1(item, lst1=[]):
    lst1.append(item)
    print(lst1)

my_list1 = [1, 2, 3]

add_to_list1(4)
add_to_list1(5, my_list1)
add_to_list1(6)
add_to_list1(7, my_list1)
add_to_list1(8)
print("")


# 12.2
def add_to_list2(item, lst2=None):
    if lst2 is None:
        lst2 = []
    lst2.append(item)
    print(lst2)

my_list2 = [1, 2, 3]

add_to_list2(4)
add_to_list2(5, my_list2)
add_to_list2(6)
add_to_list2(7, my_list2)
add_to_list2(8)
print("")


# 12.3
def add_to_list3(item, lst3=None):
    if lst3 is None:
        list1 = []
    else:
        list1 = lst3.copy()
    list1.append(item)
    print(list1)

my_list3 = [1, 2, 3]

add_to_list3(4)
add_to_list3(5, my_list3)
add_to_list3(6)
add_to_list3(7, my_list3)
add_to_list3(8)


# 13
# For loop internals
# Implementing a Custom Loop

def my_custom_loop():
    class CustomRange:
        def __init__(self, start, end):
            self.current = start
            self.end = end

        def __iter__(self):
            return self

        def __next__(self):
            if self.current >= self.end:
                raise StopIteration
            value = self.current
            self.current += 1
            return value

    # Using the custom loop
    for number in CustomRange(1, 5):
        print(number)

my_custom_loop()


# 14
# Removes the odd numbers from a given list or range
# 14.1
# For loop is not a good choice for this problem 
def remove_odd_numbers_1():

    numbers = [n for n in range(10)]

    for i in range(len(numbers)):
        if i % 2 != 0:
            del numbers[i]   

    print(numbers)
    
# remove_odd_numbers_1() # Exception - IndexError: list assignment index out of range

# 14.2
# While loop is a better choice for this problem 
def remove_odd_numbers_2():
    numbers = [n for n in range(10)]

    i = 0
    while i < len(numbers):
        if numbers[i] % 2 != 0:
            del numbers[i]  # Remove the element
        else:
            i += 1  # Only increment if no element was removed
    print(numbers)

# Example usage
remove_odd_numbers_2()


# 14.3
# We can use List Comprehension as well  
def remove_odd_numbers_3():
    numbers = [n for n in range(10)]
    numbers = [n for n in numbers if n % 2 == 0]
    print(numbers)


# 15
# Guess the output

def for_output_guess():
    for i in range(10):
        if i%2: 
            continue
            print (i)
        if i % 10: 
            break
    else:
        print('Error')    # It will never print


for_output_guess()


# 16
# Define and use a Custom Exception Class.

def custom_exception_example():
    class MyError(Exception):
        def __init__(self, value, descr, *args): 
            print ('Initializing the Custom Exception Class:- ')
            self.value = value
            self.descr = descr 
        #below is optional but nice to have, in order to be able to use 'print exception' directly
        def __str__(self): 
            return 'Nice representation of our exception: {}, {}'.format(self.value, self.descr) 
  

    def use_custom_exception():
        try: 
            raise MyError(1000, "Encountered a Run Time Error")
        except MyError as ex:
            print('My exception occurred, value:', ex.value, ex.descr)
            print(ex)

    use_custom_exception()


custom_exception_example()
print("")


# 17
# Guess the output:

def guess_output_function():
    def get_date(input_data):
        return input_data[2]

    def get_checksum(input_data):
        return input_data[1]

    def get_package(input_data):
        return input_data[0]

    def main_function():
        data = ['PACK-001', 'a0ebb0617f3de66']
        try:
            pack = get_package(data)
            print(pack)                 # 'PACK-001'
            try:
                date = get_date(data)   # exception - no index-2 is available
                print(date)             # skipped

            except IndexError as exc:
                print("Something went wrong. Please check: %s" % exc)     # catch index error and print
                raise                                                     # raise again/throw same exception

            cs = get_checksum(data)     # skipped because of 'raise' from above code
            print(cs)                   # skipped because of 'raise' from above code

        except IndexError as exc:
            print("Something went wrong. Please check: %s" % exc)   # catch index error and print
            raise                                                   # crash the program now and print unhandled exception details
        except Exception as exc:
            print("Unexpected exception occurred: %s" % exc)    

    main_function()
    print("Finished")       # never got executed because exception propagated from 'main_function' and it was not handled.


# guess_output_function()   # commenting for now else below code will not get executed because of unhandled exception


# 18
# Composition Example:
# This means that a class Composite can contain an object of another class Component. 
# This relationship means that a Composite "has-a" Component.

def composition_example():
    class Salary:
        def __init__(self, pay):
            self.pay = pay
    
        def get_total(self):
            return (self.pay*12)
 
    class Employee:
        def __init__(self, pay, bonus):#, AbstractSalary):
            self.pay = pay
            self.bonus = bonus
            self.obj_salary = Salary(self.pay)
            #self.obj_salary = AbstractSalary(self.pay)
 
        def annual_salary(self):
            return "Total: " + str(self.obj_salary.get_total() + self.bonus)
 
    
    obj_emp = Employee(600, 500)
    print(obj_emp.annual_salary())


composition_example()
print("")


# 19
# Monkey Patching Example:

def monkey_patching_example():
    class A:
        def func(self):
            print ("Class-A-func() is being called")


    def monkey_func(self):
        print ("monkey_f() is being called")
   
    # replacing address of "func" with "monkey_f"
    A.func_A = A.func           # Existing function renamed in class-A
    A.func_B = monkey_func      # Store a new function in class-A
    A.func = monkey_func        # Replace an existing function of class-A
    obj = A()
    
    # calling function "func" whose address got replaced
    # with function "monkey_f()"
    obj.func_A()
    obj.func_B()
    obj.func()


monkey_patching_example()
print("")


# 20
# MRO Example:

def mro_example():
    class A:
        def method(self):
            print("Method in class A")

    class B(A):
        def method(self):
            print("Method in class B")

    class C(A):
        def method(self):
            print("Method in class C")

    class D(B, C):
        pass

    # Testing MRO
    d = D()
    d.method()
    print(D.mro())


mro_example()
print("")


# 21
# Python Encapsulation:
# Public, Protected, Private.

def encsulation_example():
    class BankAccount:
        def __init__(self, account_number, balance):
            self.account_number = account_number    # Public member
            self._balance = balance                 # Protected member (by convention)
            self.__password = "secure_password"     # Private member
    
        # Public method
        def deposit(self, amount):
            if amount > 0:
                self._balance += amount
            else:
                print("Deposit amount must be positive")
        
        # Public method
        def withdraw(self, amount):
            if 0 < amount <= self._balance:
                self._balance -= amount
            else:
                print("Invalid withdrawal amount")

        # Public method
        def get_balance(self):
            return self._balance

        # Public method
        def change_password(self, new_password):
            if self.__validate_password(new_password):
                self.__password = new_password
            else:
                print("Password validation failed")

        # Private method
        def __validate_password(self, password):
            # A simple validation for demonstration purposes
            return len(password) > 8

    # Using the BankAccount class
    account = BankAccount("123456", 1000)

    # Accessing public member and method
    print(account.account_number)           # Output: 123456
    account.deposit(500)

    print(account.get_balance())            # Output: 1500

    # Accessing protected member (not recommended, but possible)
    print(account._balance)                 # Output: 1500

    # Trying to access private member (will result in an AttributeError)
    # print(account.__password)  # Uncommenting this line will raise an AttributeError

    # Correct way to access private member is via a public method
    account.change_password("new_secure_password")
    # account.__validate_password("password")  # This will raise an AttributeError

    # print(account.__password)  # Private : AttributeError: 'BankAccount' object has no attribute '__password'


encsulation_example()
print("")


# 22
# Python Closures:

def make_counter():
    var = 'Sometext'

    def inner():
        return var
    return inner

counter = make_counter()
del make_counter
#  
c = counter()
print(c) 


# 23
# Nonlocal:

def make_counter():
    count = 0
  
    def inner():
        nonlocal count
        count += 1 
         
        return count
    return inner
 
counter = make_counter()

c = counter()
print(c)
  
c = counter()
print(c)


# 24
# Singleton:

def singleton_example():
    class SingletonClass:
        def __new__(cls):
            if not hasattr(cls, 'instance'):
                cls.instance = super(SingletonClass, cls).__new__(cls)
            return cls.instance
  

    singleton_object_a = SingletonClass()
    singleton_object_b = SingletonClass()

    print(id(singleton_object_a))                                   # same id/address
    print(id(singleton_object_b))                                   # same id/address

    print(singleton_object_a is singleton_object_b)

    singleton_object_a.single_variable = "Singleton Variable"       # assignment to a different object
    print(singleton_object_b.single_variable)                       # reading a different object
    

singleton_example()


# 25
# Abstract Class:

def abstract_class_example():
    from abc import ABC, abstractmethod

    # Define an abstract base class
    class Vehicle(ABC):
        
        @abstractmethod
        def start_engine(self):
            """Start the vehicle's engine."""
            pass
        
        @abstractmethod
        def stop_engine(self):
            """Stop the vehicle's engine."""
            pass

        @property
        @abstractmethod
        def horse_power(self):
            pass

    # Concrete class implementing the abstract base class
    class Car(Vehicle):
        
        def start_engine(self):
            print("Car engine started.")
        
        def stop_engine(self):
            print("Car engine stopped.")

        @property
        def horse_power(self):
            return 2500

    # Concrete class implementing the abstract base class
    class Motorcycle(Vehicle):
        
        def start_engine(self):
            print("Motorcycle engine started.")
        
        def stop_engine(self):
            print("Motorcycle engine stopped.")

        @property
        def horse_power(self):
            return 500

    # Instantiate and use the classes
    print("")

    car = Car()
    car.start_engine()              # Output: Car engine started.
    car.stop_engine()               # Output: Car engine stopped.
    print(f"The Car is having {car.horse_power} CC of Horse Power")

    print("")
    motorcycle = Motorcycle()
    motorcycle.start_engine()       # Output: Motorcycle engine started.
    motorcycle.stop_engine()        # Output: Motorcycle engine stopped.
    print(f"The Bike is having {motorcycle.horse_power} CC of Horse Power")


abstract_class_example()


# 26
# 26.1 
# Decorator Example:

def decorator_func(orig_func):
    def modified_func(param):
        return "<p>{}</p>".format(orig_func(param))
    return modified_func

@decorator_func
def greet(name):
    return "Hi " + name

print(greet('John'))

# 26.2
def decorator_func1(orig_func):
    def get_cube(a, b):
        return orig_func(a, b) * a
    return get_cube

@decorator_func1
def square(a, b):
    return a ** b

print(square(4, 2))


# 26.3
def simple_decorator(func):
    GREEN = "\033[0;32m"
    YELLOW = "\033[1;33m"
    def wrapper(*args, **kwargs):
        return f"{GREEN}{func(*args, **kwargs)}{YELLOW}"
    return wrapper

@simple_decorator
def say_hello(name):
    return f"Hello, {name}!"

# Call the decorated function
print(say_hello("Alice"))


# 26.4
# Decorator with arguments
def repeat_decorator(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat_decorator(times=3)
def greet(name):
    print(f"Hello, {name}!")

# Call the decorated function
greet("Bob")


# 27
# Class vs Static Method Example:
def class_vs_static_method_example():
    class MyClass:
        class_variable = "I am a class variable"

        def __init__(self, value):
            self.instance_variable = value

        @staticmethod
        def static_method(param):
            """Static method example"""
            print(f"Static method called with parameter: {param}")

        @classmethod
        def class_method(cls, param):
            """Class method example"""
            print(f"Class method called with parameter: {param}")
            print(f"Accessing class variable: {cls.class_variable}")

        def instance_method(self):
            """Instance method example"""
            print(f"Instance method called with instance variable: {self.instance_variable}")


    # Using the static method
    MyClass.static_method("Hello")  # Output: Static method called with parameter: Hello

    # Using the class method
    MyClass.class_method("Hello")  # Output: Class method called with parameter: Hello
                                    #         Accessing class variable: I am a class variable

    # Creating an instance of MyClass
    obj = MyClass("Instance Value")

    # Using instance methods
    obj.instance_method()           # Output: Instance method called with instance variable: Instance Value

                                    # Static method can be called on instances, but it's not typical
    obj.static_method("World")      # Output: Static method called with parameter: World

                                    # Class method can also be called on instances, but it's more common to call on the class itself
    obj.class_method("World")       # Output: Class method called with parameter: World
                                    # Accessing class variable: I am a class variable


class_vs_static_method_example()


# 28
# 28.1
# Descriptor Protocol:
# A set of methods that allow to define how attributes are accessed and modified in objects.

def descriptor_example():
    class Descriptor:
        def __init__(self, name):
            self.name = name

        def __get__(self, instance, owner):
            print(f"Getting {self.name}")
            return instance.__dict__.get(self.name, None)

        def __set__(self, instance, value):
            print(f"Setting {self.name} to {value}")
            instance.__dict__[self.name] = value

        def __delete__(self, instance):
            print(f"Deleting {self.name}")
            del instance.__dict__[self.name]

    class MyClass:
        x = Descriptor('x')
        y = Descriptor('y')

        def __init__(self, x, y):
            self.x = x
            self.y = y

    # Instantiate the class
    obj = MyClass(10, 20)

    # Access the descriptors
    print(obj.x)  # Output: Getting x\n10
    obj.x = 30    # Output: Setting x to 30
    del obj.x     # Output: Deleting x
    print(obj.x)  # Output: Getting x\nNone


# 28.2
# Property

def property_example():
    class MyClass:
        def __init__(self, value):
            self._value = value

        @property
        def value(self):
            print("Getting value")
            return self._value

        @value.setter
        def value(self, new_value):
            print(f"Setting value to {new_value}")
            if new_value < 0:
                raise ValueError("Value cannot be negative")
            self._value = new_value

        @value.deleter
        def value(self):
            print("Deleting value")
            del self._value

    # Usage
    obj = MyClass(10)
    print(obj.value)  # Getting value\n10
    obj.value = 20    # Setting value to 20
    print(obj.value)  # Getting value\n20

    try:
        obj.value = -10  # Raises ValueError
    except ValueError as e:
        print(e)  # Value cannot be negative

    del obj.value     # Deleting value
    

property_example()


# 29
# Pickling, Shelving, Json Writing/Reading

def pickling_shelving_json():
    import json
    import pickle

    dct = {'Name' : 'Tony', 'Age' : '38'}

    print("writing json file...")

    with open('my_dict.json', 'w') as file:
        json.dump(dct, file)

    print("reading json file...")
    with open('my_dict.json') as f:
        my_dict = json.load(f)
        print(my_dict)

    ###
    print("Saving pickle...")
    obj = [11, 22, 33]
    file = open('my_file.obj', 'wb') 
    pickle.dump(obj, file)
    file.close()

    print("Loading pickle...")
    file = open('my_file.obj', 'rb') 
    obj = pickle.load(file)
    print(obj)
    file.close()


pickling_shelving_json()


# Python, PySpark, Pandas, Databricks, Dask, Django, Flask, FastAPI, Tornedo, Redis, RabbitMQ
# Pydantic

# 30
# Reading config.ini files


# 31
# Logging in Python


# 32
# Multithreading


# 33
# Multitprocessing


# 34
# AsyncIO


# 35
# Multitprocessing


# 36
# Metaprogramming - Metaclasses


# 37
# Metaprogramming - Dynamic Class creation at run time


# 38
# Metaprogramming - Class Decorators


# 39
# Concurrency - async - await


# 40
# Coroutines 


# 41
# Memory Profiler


# 42
# Performance Optimization


# 43
# Advanced Data Structures - "namedtuple", "dataclasses", and "collections.abc"


# 44
# Functional Programming Libraries - "toolz", "functools".


# 45
# Type Hinting and Static Typing - Static type checking with "MyPy",


# 46
# Memory-Mapped Files - "mmap"


# 47
# Cython


# 48
# Python Bytecode: Examining and manipulating Python bytecode


# 49
# Creating Python Packages: Structuring and distributing packages with "setuptools"


# 50
# Event-Driven Programming: Using libraries like "Twisted" or "Tornado".


# 51
# Cryptography: Using libraries like "cryptography" and "PyCrypto".
