 ### https://www.youtube.com/watch?v=qrMnoY8qBJM
 ### coding with sagar

import pandas as pd
import numpy as np
import os
os.chdir("E:\Work & Files\Datasets\Machine Learning A-Z (Codes and Datasets)\Part 1 - Data Preprocessing\Section 2 -------------------- Part 1 - Data Preprocessing --------------------\Python")

#### Data Read #####
dataset = pd.read_csv("Data.csv")

print(dataset)

datas = {
    "Name"  : ["Nafiz", "Nahid", "Mohon", "Mahabub", "Mehan"],
    "Age"   : [20, 5, 18, 25, 12],
    "City"  : ["Bogura", "Gopalganj", "Vhola", "China", "Chitagong"],
    "Mark"  : [78, 85, 65, 45, 90]
}

df = pd.DataFrame(datas)
print(df)

##### data save #####
df.to_csv("meow.csv", index = False)
# df.to_excel()
# df.to_dict()

##### data preview #####

dataset.head(3)
dataset.tail(3)


#### understand the data ####
dataset.info()

df.info()

dataset.describe()

df.describe()


#### shape ####
df.shape
df.columns

#### selectting ####
print(df["Name"][0])
print(df[["Name", "Age"]])


print(df[df["Age"] > 10])
print(df[df["Age"] > 10]["Name"])

df["City"][0][0]

df[(df["Age"] > 10) & (df["Mark"] > 70)]

print(df[(df["Age"] > 3) & (df["Mark"] > 70)]["Name"])

df[(df["Age"] >= 5) & (df["City"].str.lower().str[0] == "b") & (df["Mark"] > 50)]



df["City"].str.lower() #converts whole pandas series lower
df["City"].str.lower()[0] #converts whole pandas series lower and show first row
df["City"].str.lower().str[0]

condition1 = df["Age"] >= 5
condition2 = df["City"].str.lower().str[0] == "b"
condition3 = df["Mark"] > 50

df[condition1 & condition2 & condition3]["Name"][0]

## Part2

################### ADDING COLUMNS ###################

datas = {
    "Name"  : ["Nafiz", "Nahid", "Mohon", "Mahabub", "Mehan"],
    "Age"   : [20, np.nan, 18, 25, 12],
    "City"  : ["Bogura", "Gopalganj", "Vhola", "China", "Chitagong"],
    "Mark"  : [78, 85, 65, np.nan, 90]
}

df = pd.DataFrame(datas)
print(df)

#new columss
df["Salary"] = [20000, 15000, 18000, 25000, 10000]
print(df)

df["Bonus"] = df["Salary"] * 0.1
print(df)

df.insert(3, "University", ["HSTU", "BUET", "KOBOR", "RU", "RUET"])
print(df)


###################### UPDATING VALUES #################

df.loc[1, "Salary"] = 30000
print(df)

df["Bonus"] = df["Bonus"] * 1.1
print(df)

df.iloc[:, 4] = df["Mark"] + 10
print(df)

df.iloc[:, 4] = df.iloc[:, 4] - 7
print(df)


############### REMOVING VALUES #####################

# rows remove
df.drop(index = [0,2], inplace = True)
#by default it is False, keeping it False will create a copy
#line new_df = df.drop(ROWS, COLS, inplace = False) ... creates new df doesn't change actual df

print(df)

# columns remove
df.drop(columns = ["Bonus"], inplace = True) #by default it is False, keeping it False will create a copy
print(df)

#bdeleting via columns as name and rows as index

df.drop(columns = ["Salary", "Bonus"], index = [1, 4], inplace = True)
print(df)

# deleting via slicing [:2, 2:]
df.drop(index = df.index[:2], columns = df.columns[2:], inplace = True)
print(df)


# deleting via both columns and rows indexing
df.drop(index = [1, 3], columns = df.columns[[2, 4]], inplace = True)
print(df)


################################ Three methods #########################
# df.drop(index = [1, 4], columns = ["Salary", "Bonus"], inplace = True) #idex-mention
# df.drop(index = df.index[:2], columns = df.columns[2:], inplace = True) #slice-slice
# df.drop(index = [1, 3], columns = df.columns[[2, 4]], inplace = True) #index-index

## we can make more combintions for our need with these three



### handling missing data
print(df.isnull())
print(df.isnull().sum())

# 2 ways to handle
#1. Drop whole Row/Columns depending on dataset if that row/columns doen't mean much to model
#2. Fill in we some value (mean, median)

df.dropna(inplace = True) # axis = 0 -> only rows,,,,, axis = 1 -> only colums
df.dropna(inplace = True, axis = 0)

print(df)


df["Age"].fillna(df["Age"].mean(), inplace = True)
print(df)
## better use Sklearn SimpleImputer
