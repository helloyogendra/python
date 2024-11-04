# Step - 1 -> pip install cython
# Step - 2 -> Write Cython Code -> Cython_Code.pyx
# Step - 3 -> Use a setup script (setup.py) to compile the Cython code.
# Step - 4 -> Command to compile Cython/.pyx file -> python setup.py build_ext --inplace
# Step - 5 -> Import Cython module/function in Python file -> from Cython_Code import cython_sum
# Step - 6 -> Run the Python file/run_python.py in usual way

from Cython_Code import cython_sum, cython_nested_loop

import time

def python_sum(n):
    s = 0
    for i in range(n):
        s += i
    return s

def python_nested_loop(i, j):
    s = 0
    for i in range(i):
        for j in range(j):
            s = i + j
    return s

a = time.perf_counter()
print(cython_sum(1_000_000_000))
print("Cython Sum -> ", time.perf_counter() - a)            # 0.13 seconds, that is less than 1 second for 1 billion loop


a = time.perf_counter()
print(cython_nested_loop(1_00_000, 1_00_000))
print("Cython Nested Loop -> ", time.perf_counter() - a)    # 1.46 Seconds


a = time.perf_counter()
print(python_sum(1_000_000_000))
print("Python Sum -> ", time.perf_counter() - a)            # 25 to 28 seconds, for 1 billion loop


a = time.perf_counter()
print(python_nested_loop(1_00_000, 1_00_000))
print("Python Nested Loop-> ", time.perf_counter() - a)     #  122 Seconds


