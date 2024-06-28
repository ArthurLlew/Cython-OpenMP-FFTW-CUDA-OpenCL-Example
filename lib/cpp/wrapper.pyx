###########
# IMPORTS #
###########


# Cython
import cython
# Numpy
import numpy as np
cimport numpy as np #This import is required to access np.complex128_t


########
# CODE #
########


# External C++ function
cdef extern from "gcclib.cpp":
    void do_fft_c(np.complex128_t* arr, int n, int m)


# Wrap function
@cython.boundscheck(False)
@cython.wraparound(False)
def do_fft(arr):
    # Makes a contiguous copy of the numpy array
    if not arr.flags['C_CONTIGUOUS']:
        arr = np.ascontiguousarray(arr)

    # Memory view for the array
    cdef np.complex128_t [:, ::1] arr_memview = arr

    # Call function
    do_fft_c(&arr_memview[0,0], arr_memview.shape[0], arr_memview.shape[1])

    return arr