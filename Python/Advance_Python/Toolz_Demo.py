# pip install toolz

from toolz import dicttoolz as dz
from toolz import functoolz as fz
from toolz import itertoolz as iz



# pipe()
# set up pipelines for processing data without the need to save intermediate variables

def func_1(x):
    return x + 2


def func_2(x):
    return x - 2


def func_3(x):
    return x * 2


funcs = [func_1, func_2, func_3]
result = fz.pipe(10, *funcs)            # (10 + 2) -> 12 -> (12 - 2) -> 10 -> (10 * 2) -> 20  : Single result 20 produced
print(result)


# juxt() 
# Call multiple functions on one input

funcs = [func_1, func_2, func_3]
result = fz.juxt(funcs)(10)
print(result)                           # (10 + 2) -> 12, (10 - 2) -> 8, (10 * 2) -> 20  : Three results (12, 8, 20) produced

a1 = ['ab', 'bc', 'cd']
a2 = ['xy', 'yz', 'za']

print([item.capitalize() for item in a1 + a2])