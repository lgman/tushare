from bs4 import BeautifulSoup
import urllib.request

url = 'http://www.nmc.cn'
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html,'lxml')
content = soup.select('#alarmtip > ul > li.waring > a')

######### 添加到列表中
link = []
title = []
tag = []
for n in content:
    link.append(url+n.get('href'))
    title.append(n.get('title'))
    tag.append(n.text)

######## 添加到字典中
for n in content:
    data = {
        'tag'   : n.text,
        'link'  : url+n.get('href'),
        'title' : n.get('title')
    }

######## 添加到字典中
data1 = {}
for n in content:
    data1[n.text] = (url+n.get('href'),n.get('title'))
    

######## 添加到字典中
i = 0
data2 = {}
for n in content:
    i += 1
    data = {
        'tag'   : n.text,
        'link'  : url+n.get('href'),
        'title' : n.get('title')
    }
    data2[i]=data
    
print(content)

print(link)
print(title)
print(tag)

print(data)

print(data1)

print(data2)
