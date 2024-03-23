# test_main.py
import pytest

from .. import main

def test_end_to_end():
    # Trigger the first module test directly or by using pytest.mark.parametrize to
    # dynamically determine the test flow.
    result_module1 = main.main_func()
    print("Printing main = ", result_module1)
    assert result_module1
    
