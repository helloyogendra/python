import pytest

@pytest.fixture(scope="class")
def csv_data():
   
    # Replace 'data.csv' with the actual path to your CSV file
    csv_path = 'data.csv'
    
    # Read CSV file into a list of dictionaries
    with open(csv_path, 'r') as file:
        rows = [line.strip().split(',') for line in file.readlines()]
    
    # Provide rows as parameters
    return rows


class TestClass:
    value = 1

    def test_one(self):
        lst = [1, 2, 3, 1]
        final = None

        for item in lst:
            self.value = 1
            print("\n value = ", item)
            final = item
            self.std_one()

        assert self.value == final

    @pytest.mark.parametrize(pytest.fixture("csv_data"))
    def test_two(self, row):
        id, name, mobile = row.split()
        print("\n printed :: ", id, name, mobile)
        self.std_one()
        assert self.value == 1

    def std_one(self):
        TestClass.value = 7
        print("\nClass ==> ", self.check())

    #it will generate warning
    #def test_check(self):
    #   return TestClass.value
    
    
    def check(self):
        return TestClass.value
    

## run pytest
## cd C:\Users\hello\git\python\Pytesting
## pytest -sv .\pytest_class_1.py