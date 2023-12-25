import numpy as np

# np array creation
a = np.array([1,2,3,4,5,6,7,8])
a[1]

b = np.zeros(8)
b

c = np.ones(8)
c

d = np.empty(8)
d

e = np.arange(8)
e

f = np.linspace(0, 100, num=5)
f

g = np.array([1,2,3], dtype=np.int64)
type(g[0])


# adding, removing, sorting

# sort
arr = np.array([2, 1, 5, 6, 8, 3, 4, 7])
arr = np.sort(arr)
arr

# argsort
arr = np.array([[2, 1], [5, 4]])
ind = np.argsort(arr, axis=0)
ind
arr = np.take_along_axis(arr, ind, axis=0)
arr

# partition
a = np.array([7, 1, 7, 7, 1, 5, 7, 2, 3, 2, 6, 2, 3, 0])
p = np.partition(a, 4)
p

# concatenate
a = np.array([1, 2, 3, 4])
b = np.array([5, 6, 7, 8])
c = np.concatenate((a, b))
c

# dimension, size, shape
arr = np.array([[[0, 1, 2, 3],
                [4, 5, 6, 7]],

                [[0, 1, 2, 3],
                [4, 5, 6, 7]],

                [[0 ,1 ,2, 3],
                [4, 5, 6, 7]]])

arr.ndim
arr.size
arr.shape

# reshape
arr = np.arange(6) 
arr = arr.reshape(3,2) # new shape must have same size as original array
arr

a = np.array([1, 2, 3, 4, 5, 6])
a.shape
a

a2 = a[np.newaxis, :]
a2.shape
a2

b = np.expand_dims(a, axis=0)
b.shape
b

b2 = np.expand_dims(a, axis=1)
b2
b2.shape

# indexing and slicing
a = np.array([1,2,3])
a[0:2]
a[1]
a[1:]
a[:1]

# conditional indexing
a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
a[a < 6]
a[a >= 5]
a[a % 2 == 0]
a[(a>2) & (a<9)]

# basic operations
data = np.array([2, 4])
ones = np.ones(2, dtype=int )
data + ones
data - ones
data * ones
data / ones

a = np.array([1,2,3,4])
a.sum()

b = np.array([[1,2], [3,4]])
b.sum(axis=0)
b.sum(axis=1)

# broadcasting
data = np.array([1.2, 1.5])
data * 2

data.max()
data.min()
data.sum()

data = np.array([[1,2,3], 
                [4,5,6], 
                [7,8,9]])
data.max()
data.max(axis=0)
data.max(axis=1)

# indexing matrices
data[1]
data[1:]
data[:1]
data[0,2]
data[1:, 1:]

# random matrix generation
a = np.random.random((3,4))
a

rng = np.random.default_rng()
rng.integers(100, size=(2, 4)) 

# find distinct members
a = np.array([11, 11, 12, 13, 14, 15, 16, 17, 12, 13, 11, 14, 18, 19, 20])
np.unique(a)

# find distinct members and their indices
unique_values, indices_list = np.unique(a, return_index=True)
indices_list

# find distinct members and count
unique_values, count = np.unique(a, return_counts=True)
count


# reshaping matrices
data = np.array([1,2,3,4,5,6])
data.reshape((3,2))
data.reshape((2,3))
data.reshape((3,3)) # errors since size of data does not fit shape

# transpose
data = np.array([[1,2,3], [4,5,6]])
data.transpose()
data.T




