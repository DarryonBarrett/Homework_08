import random
import pandas as pd

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

categories = data['whoAmI'].unique()

one_hot_encoded = pd.DataFrame(0, columns=categories, index=data.index)

for i, category in enumerate(data['whoAmI']):
    one_hot_encoded.loc[i, category] = 1

data = pd.concat([data, one_hot_encoded], axis=1)

data.drop(columns=['whoAmI'], inplace=True)

data.head()
# print(data)