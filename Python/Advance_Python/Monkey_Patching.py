# Monkey Patching
# Dynamic modification of a class at runtime


class Animal:
    def runs(self):
        print("Animal is running")


obj1 = Animal()         # create object of class

obj1.runs()             # accessing the method of class using an instance



# lets define a method outside of this class

def walks(self):
     print("Animal is walking")


def fly(self):
     print("Animal is flying")


Animal.runs = walks     # patching, observe the syntax, runs() method is replaced with behaviour of walks, overwrite 'runs' from 'walks'

obj2 = Animal()         # create object of class

obj2.runs()             # accessing the method of class using an instance


bird = Animal()
Animal.fly = fly        # fix/explore if any issue [added a new method in our class]
bird.fly()              # fix/explore if any issue  [calling the newly added a method of our class]


#
# dynamic attributes

# in this class we have one attribute/variable that is 'color'
class Car:
     def __init__(self):
          self.color = ""



# create an object

car1 = Car()

car1.color = 'Red'

print(car1.color)

car1.brand = 'Honda'        # adding an attribute dynamically

print(car1.brand)

car1.model = 'City'         # adding an attribute dynamically

print(car1.model)

car2 = Car()                # we added the attribute in car1 object can car2 acees it / have it ??


# print(car2.model)         # Exception here ??

# can you add at class level ?? try below
# Car.brand = ""
