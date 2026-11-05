# simple imports
from pathlib import Path
import pandas as pd
import tarfile
import urllib.request
import numpy as np
import matplotlib.pyplot as plt


# load data
# def load_housing_data():
#     tarball_path = Path("datasets/housing.tgz")
#     if not tarball_path.is_file():
#         Path("datasets").mkdir(parents=True, exist_ok=True)
#         url = "https://github.com/ageron/data/raw/main/housing.tgz"
#         urllib.request.urlretrieve(url, tarball_path)
#         with tarfile.open(tarball_path) as housing_tarball:
#             housing_tarball.extractall(path="datasets")
#     return pd.read_csv(Path("datasets/housing/housing.csv"))

# housing = load_housing_data()
housing = pd.read_csv("E:\Work & Files\Programming Files\Some ML- book projects\Dataset\\archive\housing.csv")

# print(housing)
# print(housing.head())
# print(housing.info())
# print(housing.describe())
# housing["ocean_proximity"].value_counts()
#
#
# total_nan = np.isnan(housing["total_bedrooms"])
# total_nan.value_counts()
#
# housing.hist(bins = 50,figsize=(12,8))
# plt.show()



##########Equivalent of train_test_split NORMAL SPLITTING ###############

def data_split(data, split_ratio, random_state):
    np.random.seed(random_state)
    shuffled_rows = np.random.permutation(len(data))
    test_size = int(split_ratio * len(data))

    test_set_index = shuffled_rows[:test_size]
    train_set_index = shuffled_rows[test_size:]

    return data.iloc[train_set_index], data.iloc[test_set_index]

train_set, test_set = data_split(housing, 0.2, 42)

# shuffled_rows = np.random.permutation(len(housing))
# print(shuffled_rows)
# test_size = int(.2 * len(housing))
#
# print(test_size)
#
# test_set = shuffled_rows[:test_size]
# train_set = shuffled_rows[test_size:]
#
# print(test_set)
# print(train_set)
#
# housing.iloc[train_set].values
# housing.iloc[test_set].values


#####################stratified splitting###################

housing["income_cat"] = pd.cut(housing["median_income"],
                        bins = [0., 1.5, 3.0, 4.5, 6., np.inf],
                        labels = [1, 2, 3, 4, 5])


housing["income_cat"].value_counts(normalize = True)

from sklearn.model_selection import train_test_split
train_set, test_set = train_test_split(housing,
                                        test_size = 0.2,
                                        stratify = housing["income_cat"],
                                        random_state = 42)

train_set["income_cat"].value_counts(normalize = True)
test_set["income_cat"].value_counts(normalize = True)

housing["income_cat"].value_counts().sort_index().plot.bar(rot=0, grid=True)
plt.xlabel("Income category")
plt.ylabel("Number of districts")
plt.show()

#since no use we drop the column
# for _ in (train_set, test_set):
#     _.drop("income_cat", axis = 1, inplace = True)

train_set.drop("income_cat", axis = 1, inplace = True)
test_set.drop("income_cat", axis = 1, inplace = True)
