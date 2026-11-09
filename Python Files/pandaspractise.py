#### resource https://github.com/ajcr/100-pandas-puzzles/blob/master/100-pandas-puzzles.ipynb

import pandas as pd
print(pd.__version__)

##3. Print out all the version information of the libraries that are required by the pandas library.
pd.show_versions()


## 4. Create a DataFrame df from this dictionary data which has the index labels.
import numpy as np
import pandas as pd
data = {'animal': ['cat', 'cat', 'snake', 'dog', 'dog', 'cat', 'snake', 'cat', 'dog', 'dog'],
        'age': [2.5, 3, 0.5, np.nan, 5, 2, 4.5, np.nan, 7, 3],
        'visits': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'priority': ['yes', 'yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no', 'no']}

labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

df = pd.DataFrame(data)
print(df)

df.info()
df.head(5)
df.describe()


######################
df['animal'][[3,4,8]]
df["age"][[3,4,8]]
