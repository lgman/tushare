#例子1
import pandas as pd
import numpy as np

dates = pd.date_range('1/1/2000', periods=8)
df = pd.DataFrame(np.random.randn(8, 4), index=dates, columns=['A', 'B', 'C', 'D'])
print(df)
df[['B', 'A']] = df[['A', 'B']]  #两个单元格数据调换
print(df)

'''
s = df['A']
print(s)
print(s[dates[5]])

panel = pd.Panel({'one' : df, 'two' : df - df.mean()})
print(panel['two'])

print(panel['one'])
'''
