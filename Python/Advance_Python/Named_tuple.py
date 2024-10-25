from collections import namedtuple

# namedtuple is immutable

# Creating a namedtuple
Point = namedtuple('Point', ['x', 'y'])

p1 = Point(x = 10, y = 10)

print(type(p1), " : ", p1)


Car = namedtuple('Car', ['make', 'model', 'year', 'price'])

# Create instances of the Car namedtuple
car1 = Car(make='Toyota', model='Camry', year=2020, price=24000)
car2 = Car(make='Honda', model='Civic', year=2019, price=22000)

# Print the instances and attribute value or value by index
print(car1)

print(car2.price)
print(car1[0])      

make, model, year, price = car1     # unpacking like regular tuple

print(model)


# Create a new Car with a modified price using _replace()
car3 = car1._replace(price=23000)
print(car3)

# Convert car1 to an ordered dictionary
car_dict = car1._asdict()
print(car_dict)



# When to Use namedtuple

#     When you need structured, readable data containers.
#     When immutability is important (no accidental changes to data).
#     When you want memory-efficient objects (lighter than regular classes).


