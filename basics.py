import numpy as np
a=np.array([1,2,3,4,5,2,1,0])
ab=np.array([1,2,3,4], dtype=float)
print (a)
print(a.shape, a.size)
print(ab)
print (a)
b= np.array([1.1234567899,2.5678910234,3.54567890123], dtype=np.float32)
print(b.dtype)
print (b)

c= np.array([1,0,1,0,3,4], dtype=bool)
print (c)

d=np.array(["cat","dog","elephant"])
print(d, d.dtype)


#reshape
e=a.reshape(2,4)
print (e)

#slice
f=e[1,:]
print (f)

g=[10,20,30,40,50]
h=g[3:5]
print(h)

#dot and matmul
first= np.array([1,2,3])
second= np.array([4,5,6])
print(np.dot(first,second))

farray = np.array([[1, 2],
              [3, 4]])

sarray = np.array([[5, 6],
              [7, 8]])

print(farray @ sarray)


#randomness
rng = np.random.default_rng(42)
print(rng.integers(1, 10, size=5))