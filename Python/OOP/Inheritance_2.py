# OOP - Inheritance
# Demo for Inheritance between Classes

# Multilevel Inheritance

# Class A -> Class B -> class C

# 1.

# Parent [Like grandparent]
class Vehicle:

    def __init__(self, brand) -> None:
        self.brand = brand

    
    def start(self):
        print(f' The vehicle {self.brand} started')



# Child Class of Vehicle but it is Parent class for SportsCar
class Car(Vehicle):

    def __init__(self, brand, model) -> None:
        super().__init__(brand)
        self.model = model
    
    def drive(self):
        print(f' The Car {self.model} is in drive mode')



# Child Class of Car
class SportsCar(Car):

    def __init__(self, brand, model, speed_limit) -> None:
        super().__init__(brand, model)
        self.speed_limit = speed_limit
    
    def speed(self):
        print(f' The Speed of SportCar is {self.speed_limit} ')



# creating the object of child class
my_sport_car = SportsCar('Ferrari', 'F1', 350)

my_sport_car.start()        # method from Vehicle class

my_sport_car.drive()         # method from Car class

my_sport_car.speed()         # method from SportsCar class


