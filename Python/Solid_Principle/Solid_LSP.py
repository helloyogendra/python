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
