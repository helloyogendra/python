from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def test_func():
        pass

    @property
    @abstractmethod
    def area(self):
        """Calculate the area of the shape."""
        pass

    @property
    @abstractmethod
    def perimeter(self):
        """Calculate the perimeter of the shape."""
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def area(self):
        return self._width * self._height

    @property
    def perimeter(self):
        return 2 * (self._width + self._height)
    
    def test_func(self):
        print("Hello Rectangle")

class Circle(Shape):
    def __init__(self, radius):
        self._radius = radius

    @property
    def area(self):
        import math
        return math.pi * (self._radius ** 2)

    @property
    def perimeter(self):
        import math
        return 2 * math.pi * self._radius
    
    def test_func(self):
        print("Hello Circle")

# Instantiate and use the classes
print("")

rectangle = Rectangle(5, 10)
print(f"Rectangle Area: {rectangle.area}")  # Output: Rectangle Area: 50
print(f"Rectangle Perimeter: {rectangle.perimeter}")  # Output: Rectangle Perimeter: 30
rectangle.test_func()

print("")

circle = Circle(7)
print(f"Circle Area: {circle.area}")  # Output: Circle Area: 153.93804002589985
print(f"Circle Perimeter: {circle.perimeter}")  # Output: Circle Perimeter: 43.982297150257104
circle.test_func()
