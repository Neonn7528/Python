"""Задание 44
В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего из 1 столбца. 
Ваша задача перевести его в one hot вид. 
Сможете ли вы это сделать без get_dummies?
import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI'lst})
data.head()"""
import pandas as pd
import random

lst = ['robot'] * 10
lst += ['human'] * 10

random.shuffle(lst)

data = pd.DataFrame({'whoAmI': lst})

unique_vals = data['whoAmI'].unique()
for val in unique_vals:
    col_name = f'whoAmI_{val}'
    data[col_name] = 0
    data.loc[data['whoAmI'] == val, col_name] = 1

data.drop('whoAmI', axis=1, inplace=True)

data.head()