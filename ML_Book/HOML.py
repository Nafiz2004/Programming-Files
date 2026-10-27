
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Download and prepare the data
lifesat = pd.read_csv("https://github.com/ageron/data/raw/main/lifesat/lifesat.csv")
print(lifesat)

X = lifesat[["GDP per capita (USD)"]].values
y = lifesat[["Life satisfaction"]].values
print(X)
print(y)

# Visualize the data
lifesat.plot(kind='scatter', grid=True, x="GDP per capita (USD)", y="Life satisfaction")
plt.axis([23_500, 62_500, 4, 9])
plt.show()

# Select a linear model
# from sklearn.linear_model import LinearRegression
# model = LinearRegression()
# model.fit(X, y)

from sklearn.neighbors import KNeighborsRegressor
model = KNeighborsRegressor(n_neighbors=3)
model.fit(X, y)

# Make a prediction for Cyprus
X_new = [[37_655.2]]  # Cyprus' GDP per capita in 2020
print(model.predict(X_new)) # output: [[6.30165767]]

#nothing
