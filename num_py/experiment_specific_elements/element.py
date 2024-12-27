import numpy as np

#get a specific element
a = np.array([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],[21, 22, 23, 24, 25, 26, 27, 28, 29, 30]])
print(a[1,1])
print(a[0,1])

#get a specific row
print(a[0,:])

#get a specific column  
print(a[:,1])


print(a[0, 1:-1:2])