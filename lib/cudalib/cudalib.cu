// Header file for this code
#include "cudalib.h"
// Complex numbers for device
#include <cuComplex.h>


// Kernel code
__global__ void kernel(cuDoubleComplex *matrix, int n, int m)
{
    // i nad j are now obtained via blocks and threads
    int i = blockIdx.x * blockDim.x + threadIdx.x;
    int j = blockIdx.y * blockDim.y + threadIdx.y;
    // Verify that we are not exceeding array bounds
    if (i < n && j < m)
    {
        matrix[i * m + j] = cuCadd(matrix[i * m + j], make_cuDoubleComplex(i, j));
    }
}


// Function to process FFT
void cuda_func(std::complex<double> *matrix, int n, int m)
{
    // Matrix size
    int size = sizeof(std::complex<double>)*n*m;
    // Make device memory pointer of a compatible complex type
    cuDoubleComplex *matrix_copy;
    // Threads and blocks settings
    // Since we know that we will get array 4x4, we can do block and thread management like this
    // In non-example code this small section should be more complicated
    dim3 threadsPerBlock(n/2, m/2);
    dim3 numBlocks(n/threadsPerBlock.x, m/threadsPerBlock.y);

    // Allocate memory
    cudaMalloc(&matrix_copy, size);

    // Copy input to allocated memory
    cudaMemcpy(matrix_copy, matrix, size, cudaMemcpyHostToDevice);

    // Run kernel
    kernel<<<numBlocks, threadsPerBlock>>>(matrix_copy, n, m);

    // Retrieve result
    cudaMemcpy(matrix, matrix_copy, size, cudaMemcpyDeviceToHost);

    // Free allocated memory
    cudaFree(matrix_copy);
}