def f(x):
    return x*x
mylist = []
mylist = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])

for item in mylist:
    print(item)

l2=map(lambda x,y:x**y,[1,2,3],[1,2,3])
for i  in l2:
    print(i)

l3=map(lambda x,y:(x**y,x+y),[1,2,3],[1,2,3])
for i in l3:
    print(i)


print(map(None, [2,4,6],[3,2,1]))

def format_name(s):
    s1=s[0:1].upper()+s[1:].lower();
    return s1;
print(map(format_name, ['adam', 'LISA', 'barT']))

