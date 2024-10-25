# collections.abc 
# This module in Python provides abstract base classes (ABCs) for data structures that are part of the collections module.
# 
# These ABCs define a standard way to check if a class conforms to a particular interface (e.g., Iterable, Mapping, Sequence) 
# and allow to create custom collections by inheriting from these classes.
# 
from collections.abc import Iterable


# Check if a list is an instance of Iterable
print(isinstance([1, 2, 3], Iterable))  # Output: True


# Check if an integer is an instance of Iterable
print(isinstance(42, Iterable))  # Output: False




class MyList(Iterable):
    def __init__(self, *args):
        self.items = list(args)

    def __iter__(self):
        # Return an iterator over the list of items
        return iter(self.items)


# Create an instance of MyList
my_list = MyList(1, 2, 3, 4, 5)

# Iterate over it, just like you would with a regular list
for item in my_list:
    print(item)

