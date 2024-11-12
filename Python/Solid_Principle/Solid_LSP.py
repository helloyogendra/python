# Liskov Substitution Principle (LSP)

# LSP states that objects of a superclass should be replaceable with objects of a subclass without affecting the correctness of the program. 
# In other words, subclasses should behave in a way that their base classes expect.

# Importance
# Reliability: Ensures that subclass instances can be used interchangeably with superclass instances.
# Polymorphism: Facilitates the use of polymorphic behaviors without unexpected side effects.
# Robustness: Prevents bugs that arise from improper subclass implementations.

# # Violation Example
# A `Bird` superclass with a `fly` method and a `Penguin` subclass that cannot fly:
# # Violates LSP: Penguin cannot fly, but inherits fly method

class Bird:
    def fly(self):
        pass


class Sparrow(Bird):
    def fly(self):
        print("Sparrow flying")


class Penguin(Bird):
    def fly(self):
        raise NotImplementedError("Penguins can't fly")
    

# Issue: Replacing `Bird` with `Penguin` leads to runtime errors.


### LSP-Compliant Example
# Redefine the class hierarchy to avoid such violations:

from abc import ABC, abstractmethod

class Bird(ABC):
    @abstractmethod
    def move(self):
        pass

# FlyingBird -> Bird
class FlyingBird(Bird):
    @abstractmethod
    def fly(self):
        pass

# Sparrow -> FlyingBird -> Bird
class Sparrow(FlyingBird):
    def fly(self):
        print("Sparrow flying")

    def move(self):
        self.fly()
 
# Penguin -> Bird
class Penguin(Bird):
    def move(self):
        print("Penguin walking")



sp = Sparrow();
sp.fly();
sp.move();

pg = Penguin();
pg.move();



# Benefits:
# - `Penguin` no longer inherits a `fly` method it cannot implement.
# - Clear separation of bird types based on their capabilities.
# - Subclasses adhere to the expectations set by their abstract base classes.