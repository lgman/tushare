import pandas as pd
import numpy as np

#1.apply()
#当想让方程作用在一维的向量上时，可以使用apply来完成，如下所示
frame = pd.DataFrame(np.random.randn(4, 3), columns=list('bde'), index=['Utah', 'Ohio', 'Texas', 'Oregon'])
print(frame)

f = lambda x: x.max() - x.min()
frame1 = frame.apply(f)
print(frame1)

#2.applymap()
#如果想让方程作用于DataFrame中的每一个元素，可以使用applymap().用法如下所示
format1 = lambda x: '%.2f' % x      #保留2位小数
frame2 = frame.applymap(format1)
print(frame2)

#3.map()
#map()只要是作用将函数作用于一个Series的每一个元素，用法如下所示
format2 = lambda x: '%.3f' % x      #保留2位小数
seriesA = frame['e'].map(format2)
print(seriesA)

#总的来说就是apply()是一种让函数作用于列或者行操作，
#applymap()是一种让函数作用于DataFrame每一个元素的操作，
#而map是一种让函数作用于Series每一个元素的操作
