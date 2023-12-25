import numpy as np

# np array creation
a = np.array([1,2,3,4,5,6,7,8])
a[1]

b = np.zeros(8)
b
type(b[0])

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

