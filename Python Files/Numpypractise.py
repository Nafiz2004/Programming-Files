

import numpy as np
print(np.__version__)
np.show_config()

null_vector = np.zeros(10, dtype = np.int16)
print(null_vector)

size = null_vector.size * null_vector.itemsize
print(size)

help(np.add)

new_null_vector = np.zeros(10)
new_null_vector[4] = 1
print(new_null_vector)

ranged_nums = np.array(range(10,50))
ranged_nums = np.arange(10, 50)
print(ranged_nums)

ranged_nums = ranged_nums[::-1]
print(ranged_nums)

##Question 9: Create a 3x3 matrix with values ranging from 0 to 8 (★☆☆)

vals = np.arange(9).reshape(3, 3)
print(vals)

##10. Find indices of non-zero elements from [1, 2, 0, 0, 4, 0] (★☆☆)

nums = np.array([1, 2, 0, 0, 4, 0])
position = np.where(nums != 0)
print(position)

position2 = np.where(vals % 2 == 0)
print(position2)
# (0,0) -> 0 , (0,2) -> 2, (1,1) -> 4, (2,0) -> 6, (2,2) -> 8
