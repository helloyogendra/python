# Interface Segregation Principle (ISP)

# ISP advises that no client should be forced to depend on methods it does not use. 
# Instead of having large, monolithic interfaces, create smaller, more specific ones.

# Importance
# Decoupling: Reduces the interdependencies between classes.
# Flexibility: Allows clients to use only the methods they need.
# Maintainability: Smaller interfaces are easier to understand and modify.

# Violation Example
# A `Printer` interface that includes both printing and scanning:

from abc import ABC, abstractmethod

class Printer(ABC):
    @abstractmethod
    def print(self, document):
        pass

    @abstractmethod
    def scan(self, document):
        pass


class BasicPrinter(Printer):
    def print(self, document):
        print(f"Printing {document}")

def scan(self, document):
    raise NotImplementedError("BasicPrinter cannot scan")


# Issue: `BasicPrinter` is forced to implement a `scan` method it doesn't support.

# ISP-Compliant Example
# Separate interfaces for different functionalities:

from abc import ABC, abstractmethod
class Printer(ABC):
    @abstractmethod
    def print(self, document):
        pass
    

class Scanner(ABC):
    @abstractmethod
    def scan(self, document):
        pass


class MultiFunctionPrinter(Printer, Scanner):
    def print(self, document):
        print(f"Printing {document}")   

    def scan(self, document):
        print(f"Scanning {document}")


class BasicPrinter(Printer):
    def print(self, document):
        print(f"Printing {document}")



# Benefits:
# - `BasicPrinter` only implements the `Printer` interface.
# - Clients can depend on specific interfaces (`Printer` or `Scanner`) without unnecessary methods.
# - Enhances modularity and flexibility.