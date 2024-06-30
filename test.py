###########
# IMPORTS #
###########


# Handy arrays
import numpy as np
# FFT
import scipy.fft as fft
# Custom module
from lib.cpp.gcclib import do_fft


########
# CODE #
########


# Complex double presision array
arr = np.zeros((4,4), dtype=np.complex128)

# Run C++ code and print result
do_fft(arr)
print('do_fft result:')
print(arr)

# Do same computation, but with python
X, Y = np.ogrid[:arr.shape[0],:arr.shape[1]]
fft_res = fft.fft2((X+Y).astype(np.complex128))
fft_res.real += X
fft_res.imag += Y
print('Python result:')
print(fft_res)


# NOTE: you can allways call dll explicitly with ctypes like this

import ctypes as ct

cudalib = ct.CDLL('./lib/cudalib/cudalib')
# Define dll function
cudalib.cuda_func.argtypes = np.ctypeslib.ndpointer(dtype=np.complex128, ndim=2), ct.c_size_t, ct.c_size_t
cudalib.cuda_func.restype = None

# Complex double presision array (you can even use slices when calling dll function!)
arr2 = np.zeros((5, 4,4), dtype=np.complex128)
# Make array C contiguous
if not arr2.flags['C_CONTIGUOUS']:
    arr2 = np.ascontiguousarray(arr2)
cudalib.cuda_func(arr2[0, :, :], *arr.shape)