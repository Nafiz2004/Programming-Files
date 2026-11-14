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
 ## normalize = True means will show in percentage
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


### page 60+

housing.plot(kind="scatter", x="longitude", y="latitude", alpha = 0.3, grid=True)
plt.show()

housing.plot(kind="scatter", x="longitude", y="latitude", grid=True,
            s = housing["population"]/100, label = "population", c = "median_house_value",
            cmap = "jet", colorbar = True, legend = True, sharex = False, figsize = (10, 7))
plt.show()

corr_matrix = housing.corr(numeric_only = True)
corr_matrix["median_house_value"].sort_values(ascending = False)


from pandas.plotting import scatter_matrix

attributes = ["median_house_value", "median_income", "total_rooms", "housing_median_age"]
scatter_matrix(housing[attributes], figsize=(12,8))
plt.show()

housing.plot(kind="scatter", x="median_income", y="median_house_value",
alpha=0.1, grid=True)
plt.show()


housing["rooms_per_house"] = housing["total_rooms"] / housing["households"]
housing["bedrooms_ratio"] = housing["total_bedrooms"] / housing["total_rooms"]
housing["people_per_house"] = housing["population"] / housing["households"]


corr_matrix = housing.corr(numeric_only = True)
corr_matrix["median_house_value"].sort_values(ascending = False)


######### page 67+

print(housing["total_bedrooms"])

total_nan = np.isnan(housing["total_bedrooms"]).value_counts()
print(total_nan)

# housing["total_bedrooms"].isnull().sum()
# housing["total_bedrooms"].isnull().value_counts()


from sklearn.impute import SimpleImputer
imputer = SimpleImputer(strategy = "mean")
housing_num = housing.select_dtypes(include=[np.number]) ## selects only numbers

X = imputer.fit_transform(housing_num)

imputer.statistics_
imputer.strategy

## gives back pandas dataset
housing_tr = pd.DataFrame(
    X,
    columns=housing_num.columns,
    index=housing_num.index
)
## we can set sklearn.set_config(transform_output = "pandas")

housing_cat = housing[["ocean_proximity"]]
from sklearn.preprocessing import OrdinalEncoder

encoder = OrdinalEncoder()
X_encoded = encoder.fit_transform(housing_cat)
print(X_encoded)
### assigns 0,1,2,3 ordially ... good for clearn distinction like good, bad, very bad, excellent


from sklearn.preprocessing import OneHotEncoder

encoder = OneHotEncoder(sparse_output=False)
X_encoded = encoder.fit_transform(housing_cat)
print(X_encoded)
## handle_unknows = "ignore" very powerful
## sparse_output = True return numpy which is good but
## A sparse matrix stores mainly nonzero values and their positions,
## saving memory and potentially speeding up computations.

X_dense = X_encoded.toarray() ## same as spar = True
encoder.feature_names_in_
encoder.get_feature_names_out()

###### page 75+

for sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler(feature_range = (0, 1)) #(-1,1) also good
X_scaled = scaler.fit_transform(X)

# clip = True -> helps with outliers


from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)


#### better way to use scaling, training without inverse transform
from sklearn.compose import TransformedTargetRegressor
model = TransformedTargetRegressor(LinearRegression(), transformer = StandardScaler)
model.fit(x,y)
## used LinearRegression(), StandardScaler(), inverse_transform() at the same time
y_pred = model.predict(x_)


log_pop = np.log(housing[["population"]])
print(log_pop)
### to make it sklearn compatible .....

from sklearn.preprocessing import FunctionTransformer
log_transformer = FunctionTransformer(np.log, inverse_func = np.exp)
log_pop = log_transformer.transform(housing["population"])
print(log_pop)


from sklearn.preprocessing import FunctionTransformer
from sklearn.metrics.pairwise import rbf_kernel

rbf_transformer = FunctionTransformer(rbf_kernel,
                                    kw_args = dict(Y = [[35.]],gamma = 0.1))


age_similitarity = rbf_transformer.transform(housing[["housing_median_age"]])
print(age_similitarity)
