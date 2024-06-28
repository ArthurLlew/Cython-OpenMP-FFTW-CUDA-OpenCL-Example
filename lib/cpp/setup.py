###########
# IMPORTS #
###########


# Handy arrays
import numpy as np
# OS
import os
# Tools to build module
from setuptools import setup, Extension
# Cython
from Cython.Build import cythonize


########
# CODE #
########


# Create extension to build it futher down
ext = Extension(# Extension name (mandatory)
                'gcclib',
                # Cython source file
                sources=['wrapper.pyx'],
                # Compiler language
                language='c++',
                # Compiler arguments
                # 1) Use OpenMP
                extra_compile_args=['/openmp'],
                # List of directories to search for C/C++ header files
                # 1) Is neaded for numpy types to work properly in .pyx
                # 2) Path to the FFTW header files
                # 3) Path to the OpenCL include directory
                # 4) Path to the custom Cuda library header files
                include_dirs=[np.get_include(),
                              os.path.join('..', '3rd_party_libs', 'fftw'),
                              os.path.join(os.environ['CUDA_PATH'], 'include'),
                              os.path.join('..', 'cudalib')],
                # List of extra files to link with (eg. .lib files)
                # 1) Path to the FFTW lib
                # 2) Path to the OpenCL lib
                # 3) Path to the custom Cuda lib
                extra_objects=[os.path.join('..', '3rd_party_libs', 'fftw', 'libfftw3-3.lib'),
                               os.path.join(os.environ['CUDA_PATH'], 'lib', 'x64', 'OpenCL.lib'),
                               os.path.join('..', 'cudalib', './cudalib.lib')])

# Build extention
setup(ext_modules = cythonize([ext]))