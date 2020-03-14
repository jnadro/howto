#pragma once

extern "C" 
{

#if _WIN32
	#define API __declspec(dllexport)
#else
	#define API
#endif

	struct Point
	{
		float x, y;
	};
	
	API int get();
	API int add(int x, int y);
	API float add_float(float x, float y);
	API void saxpy(unsigned int n, float a, const float* x, float* y);
}
