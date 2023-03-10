import numpy as np

array = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
print(array.shape)

array2= array.reshape(3,5)
print(array2)
# Dimension
print(array2.ndim)
# type
print(array2.dtype.name)
# size
print(array2.size)

array3 = np.zeros((3,4))
print(array3)

array4 = np.ones((3,4))
print(array4)

print(np.empty((3,4)))

print(np.arange(10,50,5))

print(np.linspace(0,10,20))

a = np.array([1,2,3])
b = np.array([1,2,3])

print(a+b)
print(a*b)
print(a**2)

c = a.copy()
print(c)

print(array[0:4])

print(array[::-1])


print(array2[0:,1])
print(array2[0,:1])
print(array2[1,1:4])
print(array2[-1,:])
print(array2[:,-1])

print(array2.ravel())
print(array2.T)