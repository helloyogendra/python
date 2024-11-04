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




