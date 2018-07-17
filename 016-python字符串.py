msg = "hello world"

#首字母大写
print(msg.capitalize())

#按照字符串是20个，居中显示
print(msg.center(20,'*'))

#字符串从第几个到第几个字符中，包含某字符的计数
print(msg.count('o',0,5))
print(msg.count('o',6))
print(msg.count('h',0))

#按下标取字符串中的字符
print(msg[0])
print(msg[6])

#判断一个字符串是否是以'd'结尾的
print(msg.endswith('d'))

#指定tab键或者空格键后面的空格个数
msg1 = 'a\tb'
print(msg1)
print(msg1.expandtabs(10))

#找到对应字符的索引，没有找到就直接输出-1
print(msg.find('d'))
print(msg.find('z'))
print(msg.find('d',1,11))

#格式化
print('{0},{1}'.format('name','age'))
print('{name}'.format(name = "stone"))

#索引：查看指定字符的索引
print(msg.index('w'))

#判断字符都是数字
print(msg.isalnum())  

#判断字符都是字母
print(msg.isalpha())
msg1="abcd"
print(msg1.isalpha())

#判断是否是十进制数字
msg1="10100011"
print(msg1.isdecimal())

#判断是否是整型数字
msg1="101.11"
print(msg1.isdigit())

#判断是不是数字
print(msg1.isnumeric())

print(msg.isidentifier()) 
#判断字符串内是否包含关键字;

print(msg.islower())
#判断字符串是否是小写 

print(msg.isspace()) 
#判断字符串是否是空格

print(msg.istitle()) 
#是否是标题 单词首字母必须是大写的 其他的字符不能是大写的，

print(msg.isupper())
#是否都是大写

#左对齐  
print(msg.ljust(10,'*'))

#右对齐
print(msg.rjust(20,'#'))

print(msg.lower()) 
#将所有的大写转换成小写

print(msg.upper())
#将所有的小写转换成大写

print(msg.lstrip())
#左边去除空格

print(msg.rstrip())  
#去除右边的空格

msg1 = msg.maketrans('hello','china')
print(msg1)
print(msg)
#将字符串进行替换 替换的字符串需要跟等长

#print(msg.rfill('####'))  
#从右侧填充  

#移除空白 strip()：去除空白
msg1 = "   你好！ 世界！   "
print(msg1.strip())

#分割 split()
print(msg.split(' '))

#长度 len()
print(len(msg))

#索引 msg[3]:字符索引

#切片 msg[0:3]:字符串切片 msg[2:7:2]:按步长取
print(msg[6:10])
print(msg[6:11])




