#例子1:多个list组成dict
key = ['a','b','c','d']
value = [1,2,3,4]
mydict = dict(zip(key,value))
print(mydict)

#例子2:可以用zip同时遍历多个列表，生成一个多维列表
other = [5,6,7,8]
mylist = list(zip(key,value,other))
print(mylist)

#例子3: 多个list组成字典
date=['2017-01','2017-02','2017-03','2017-04']
c7_list=[1,2,3,4]    
c8_list=['a','b','c','d']
c9_list=['x','y','z','w']
new_list=[]
mid=map(list,zip(date,c7_list,c8_list,c9_list))
for item in mid:
    new_dict=dict(zip(['date','c7','c8','c9'],item))
    new_list.append(new_dict)
print(new_list)

#列表的合并与拆分
x=[1,2,3]
y=[4,5,6]
z=zip(x,y)
print(z)   # [(1, 4), (2, 5), (3, 6)]

a,b=zip(*z)
print(a)   # (1, 2, 3)
print(b)   # (4, 5, 6)

# 通过列表和字典模拟数据的行列转换
a=[
['a',1],
['a',2],
['a',3],
['b',1],
['b',2],
['c',3]]

print a
dict={}
for item in a:
    dict[item[0]]=[]
    
for item in a:
    dict[item[0]].append(item[1])
    
print(dict)

#输出：{'a': [1, 2, 3], 'c': [3], 'b': [1, 2]}
