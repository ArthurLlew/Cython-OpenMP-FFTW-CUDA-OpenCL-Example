// Used by dll exporter
#ifdef CUDADLL_EXPORTS
#define DLLEXPORT __declspec(dllexport)
#else
#define DLLEXPORT __declspec(dllimport)
#endif

// Complex numbers
#include <complex>

// Exposed function
extern "C" DLLEXPORT void cuda_func(std::complex<double> *matrix, int n, int m);