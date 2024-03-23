from .. import module2
 

def test_sub():
    x = 40
    y = 10
    rs1 = 30
    rs2 = module2.sub(x, y)
    print("Printing test module-2")
    assert rs1 == rs2