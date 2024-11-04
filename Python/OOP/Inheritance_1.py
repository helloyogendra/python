# OOP - Inheritance
# Demo for Inheritance between Classes

# Parent class - the class whose properties and methods will be inherited in a child class
# Child class - the class which is going to inherit from the parent class

# 1.

# Parent
class Animal:

    def __init__(self, name) -> None:
        self.name = name

    
    def speak(self):
        print(f' The animal {self.name} makes a sound')



# Child class Cat is inheriting from Parent class Animal
class Cat(Animal):
    
    # spaek method from Animal class will be suppresed
    # Cat class is overiding the speak method by defining its own spaek method
    def speak(self):
        print(f' The cat {self.name} makes a sound of meow')



# create an instance of Cat class
cat = Cat("Bilbo")

cat.name = 'Joro'

cat.speak()                 # calling speak () method of Cat class