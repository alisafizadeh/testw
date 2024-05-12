import numpy as np

array=np.zeros(10)
array

array=np.ones(10)
array


array=np.ones(10)
array*5

array=np.arange(10,51,dtype=int)
array


array=np.arange(10,51,2)
array

array=np.arange(0,9)
array.reshape(3,3)



array=np.eye(3,3)
array


array=np.random.rand()
array


array=np.random.rand(25)
array


array=np.arange(0.01,1.01,0.01)



array=np.linspace(0,1,20)
array

########################



mat=np.arange(1,26).reshape(5,5)
mat


mat[2:,1:]



mat[3,4]


mat[:3,1].reshape(3,1)


mat[4]


mat[3:]


mat.sum()

mat.std()

mat.sum(axis=0)



