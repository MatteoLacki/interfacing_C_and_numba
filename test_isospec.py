import ctypes

from numba import carray
from numba import cfunc
from numba import njit
from numba import types
from numba.extending import get_cython_function_address

import os

from llvmlite import binding
from numba import njit
from numba.core import types
from numba.core import typing

import IsoSpecPy
import numba

from IsoSpecPy.isoFFI import isoFFI

import ctypes

lib = ctypes.CDLL(
    "./ve_Cnumba/lib/python3.12/site-packages/IsoSpecCppPy.cpython-312-x86_64-linux-gnu.so"
)
cfunc = lib.getHeaviestPeakMassIso
cfunc.restype = ctypes.c_double
cfunc.argtypes = [ctypes.POINTER(ctypes.c_int)]

x = IsoSpecPy.Iso("C10")
cfunc(x)


@njit
def example():
    return cfunc(x)


print(example())  # 7


# Get the raw function pointer
func_ptr = ctypes.cast(lib.getHeaviestPeakMassIso, ctypes.c_void_p).value


@njit
def call_heaviest_peak(ptr):
    return cfunc_type(ptr)


# Declare the signature: double(void*)
sig = types.double(types.voidptr)

# Create a Numba "foreign function" type
from numba import cffi_support
from numba.core import cgutils

# Create a callable function pointer
from numba.types import ExternalFunctionPointer

cfunc_type = ExternalFunctionPointer(sig, ptr=func_ptr)


# Now you can call it from JIT-compiled functions
@njit
def call_heaviest_peak(ptr):
    return cfunc_type(ptr)
