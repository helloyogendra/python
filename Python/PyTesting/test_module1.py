from .. import module1

def test_add():
    x = helper_func_1()
    y = helper_func_2()
    rs1 = 32
    rs2 = module1.add(x, y)
    print("Printing test module-1 : rs2 = ", rs2)
    assert rs1 == rs2


def helper_func_1():
    return 11


def helper_func_2():
    return 11 + 10

# running
# C:\Yogi_Data\pytest_project> pytest -sv .\pytest_testing 