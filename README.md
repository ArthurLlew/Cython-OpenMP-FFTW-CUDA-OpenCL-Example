Example of using OpenMP, FFTW, CUDA and OpenCL in Cython module:
==============================
This example shows how to setup project for Cython module that uses OpenMP, FFTW, CUDA and OpenCL on Windows x64.
A lot of information about this topic can be found online but there are no full examples on how to do something like this.

Features:
------------------------------
There is a .vscode folder for Visual Studio Code IDEA to properly interpret C++ code.

Project contains:
1) Python code to test Cython module
2) Cython module written in Cython and C++
3) FFTW library files (can be downloaded here https://www.fftw.org/install/windows.html)
4) CUDA library (look inside to find instructions on how to compile it)
3) Invocation of FFTW and CUDA libraries, use of OpenMP and OpenCL in C++ code of Cython module

**Note:**  OpenCL is not used like CUDA because it misses built-in complex type unlike CUDA. Technically C/C++ ```complex``` type is either ```float2``` or ```double2``` so it is possible to wrap it up with appropriate ```complex``` behaviour in OpenCL kernel.
A great example can be found in PyOpenCL project: https://github.com/inducer/pyopencl/blob/main/pyopencl/cl/pyopencl-complex.h