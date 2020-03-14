#include "api.h"

extern "C"
{
    int get() { return 42; }
    int add(int x, int y) { return x + y; }
    float add_float(float x, float y) { return x + y; }
    void saxpy(unsigned int n, float a, const float* x, float* y)
    {
        for (unsigned int i = 0; i < n; ++i)
        {
            y[i] = a * x[i] + y[i];
        }
    }
}
