import pytest

@pytest.fixture(scope="class")
def csv_data():
    csv_path = 'data.csv'
    
    with open(csv_path, 'r') as file:
        rows = [line.strip().split(',') for line in file.readlines()]
    return rows


class TestClass:
    value = 1

    @pytest.mark.parametrize("row", pytest.fixture("csv_data"))
    def test_two(self, row):
        print("type is = ", type(row))
        print("row is = ", row)

        # id, name, mobile = row
        # print("\n printed :: ", id, name, mobile)
        # self.std_one()
        assert self.value == 1

## run pytest
## cd C:\Users\hello\git\python\Pytesting
## pytest -sv .\pytest_class_2.py
