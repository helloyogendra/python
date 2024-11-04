# OOP - Encapsulation - Data Hiding
# Property

class Circle:
    def __init__(self, radius):
        self.__radius = radius                         
       

    @property
    def radius(self):
       return self.__radius
    

    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError('Radius can not be less than zero')
        
        self.__radius = value

    
    @property
    def area(self):
        return 3.14 * (self.__radius ** 2)
        
    


# Remeber these are properties and not function
# Accessing these properties


circle = Circle(7)          # create an object

print(circle.radius)        # reading radius through property

print(circle.area)

circle.radius = 5           # chaging the value of private attribute through property setter

print(circle.area)


# circle.radius = -2        # Expect exception here