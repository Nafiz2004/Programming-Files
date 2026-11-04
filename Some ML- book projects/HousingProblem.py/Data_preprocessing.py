# simple imports
from pathlib import Path
import pandas as pd
import tarfile
import urllib.request
import numpy as np
import matplotlib.pyplot as plt


# load data
def load_housing_data():
    tarball_path = Path("datasets/housing.tgz")
    if not tarball_path.is_file():
        Path("datasets").mkdir(parents=True, exist_ok=True)
        url = "https://github.com/ageron/data/raw/main/housing.tgz"
        urllib.request.urlretrieve(url, tarball_path)
        with tarfile.open(tarball_path) as housing_tarball:
            housing_tarball.extractall(path="datasets")
    return pd.read_csv(Path("datasets/housing/housing.csv"))

# housing = load_housing_data()
housing = pd.read_csv("E:\Work & Files\Programming Files\Some ML- book projects\Dataset\\archive\housing.csv")

print(housing)
print(housing.head())
print(housing.info())
print(housing.describe())
housing["ocean_proximity"].value_counts()


total_nan = np.isnan(housing["total_bedrooms"])
total_nan.value_counts()

housing.hist(bins = 50,figsize=(12,8))
plt.show()



# Equivalent of train_test_split

def data_split(data, split_ratio, random_state):
    np.random.seed(random_state)
    shuffled_rows = np.random.permutation(len(data))
    test_size = int(split_ratio * len(data))

    test_set_index = shuffled_rows[:test_size]
    train_set_index = shuffled_rows[test_size:]

    return data.iloc[train_set_index], data.iloc[test_set_index]

train_set, test_set = data_split(housing, 0.2, 42)
print(train_set)
print(test_set)

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
