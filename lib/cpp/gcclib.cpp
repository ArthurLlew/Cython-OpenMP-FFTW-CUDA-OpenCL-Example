// Used to get std::cout
#include <iostream>
// Standart library
#include <stdlib.h>
// Complex numbers
#include <complex>
// OpenMP
#include <omp.h>
// FFTW
#include "../3rd_party_libs/fftw/fftw3.h"
// CUDA
#include "../cudalib/cudalib.h"
// OpenCL
#define CL_USE_DEPRECATED_OPENCL_2_0_APIS
#include <CL/cl.hpp>


void do_fft_c(std::complex<double> *arr, int n, int m)
{
    // OpenMP loop to fill in some values
    #pragma omp parallel for
    for (int i = 0; i < n; i+=1)
    {
        for (int j = 0; j < m; j+=1)
        {
            arr[i * m + j] += i + j;
        }
    }

    // Perform FFT with FFTW
    fftw_plan p = fftw_plan_dft_2d(n, m, reinterpret_cast<fftw_complex*>(arr), reinterpret_cast<fftw_complex*>(arr), FFTW_FORWARD, FFTW_ESTIMATE);
    fftw_execute(p);
    fftw_destroy_plan(p);

    // Call Cuda code
    cuda_func(arr, m, n);

    // OpenCL test code (just print platform info)
    std::cout << "Printing OpenCL info:\n";

    // get all platforms (drivers), e.g. NVIDIA
    std::vector<cl::Platform> all_platforms;
    cl::Platform::get(&all_platforms);

    cl::Platform default_platform = all_platforms[0];
    std::cout << "Using platform: " <<default_platform.getInfo<CL_PLATFORM_NAME>() << "\n";

    std::vector<cl::Device> all_devices;
    default_platform.getDevices(CL_DEVICE_TYPE_ALL, &all_devices);
    if (all_devices.size() == 0) {
        std::cout << " No devices found.\n";
        exit(1);
    }

    cl::Device default_device = all_devices[0];
    std::cout << "Using device: " << default_device.getInfo<CL_DEVICE_NAME>() << "\n";
}