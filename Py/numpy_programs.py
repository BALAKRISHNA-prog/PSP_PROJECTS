#NumPy Basics: Arrays and Vectorized Computation
import numpy as np
my_arr = np.arange(10)
print(my_arr)
my_list = list(range(10))
print(my_list)
#
for array in range(10):
    my_arr2 = my_arr*2

print(my_arr2)

for lst in range(10):
    my_list2 = [x*2 for x in my_list]

print(my_list2)

#The NumPy ndarray: A Multidimensional Array Object
data = np.random.randn(2, 3)
print(data)

print(data*10)

print(data + data)
#
print(data.shape)
print(data.dtype)
#
data1 = [6, 7.5, 8, 0, 1]
arr1 = np.array(data1)
print(arr1)
#
data2 = [[1, 2, 3, 4], [5, 6, 7, 8]]
arr2 = np.array(data2)
print(arr2)
#
print(arr2.ndim)
print(arr2.shape)
print(arr1.dtype)
#
print(np.zeros(10))
print(np.zeros((3,6)))
print(np.empty((2,3,2)))
#
print(np.array(15))
#Data types for ndarrays
arr1 = np.array([1, 2, 3], dtype=np.float64)
arr2 = np.array([1, 2, 3], dtype=np.int32)
print(arr1.dtype)
print(arr2.dtype)
#
arr = np.array([1,2,3,4,5])
print(arr.dtype)
float_arr = arr.astype(np.float64)
print(float_arr.dtype)
#
arr = np.array([3.7, -1.2, -2.6, 0.5, 12.9, 10.1])
print(arr)
print(arr.astype(np.int32))
#astype to convert array of strings representing numbers to numeric form
numeric_strings = np.array(['1.25','-9.6','42'], dtype=np.string_)
print(numeric_strings.astype(float))
#
int_array = np.arange(10)
calibers = np.array([.2, .270, .357, .380, .44, .50], dtype=np.float64)
print(int_array.astype(calibers.dtype))
#
empty_uint32 = np.empty(8, dtype='u4')
print(empty_uint32)
#Arithmetic with NumPy Arrays
arr = np.array([[1., 2., 3.],[4., 5., 6.]])
print(arr)
print(arr*arr)
print(arr-arr)
print(1/arr)
print(arr**0.5)
#Comparisons between arrays of the same size yield  boolean arrays:
arr2 = np.array([[0., 4., 1.],[7., 2., 12.]])
print(arr2)
print(arr2>arr)
#Basic indexing and slicing
arr = np.arange(10)
print(arr)
print(arr[5])
print(arr[5:8])
arr[5:8] = 12
print(arr)
#slicing
arr_slice = arr[5:8]
print(arr_slice)
arr_slice[1] = 12345
print(arr)
#The "bare" slice[:] will assign to all values in array:
arr_slice[:] = 64
print(arr)
#
arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr2d[2])

print(arr2d[0][2])
print(arr2d[0, 2]
)
#
arr3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arr3d)
print(arr3d[0])
old_values = arr3d[0].copy()

arr3d[0] = 42
print(arr3d)
arr3d[0] = old_values
print(arr3d)
print(arr3d[1, 0]
)
x = arr3d[1]
print(x)
print(x[0])
#indexing with slices
print(arr)
print(arr[1:6])

print(arr2d)
print(arr2d[:2])
print(arr2d[:2, 1:])
print(arr2d[1, :2]
)
print(arr2d[:2, 2])
print(arr2d[:, :1]
)
arr2d[:2, 1:] = 0
print(arr2d)
#Boolean Indexing
names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])

data = np.random.randn(7, 4)
print(names
)
print(data)
print( names == 'Bob'
)
print( data[names == 'Bob']
)
print(data[names == 'Bob', 2:])
print(data[names == 'Bob', 3])
print(names != 'Bob')
print(data[~(names == 'Bob')]
)

cond = names == 'Bob'
print(data[~cond]
)
#
mask = (names == 'Bob') | (names == 'Will')
print(mask)
print(data[mask]
)
data[data < 0] = 0
print(data)

data[names != 'Joe'] = 7
print(data)
#Fancy Indexing
arr = np.empty((8, 4))

for i in range(8):
    arr[i] = i
print(arr)
print(arr[[4, 3, 0, 6]])
print(arr[[-3, -5, -7]])

arr = np.arange(32).reshape((8, 4))

print(arr)
print(arr[[1, 5, 7, 2], [0, 3, 1, 2]])
print(arr[[1, 5, 7, 2]][:, [0, 3, 1, 2]])
#Transposing Arrays and Swapping Axes
arr = np.arange(15).reshape((3, 5))

print(arr)
print(arr.T
)
arr = np.random.randn(6, 3)

print(arr)
print(np.dot(arr.T, arr))
arr = np.arange(16).reshape((2, 2, 4))

print(arr)
print(arr.transpose((1, 0, 2)))

print(arr)
print(
arr.swapaxes(1, 2))
# Universal Functions: Fast Element-Wise Array Functions 

arr = np.arange(10)
print(arr)
print(np.sqrt(arr))
print(np.exp(arr))
#
x = np.random.randn(8)
y = np.random.randn(8)
print(x)
print(y)
print(
np.maximum(x, y)
)

arr = np.random.randn(7) * 5
print(arr)
remainder, whole_part = np.modf(arr)

