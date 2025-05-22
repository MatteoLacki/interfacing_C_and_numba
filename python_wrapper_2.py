import ctypes

from numba import njit

DSO = ctypes.CDLL("./add_ints.so")

# Add typing information
c_func = DSO.sum
c_func.restype = ctypes.c_int
c_func.argtypes = [ctypes.c_int, ctypes.c_int]


@njit
def example(x, y):
    return c_func(x, y)


print(example(3, 4))  # 7
print(example.py_func(3, 4))  # 7
c_func(2, 6)
