seasons = ['spring','summer','fall','winter']
print(list(enumerate(seasons)))
print(list(enumerate(seasons,start=1)))
print(list(enumerate(seasons,start=3)))

for i,element in enumerate(seasons):
    print(i,element)

list1=[1,2,3,4,5,6]
list2=list1[::-1]
list3=[i**i for i in list1 if not i%2]

print(list1,list2,list3)
