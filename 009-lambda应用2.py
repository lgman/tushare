'''
#例子1
import pandas as pd
 
list = [98,88,37,68,86,33]
 
df = pd.DataFrame(list, columns=['score']) # convert list to dataframe
 
df['level'] = '' # add a column
 
def judgeLevel(df):
    for i in range(len(df)):
        if df.score.ix[i] < 60:
            df.level.ix[i] = 'C'
        elif df.score.ix[i] > 90:
            df.level.ix[i] = 'A'
        else:
            df.level.ix[i] = 'B'
    return df
 
df = judgeLevel(df)

print(df)
'''

import pandas as pd
 
list = [98,88,37,68,86,33]
 
df = pd.DataFrame(list, columns=['score'])
 
df['level'] = '' # add a column
 
def judgeLevel(df):
    if df['score'] < 60:
        return 'C'
    elif df['score'] > 90:
        return 'A'
    else:
        return 'B'
 
df['level'] = df.apply(lambda r: judgeLevel(r), axis=1)
print(df)
