# Dependency Inversion Principle (DIP)
# **DIP** states that high-level modules should not depend on low-level modules; both should depend on abstractions. 
# Additionally, abstractions should not depend on details; details should depend on abstractions.

# **Importance**
# Decoupling:** Reduces the dependency between high-level and low-level modules.
# Flexibility:** Facilitates changing low-level implementations without affecting high-level logic.
# Testability:** Makes it easier to mock dependencies during testing.

# **Violation Example**
# A `ReportGenerator` class directly depends on a `Database` class:

class Database:
    def get_data(self):
        # Fetch data from the database
        return "Data from DB"
    

class ReportGenerator:
    def __init__(self):
        self.database = Database()

    def generate(self):
        data = self.database.get_data()
        return f"Report with {data}"
    
# **Issue:** `ReportGenerator` is tightly coupled to `Database`. 
# Changing `Database` or using a different data source requires modifying `ReportGenerator`.


### **DIP-Compliant Example**
# Depend on abstractions (interfaces) rather than concrete implementations:

from abc import ABC, abstractmethod
# Abstraction
class DataSource(ABC):
    @abstractmethod
    def get_data(self):
        pass


# Low-level module
class Database(DataSource):
    def get_data(self):
        return "Data from DB"


class APIService(DataSource):
    def get_data(self):
        return "Data from API"


# High-level module
class ReportGenerator:
    def __init__(self, data_source: DataSource):
        self.data_source = data_source

    def generate(self):
        data = self.data_source.get_data()
        return f"Report with {data}"


# Usage
database = Database()
report = ReportGenerator(database)
print(report.generate()) # Output: Report with Data from DB

api_service = APIService()
report = ReportGenerator(api_service)
print(report.generate()) # Output: Report with Data from API


# **Benefits:**
# - `ReportGenerator` can work with any `DataSource` implementation.
# - Adding new data sources doesn't require modifying `ReportGenerator`.
# - Enhances modularity and adherence to DIP.
