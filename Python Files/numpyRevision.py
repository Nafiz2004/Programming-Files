
#>>>>>>>>> Course: Numpy For Machine Learning by John Elder

############################# lec 1 ###########################

import numpy as np

nums = np.array([1, 34, 5])
print(nums)
print(nums.shape) #n-D length
print(len(nums)) #1-D length

nums2 = np.array(range(1, 10, 2))
nums3 = np.arange(1, 10, 2)
nums4 = np.zeros((2, 5))
nums5 = np.full((2, 3), 5)

print(nums2)
print(nums3)
print(nums4)
print(nums5)

########################### Lec-2 #########################

values = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0, -1])
values2 = np.array([[1,2,3], [2,4,6]])

print(values[1:3])
print(values2[1][0:2]) # gets 2,4

print(values2[0:1, 0:2]) # first 0:1 means [1,2,3] and last 0:2 means 1,2
print(values2[:, 0:2]) # very powerful

print(values[1:7:2]) # "2" is step like in range
print(values[::2]) # everything in step 2

########################## Lec-3 #########################

# np.absolute() -> abs()
# np.exp() -> power()
# np.min()
# np.max()
# np.sort()
#.......................

############################ lec-4 #######################

# view

np1 = np.array([0,1,2,3,4])
np2 = np1
np3 = np1.view()
np4 = np1.copy()

print(np1)
print(np2)
print(np3)
print(np4)

np1[0] = -123

print(np1)
print(np2)
print(np3)
print(np4)

np3.shape = (5, 1)

print(np1)
print(np2)
print(np3)
print(np4)

# = → same array, same data
# .view() → new array, same data
# .copy() → just copy

#some experiment
np2[1] = 55
print(np1, np2)
np3[2] = 66
print(f"{np1}\n{np2}\n{np3}")

######################## Lec - 5 #########################

vals = np.array([[1,2,3], [2,4,6]])
print(vals.shape)
print(vals.shape[0])

#reshaping
vals2 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0, -1])
vals3 = vals2.reshape(6,2) #reshape() can work -> n-D array to n-D array
print(vals3)
print(vals3.shape)

vals4 = vals2.reshape(2, 2, 3)
print(vals4)

vals5 = vals4.reshape(-1) # to make 1-D
print(vals5)

vals6 = vals5.reshape(2, -1) # "-1" figures out itself
vals7 = vals5.reshape(-1, 2, 3)
print(vals6)
print(vals7) # vals7 is underdefined

print(vals6.shape)
print(vals7.shape)


###################### Lec - 6 ##################################

num1 = np.array([
    [[1, 2, 3],[4, 5, 6]],
    [[66, 77, 0], [99, 11, 0]]
    ])

print(num1)

for x in np.nditer(num1):
    print(x)


########################### Lec-7 ###############################

# np.sort() -> returns copy, Can sort n-D arrays too
arr = np.array([5, 3, 6, 3, 0, 2, -1, 3])
arr = np.sort(arr)

arr2 = np.array(["Nafiz", "Arobi", "Mustakim"])
arr2 = np.sort(arr2)

arr3 = np.array([True, False, False, True])
arr3 = np.sort(arr3)

print(arr)
print(arr2)
print(arr3)


########################## Lec-8 ##############################

values = np.array([3, -2, 5, 8, 3, 0, 5, 8, 0, 4])

x = np.where( values == 3)
print(x)
print(x[0])

y = np.where( values % 2 == 0)
print(y[0])


###################### Lec-9 #############################

nums = np.array([4, -3, 7, 6, 8, 9, 2])
filtered_nums = (nums % 2 == 0)

print(nums)
print(filtered_nums)
print(nums[filtered_nums])






#####@@@@@@@@@ course: https://www.youtube.com/watch?v=9DhZ-JCWvDw&t=1850s

#### Numpy basics

nums = np.array([1, 5, 4, 3, 7, 9, 2])
print(nums.shape)
print(nums.size)
print(nums.ndim)
print(nums.dtype)

# change datatype
float_nums = nums.astype(float)
print(float_nums)

print(nums + 5)
print(nums ** 2)
print(nums % 2 == 0)
print(nums[nums % 2 == 0])


### Indexing, slicing

nums = np.array([1, 5, 4, 3, 7, 9, 2])
nums = nums[::-1] #reverse

print(nums)
print(nums[[0, -1 ]])

vals = nums > 4
print(nums[vals])
# same stuff
print(nums[nums > 4])


## reshaping .ravel(), .flaten(), .reshape(-1) >>> same
## .reshape(-1), .ravel() returns view()
## .flaten() returns copy()

### add data
nums = np.append(nums, [20, 30, 40])
print(nums)

### concatinate, vstack, hstack ###
# Function      ----	Direction  ----	Equivalent here
# vstack()      ----	Vertical   ----	concatenate(axis=0)
# hstack()      ----	Horizontal ----	concatenate(axis=1)
# concatenate()	----    You choose ----	axis=0 or axis=1


a = np.array([[1, 2],
              [3, 4]])

b = np.array([[5, 6],
              [7, 8]])

print(np.concatenate((a, b), axis = 0))
print(np.vstack((a, b)))

print(np.concatenate((a ,b), axis = 1))
print(np.hstack((a, b)))


## deleting array eliment

nums = np.array([1, 3, 6, 2, 7, 9, 8, 3])
np.delete(nums, 0) #insead of just deleting it will return

# spliting

x, y = np.split(nums, 2)
print(x)
print(y)

## np.hsplit(), np.vsplit()

# broadcasting
nums = np.array([1, 3, 6, 2, 7, 9, 8, 3])
prices = nums - (nums * 10) / 100

print(prices)

a = np.array([[1, 2],
              [3, 4]])
p = np.array([5, 5])

res = a + p
print(res)

#vectorization

arr = np.array([1, 3, np.nan, 5, np.inf, -np.inf])
print(np.isnan(arr))

print(arr)

cleaned_arr = np.nan_to_num(arr, nan = 1, posinf = 100, neginf = -100)
print(cleaned_arr)

import numpy as np

valss = np.array(["Hi", "A", "Name"])

print(valss)
