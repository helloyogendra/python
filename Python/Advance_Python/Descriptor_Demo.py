# Descriptors
# Python descriptors are a powerful mechanism for customizing attribute access and modification. 
# They allow to define custom behavior when an attribute is accessed, set, or deleted
# 
# When to Use Descriptors:
# to customize attribute access or modification behavior.
# to implement validation or data transformation logic for attributes.
# to create reusable components for attribute management.

# Example - 1:

def descriptor_demo_1():
    import os

    class DirectorySize:

        def __get__(self, obj, objtype=None):
            return len(os.listdir(obj.dirname))


    class Directory:

        size = DirectorySize()              # Descriptor instance

        def __init__(self, dirname):
            self.dirname = dirname          # Regular instance attribute

    # just to make this code full proof
    if not os.path.exists('C:\\Yogi_Data\\UTIC\\delete.txt'):
        os.system('dir > C:\\Yogi_Data\\UTIC\\delete.txt')

    s = Directory('C:\\Yogi_Data\\UTIC')
    g = Directory('C:\\Yogi_Data\\Videos')

    print(s.size)                                           # The songs directory has twenty files

    print(g.size)                                           # The games directory has three files

    os.remove('C:\\Yogi_Data\\UTIC\\delete.txt')            # Delete 

    print(s.size)   



descriptor_demo_1()

# Example - 2:

def descriptor_demo_2():
    import logging

    logging.basicConfig(level=logging.INFO)


    class LoggedAgeAccess:

        def __get__(self, obj, objtype=None):
            value = obj._age
            logging.info('Accessing %r giving %r', 'age', value)
            return value

        def __set__(self, obj, value):
            logging.info('Updating %r to %r', 'age', value)
            obj._age = value

    class Person:

        age = LoggedAgeAccess()             # Descriptor instance

        def __init__(self, name, age):
            self.name = name                # Regular instance attribute
            self.age = age                  # Calls __set__()

        def birthday(self):
            self.age += 1                   # Calls both __get__() and __set__()

        def __repr__(self) -> str:
            return f'{self.name}, {self.age}'

    
    mary = Person('Mary M', 30)
    print(mary)

    dave = Person('David D', 40)
    print(dave)

    print(vars(mary))

    print(vars(dave))



descriptor_demo_2()


# Example
# Using one Descriptor [One property/atttribute] across multiple classes

class PositiveInteger:
    def __get__(self, instance, owner):
        return instance._value
    
    def __set__(self, instance, value):
        if value < 0:
            raise ValueError("Must be positive")
        instance._value = value

class Account:
    balance = PositiveInteger()

class Product:
    stock = PositiveInteger()

acc = Account()
acc.balance = 100

prod = Product()
prod.stock = 50



# Example
# Using Descriptor for type checking / type enforcement

class TypedProperty:
    def __init__(self, name, type_):
        self.name = name
        self.type_ = type_

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, self.type_):
            raise TypeError(f"Expected {self.type_}, got {type(value)}")
        instance.__dict__[self.name] = value

class Person:
    age = TypedProperty("age", int)

person = Person()
person.age = 25  # Valid

# person.age = "25"             # Raises TypeError



