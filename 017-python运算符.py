a,b=10,20
print('a={},b={},a+b={}'.format(a,b,a+b))
print('a={},b={},a-b={}'.format(a,b,a-b))
print('a={},b={},a*b={}'.format(a,b,a*b))
print('a={},b={},a/b={}'.format(a,b,a/b))
print('a={},b={},a%b={}'.format(a,b,a%b))
print('a={},b={},a**b={}'.format(a,b,a**b))
print('a={},b={},a//b={}'.format(a,b,a//b))

print("{}=={}是{}".format(a,b,a==b))
print("{}!={}是{}".format(a,b,a!=b))
print("{}>{}是{}".format(a,b,a>b))
print("{}<{}是{}".format(a,b,a<b))
print("{}>={}是{}".format(a,b,a>=b))
print("{}<={}是{}".format(a,b,a<=b))

print("{},{},a=b,a={}".format(a,b,b))
print("a+=1,a={}".format(a+1))
print("a-=1,a={}".format(a-1))
print("a*=2,a={}".format(a*2))
print("a/=2,a={}".format(a/2))
print("a%=2,a={}".format(a%2))
print("a**=2,a={}".format(a**2))
print("a//=2,a={}".format(a//2))

print('a={},b={},a&b={}'.format(bin(a),bin(b),a&b))
print('a={},b={},a|b={}'.format(bin(a),bin(b),a|b))
print('a={},b={},a^b={}'.format(bin(a),bin(b),a^b))
print('a={},~a={}'.format(bin(a),~a))
print('a={},a<<2={}'.format(bin(a),a<<2))
print('a={},a>>2={}'.format(bin(a),a>>2))

print('a={},b={},a and b = {}'.format(a,b,a and b))
print('a={},b={},a or b = {}'.format(a,b,a or b))
print('a={},not a = {}'.format(a,b,not a))

print('a is b = {}'.format(a is b))
print('a is not b = {}'.format(a is not b))

list1 = [10,30,50,70,90,100]
print('a={},list1={},a in list1 = {}'.format(a,list1,a in list1))
print('a={},list1={},a not in list1 = {}'.format(a,list1,a not in list1))

