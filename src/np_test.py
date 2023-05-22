#Was trying to figure out how to stack hive output since I don't know
#much numpy

import numpy as np 

array = np.array([
    [0, 1], 
    [0, 1], 
    [0, 1], 
    [0, 1], 
    [0, 1], 
    ])

array2 = np.array([
    [1, 0], 
    [1, 0], 
    [1, 0], 
    [1, 0], 
    [1, 0], 
    ])

print(array.shape)
print(array[:, 1])

print(np.column_stack((array[:, 1], array2[:, 0], array[:, 0])))