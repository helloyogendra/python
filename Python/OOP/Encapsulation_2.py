# OOP - Encapsulation - Data Hiding
# Demo for Protected Attributes

# Use Single Underscore before name of a attribute or method to mark it protected
# Protected members (attributes or methods) are available for a child class

class Car:

    def __init__(self, brand, model, price):
        print("Car init called...")
        self.brand = brand                          # Public attribute/variable
        self._model = model                         # Protected attribute/variable, starts with single underscore
        self.__price = price                        # Private attribute/variable, starts with double underscore

    
    def get_car_info(self):
        print(f'Brand: {self.brand}, Model: {self._model}')
    

    def __str__(self):
        return f'Class: Car, Brand: {self.brand}, Model: {self._model}'



# 'Car' is Parent Class / Base Class / Super Class
# 'SportsCar' is Child class / Derived class / sub class
class SportsCar(Car):

    def __init__(self, brand, model, price, speed):
        print("SportsCar init called...")

        super().__init__(brand, model, price)               # calling init of parent class

        self.speed = speed                                  # attribute/variable of SportsCar


    def check_speed(self):
        print(f"Speed of sport car is {self.speed} km/h")
        print(f"Model : {self._model}")                     # Accessing a protected member of parent class from child class function




sport_car_1 = SportsCar("Audi", "Q3", 30000, 250)

sport_car_1.get_car_info()


print(sport_car_1._model)           # Accessing a protected member through an object, yes allowed but not suggested


