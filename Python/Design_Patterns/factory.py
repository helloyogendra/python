# Factory Design Patterns:
# 
# Version - 1

from abc import ABC, abstractmethod

# Product interface
class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

# Concrete Products
class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

# Factory
class AnimalFactory:
    @staticmethod
    def get_animal(animal_type: str) -> Animal:
        if animal_type == "Dog":
            return Dog()
        elif animal_type == "Cat":
            return Cat()
        else:
            raise ValueError("Unknown animal type")


# Client code
if __name__ == "__main__":

    animal1 = AnimalFactory.get_animal("Dog")
    print(animal1.speak())                          # Output: Woof!

    animal2 = AnimalFactory.get_animal("Cat")
    print(animal2.speak())                          # Output: Meow!



# 
# Version - 2

from enum import Enum
from abc import ABC, abstractmethod
from typing import Annotated, TypeAlias, NewType


class Shape_Keys(Enum):
    CIRCLE = "circle"
    SQUARE = "square"
    RECTANGLE = "rectangle"


# Product interface
class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass

# Concrete Products
class Circle(Shape):
    def draw(self):
        return "Drawing a Circle"

class Square(Shape):
    def draw(self):
        return "Drawing a Square"

# Factory
class ShapeFactory:
    @staticmethod
    def get_shape(shape_type: Shape_Keys) -> Shape:
        if shape_type == Shape_Keys.CIRCLE:
            return Circle()
        elif shape_type == Shape_Keys.SQUARE:
            return Square()
        else:
            raise ValueError("Unknown shape type")


# Client code
if __name__ == "__main__":

    Fact: TypeAlias = ShapeFactory

    shape1 = Fact.get_shape(Shape_Keys.CIRCLE)
    print(shape1.draw())                            # Output: Drawing a Circle

    shape2 = Fact.get_shape(Shape_Keys.SQUARE)
    print(shape2.draw())                            # Output: Drawing a Square


