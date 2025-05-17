import os

from llvmlite import binding
from numba import njit
from numba.core import types
from numba.core import typing

# load the library into LLVM
path = os.path.abspath("./add_ints.so")
binding.load_library_permanently(path)

# Adds typing information
c_func_name = "sum"
return_type = types.int64
argty = types.int64
c_sig = typing.signature(return_type, argty, argty)
c_func = types.ExternalFunction(c_func_name, c_sig)


@njit
def example(x, y):
    return c_func(x, y)


print(example(3, 4))  # 7
