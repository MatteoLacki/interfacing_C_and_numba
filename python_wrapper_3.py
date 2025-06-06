import ctypes
import numpy as np

from numba import cfunc
from numba import njit
from numba import types

# Load the shared library
lib = ctypes.CDLL("./libmyarray.so")

# Set return and argument types
lib.make_array.argtypes = [ctypes.c_int]
lib.make_array.restype = ctypes.POINTER(ctypes.c_int)


# Wrapper function to convert to NumPy array
def get_array(n):
    ptr = lib.make_array(n)
    if not ptr:
        raise MemoryError("C malloc failed")

    # Create a numpy array from the raw pointer
    arr = np.ctypeslib.as_array(ptr, shape=(n,))
    return arr


get_array(10)


@njit
def process_array(arr):
    total = 0
    for i in range(arr.shape[0]):
        total += arr[i]
    return total


n = 10
arr = get_array(n)  # Call C code
result = process_array(arr)  # Use inside Numba
print(result)
