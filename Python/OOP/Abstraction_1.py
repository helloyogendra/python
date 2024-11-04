# OOP - Abstraction
# Demo for Abstract Class

# We can not create object/instance of abstract class.
# We need to use an Abstract class like a parent class.
# We can have abstract methods inside an abstract class

from abc import ABC, abstractmethod

# A Parent/Abstract class
class Vehicle(ABC):

    @abstractmethod
    def start_engin(self):
        pass


    @abstractmethod
    def stop_engin(self):
        pass


# A child class
class Car(Vehicle):

    
    def start_engin(self):
        print('Car is started')


    
    def stop_engin(self):
        print('Car is stopped')


# A child class
class Bike(Vehicle):

    
    def start_engin(self):
        print('Bike is started')


    
    def stop_engin(self):
        print('Bike is stopped')


car = Car()         # object of Car class

car.start_engin()
car.stop_engin()

bike = Bike()       # object of bike class

bike.start_engin()
bike.stop_engin()


