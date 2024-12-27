import numpy as np

a = np.array([1, 2, 3], dtype=np.int16)
print(a)

b = np.array([[1, 2, 3], [4, 5, 6]], dtype=np.int32)
print(b)

#get dimensions
print(a.ndim)
print(b.ndim)

#get shape
print(a.shape)
print(b.shape)

#get type
print(a.dtype)
print(b.dtype)

#get size
print(a.itemsize)
print(b.itemsize)

#get total size
print("a total size",a.size * a.itemsize)
print("b total size",b.size * b.nbytes)
