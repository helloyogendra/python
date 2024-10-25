# dataclasses 
# mutable by default, can be made immutable
# Python 3.7

# Provide a simple way to create classes that are primarily used to store data. 
# Automatically Generated Methods - __init__, __eq__, __repr__

# Using __post_init__ Method

#     You can define a __post_init__ method to customize object initialization.
#     Useful for additional validation or computations after the __init__ method runs.


from dataclasses import dataclass



@dataclass
class Car:
    make: str
    model: str
    year: int
    price: float = 25000        # default value can be added


    def __post_init__(self):

        # Ensure the price is positive
        if self.price < 0:
            raise ValueError("Price cannot be negative")


# Create instances of the Car dataclass
car1 = Car(make='Toyota', model='Camry', year=2020, price=24000.0)
car2 = Car(make='Honda', model='Civic', year=2019, price=22000.0)

# Will raise an error if the price is negative
try:
    car4 = Car(make='Tesla', model='Model S', year=2021, price=-50000)
except ValueError as e:
    print(e)



# Print the instances
print(car1)
print(car2)




# Making dataclass Immutable (like namedtuple)

@dataclass(frozen=True)
class Vehicle:
    make: str
    model: str
    year: int
    price: float

car5 = Vehicle(make='Chevrolet', model='Malibu', year=2020, price=26000.0)

# car5.price = 25000.0  # This will raise an error because the dataclass is frozen
