# Cython_Code.pyx

def cython_sum(long long n):
    cdef long long s = 0
    cdef long long i
    for i in range(n):
        s += i
    return s


def cython_nested_loop(int i, int j):
    cdef int s = 0
    for i in range(i):
        for j in range(j):
            s = i + j
    return s