print(remainder)
print(whole_part)
print(arr)
print(np.sqrt(arr))
print(np.sqrt(arr, arr))

print(arr)

#Array-Oriented Programming with Arrays
points = np.arange(-5, 5, 0.01) # 1000 equally spaced points
xs, ys = np.meshgrid(points, points)
 
print(ys)
z = np.sqrt(xs ** 2 + ys ** 2)

print(z)
#Matplot
import matplotlib.pyplot as plt
print(plt.imshow(z, cmap=plt.cm.gray)); plt.colorbar()

print(plt.title("Image plot of $\sqrt{x^2 + y^2}$ for a grid of values"))
#Expressing Conditional Logic as Array Operations


xarr = np.array([1.1, 1.2, 1.3, 1.4, 1.5])

yarr = np.array([2.1, 2.2, 2.3, 2.4, 2.5])

cond = np.array([True, False, True, True, False])

result = [(x if c else y)
          for x, y, c in zip(xarr, yarr, cond)]
print(result)

result = np.where(cond, xarr, yarr)
print(result)

arr = np.random.randn(4, 4)
print(arr)
print(arr>0)
print(np.where(arr > 0, 2, -2))
print(np.where(arr > 0, 2, arr)) # set only positive values to 2
#Mathematical and Statistical Methods
arr = np.random.randn(5, 4)
print(arr)
print(arr.mean())
print(np.mean(arr))
print(arr.sum())


print(arr.mean(axis=1))

print(arr.sum(axis=0))
arr = np.array([0, 1, 2, 3, 4, 5, 6, 7])
print(arr.cumsum()
)
arr = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
print(arr)
print(arr.cumsum(axis=0)
)
print(arr.cumprod(axis=1)
)
#Methods for Boolean Arrays
arr = np.random.randn(100)
print((arr > 0).sum()) # Number of positive values
bools = np.array([False, False, True, False])

print(bools.any()
)
print(bools.all()
)
#Sorting
arr = np.random.randn(6)
print(arr)
print(arr.sort())
print(arr)

arr = np.random.randn(5, 3)

print(arr)
arr.sort(1)
print(arr)
large_arr = np.random.randn(1000)

large_arr.sort()

print(large_arr[int(0.05 * len(large_arr))]) # 5% quantile

#Unique and Other Set Logic
names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])
print(np.unique(names))
ints = np.array([3, 3, 3, 2, 2, 1, 1, 4, 4])
print(np.unique(ints))
print(sorted(set(names))
)
values = np.array([6, 0, 0, 3, 2, 5, 6])

print(np.in1d(values, [2, 3, 6])
)
#File Input and Output with Arrays

arr = np.arange(10)

np.save('some_array', arr)

print(np.load('some_array.npy'))
print(np.savez('array_archive.npz', a=arr, b=arr)
)
arch = np.load('array_archive.npz')

print(arch['b']
)
print(np.savez_compressed('arrays_compressed.npz', a=arr, b=arr))

# Linear Algebra
x = np.array([[1., 2., 3.], [4., 5., 6.]])
y = np.array([[6., 23.], [-1, 7], [8, 9]])

print(x)
print(y)
print(x.dot(y))#x.dot(y) is equivalent to np.dot(x, y)
print(np.dot(x, y))
print(np.dot(x, np.ones(3)))
#The @ symbol (as of Python 3.5) also works as an infix operator that performs
#matrix multiplication:
print( x @ np.ones(3))
#
from numpy.linalg import inv, qr

X = np.random.randn(5, 5)

mat = X.T.dot(X)
print(inv(mat))
print(mat.dot(inv(mat))
)

q, r = qr(mat)

print(r)
# Pseudorandom Number Generation
samples = np.random.normal(size=(4, 4))
print(samples)
#Python’s built-in random module, by contrast, only samples one value at a time.
#As you can see from this benchmark, numpy.random is well over an order of
#magnitude faster for generating very large samples
import numpy as np
from random import normalvariate
import matplotlib.pyplot as plt
plt.imshow(z, cmap=plt.cm.gray)
plt.colorbar()
plt.title("Image plot of $\sqrt{x^2 + y^2}$ for a grid of values")
plt.show()
N = 1000000
np.random.seed(1234)
rng = np.random.RandomState(1234)

print(rng.randn(10)
)
# Example: Random Walks
import random
position = 0
walk = [position]
steps = 1000
for i in range(steps):
    step = 1 if random.randint(0, 1) else -1
    position += step
    walk.append(position)

print(plt.plot(walk[:100]))
plt.show()
#
nsteps = 1000
draws = np.random.randint(0, 2, size=nsteps)
steps = np.where(draws > 0, 1, -1)
walk = steps.cumsum()

print(walk.min())
print(walk.max())
print((np.abs(walk) >= 10).argmax())

#Simulating Many Random Walks at Once

nwalks = 5000
nsteps = 1000
draws = np.random.randint(0, 2, size=(nwalks, nsteps)) # 0 or 1
steps = np.where(draws > 0, 1, -1)
walks = steps.cumsum(1)
print(walks)
print(walks.max())
print(walks.min())
hits30 = (np.abs(walks) >= 30).any(1)
print(hits30)
print( hits30.sum()) # Number that hit 30 or -30
crossing_times = (np.abs(walks[hits30]) >= 30).argmax(1)
print(crossing_times.mean())



























































