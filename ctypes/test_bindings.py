import ctypes

# Load up the dll.  On Windows the .dll is automatically appended.
lib = ctypes.cdll.LoadLibrary("build/libhowtoctypes.dylib")

# You can access exported functions as attributes of the dll object and
# call them like a Python callable.
print(lib.get())

# All the primitve C data types are here.
# They can be created like so with different bit widths
i_8 = ctypes.c_int8(10)
i_16 = ctypes.c_int16(10)
i_32 = ctypes.c_int32(10) # or ctypes.c_int(10)
i_64 = ctypes.c_int64(10)

# Unsigned types
u_8 = ctypes.c_uint8(4)
u_16 = ctypes.c_uint16(4)
u_32 = ctypes.c_uint32(4)
u_64 = ctypes.c_uint64(4)

f = ctypes.c_float(10.5)

# The argtypes attribute on the function object is an array of ctypes
# https://docs.python.org/3/library/ctypes.html#ctypes._FuncPtr.argtypes
lib.add.argtypes = [ctypes.c_int, ctypes.c_int]

# Calling the function is straightforward.  Create two ints and pass them 
# in.  Because we specified the argtypes Python will protect against
# incompatible arguments.
lib.add(ctypes.c_int(4), ctypes.c_int(15))

# The above call is verbose so we can just pass in Python ints
results = lib.add(4, 15)

# Results in ArgumentError("argument1: wrong type")
# result = lib.add(4.0, 15)

# Specify the argtypes like before
lib.add_float.argtypes = [ctypes.c_float, ctypes.c_float]

# Now specify the single return type using the restype attribute.
# https://docs.python.org/3/library/ctypes.html#ctypes._FuncPtr.restype
lib.add_float.restype = ctypes.c_float

print(lib.add_float(2.25, 0.75))

print(lib.add_float(2, 0.75))

saxpy = lib.saxpy
# ctypes.POINTER() is used to declare a pointer to the type passed in.
saxpy.argtypes = [ctypes.c_uint, ctypes.c_float, ctypes.POINTER(ctypes.c_float), ctypes.POINTER(ctypes.c_float)]

# Use Python's None for void
saxpy.restype = None

n = 5
a = ctypes.c_float(2.0)

# Create the array type
FloatArrayType = ctypes.c_float * n

# Create our arrays with the new type.
x = FloatArrayType(1.0, 1.0, 1.0, 1.0, 1.0)
y = FloatArrayType(2.0, 2.0, 2.0, 2.0, 2.0)

saxpy(n, a, x, y)
for i in y: print(i, end=" ")

class Point(ctypes.Structure):
  _fields = [("x", ctypes.c_float),
             ("y", ctypes.c_float)]
p = Point(x=5.0, y=50.0)
print(p.x, p.y)