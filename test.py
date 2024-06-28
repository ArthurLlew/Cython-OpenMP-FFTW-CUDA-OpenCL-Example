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