# __slots__ 
# By using __slots__ we can have only fix set of attributes [pre-defined attributes]
# If we use slots then we can not add dynamic attributes to our class
# By using slots we can a better class which could be more memory efficient

# Advantages of using slots - memory optimization, performance, fixed design approach.
# Disadvantage - limited flexibility


# Example - without slots
# we can add dynamic attributes 

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

car2 = Car()                # we added the attribute in car1 object can car2 acees it, no it can not

print("")

# Example - with __slots__
# we can not add dynamic attributes 

class Person:
     
    __slots__ = ['name', 'age', 'country']         # define/fix the attributes for this class

    def __init__(self, name, age, country) -> None:
          self.name = name
          self.age = age
          self.country = country

    
    def get_name(self):
         return self.name
    

    def set_name(self, name):
        if name != '':
            self.name = name
        else:
             raise ValueError('Empty name not allowed')
        


# create object of person class

p1 = Person('John', 32, 'Poland')

print(p1.get_name())

print(p1.age)

print(p1.country)

p1.age = 35             # for 'p1' object change the value of attribute 'age'

print(p1.age)


# lets try to add a dynamic attribute

# p1.gender = 'Male' # Not allowed because of slots : AttributeError: 'Person' object has no attribute 'gender'

# print(p1.gender)        
          