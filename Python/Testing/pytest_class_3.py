#conftest.py
import os, pytest


@pytest.fixture(scope="class")
def client():

    file = "test.txt"
    path = "C:/Yogi_Data/pytest_project"

    full = os.path.normpath(os.path.join(path, file))

    if os.path.exists(full):
        yield full



@pytest.mark.usefixtures("client")
class TestStaticPages:

    def test_start_1(self, client):

        path = client
        print("\n##################################\n")
        print(path)
        print(type(path))
        print("\n##################################\n")
        assert len(path) > 0

    def test_start_2(self, client):

        path = client
        print("\n=========================================\n")
        print(path)
        print(type(path))
        print("\n=======================================\n")
        assert len(path) < 0

    def test_start_3(self, client):

        path = client
        print("\n***************************************************\n")
        print(path)
        print(type(path))
        print("\n***************************************************\n")
        assert len(path) == 0


## run pytest
## cd C:\Users\hello\git\python\Pytesting
## pytest -sv .\pytest_class_3.py