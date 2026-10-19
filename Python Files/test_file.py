

import numpy as np

np.array([5, 6, 9, 10, 4])
np.array(range(1, 11, 2))
np.arange(1, 11, 2)
np.full((2, 3), "A")
np.zeros((2, 5))

values = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0, -1])
values2 = np.array([[1,2,3], [2,4,6]])

values[1:3]
values2[1][0:2]
values2[:, 0:2]
values[1:7:2]
values2[::2]

np.absolute(values)


np1 = np.array([0,1,2,3,4])
np2 = np1.view()
np3 = np1.copy()
print(np1, np2)

np1[2] = 234
np2[1] = 123
np3[3] = 111



np1.shape = (5, 1)
print(np1, np2)

vals = np.array([[1,2,3], [2,4,6]])
print(vals.shape)
print(vals.shape[0])

vals2 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0, -1])
vals3 = vals2.reshape(6,2) #reshape() can work -> n-D array to n-D array

vals3
vals2.reshape(3, -1)

vals3.reshape(-1)

vals2.reshape(2, -1, 3)




num1 = np.array([
    [[1, 2, 3],[4, 5, 6]],
    [[66, 77, 0], [99, 11, 0]]
    ])

for i in vals2:
    print(i)


for j in np.nditer(num1):
    print(j)

arr3 = np.array([True, False, False, True])
arr3 = np.sort(arr3)
print(arr3)

values = np.array([3, -2, 5, 8, 3, 0, 5, 8, 0, 4])
x = np.where(values %  3 == 0)

print(x)

nums = np.array([4, -3, 7, 6, 8, 9, 2])
fil_nums = nums[(nums % 2 == 0)]
print(fil_nums)


nums = np.array([1, 5, 4, 3, 7, 9, 2])
nums = nums[::-1]
print(nums)

nums[[0, -2]]

a = np.array([[1, 2],
              [3, 4]])

b = np.array([[5, 6],
              [7, 8]])

np.concatenate((a, b), axis = 0)
np.vstack((a, b))

np.concatenate((a ,b), axis = 1)
np.hstack((a, b))



nums = np.array([1, 3, 6, 2, 7, 9, 8, 3,5])
np.delete(nums, 0)

x, y = np.split(nums, 2)
print(x)
print(y)


nums = np.array([1, 3, 6, 2, 7, 9, 8, 3])
prices = nums - (nums * 10) / 100

arr = np.array([1, 3, np.inf, -np.inf, np.nan])
print(np.isnan(arr))


cleaned_arr = np.nan_to_num(arr, nan = 1, posinf = 100, neginf = -100)
print(cleaned_arr)


import pandas as pd

datas = {
    "Name"  : ["Nafiz", "Nahid", "Mohon", "Mahabub", "Mehan"],
    "Age"   : [20, 5, 18, 25, 12],
    "City"  : ["Bogura", "Gopalganj", "Vhola", "China", "Chitagong"],
    "Mark"  : [78, 85, 65, 45, 90]
}


df = {
    "Name"    : ["Nafiz", "Nahid", "Mahabub"],
    "Address" : ["Bogura-Sadar", "Namuza", "Namajgor"],
}



dataset = pd.DataFrame(datas)
dataset2 = pd.DataFrame(df)
dataset
dataset2


dataset.head(3)
dataset.tail(3)


dataset.info()
dataset.describe()

dataset.shape
dataset.columns

abc = dataset[["Name", "Age"]]
print(abc)


dataset[(dataset["Age"] > 15)]["Name"]

dataset[(dataset["Age"] >= 18) & (dataset["Mark"] > 75)]["Name"][0][0].lower()

dataset["City"].str.lower().str[0] #converts whole pandas series lower

dataset[(dataset["Age"] > 5) & (dataset["City"].str.lower().str[0] == "b") & (dataset["Mark"] > 50)]["Name"][0]
