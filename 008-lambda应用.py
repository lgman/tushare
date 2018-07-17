#例子1
f = [lambda x:x*i for i in range(4)]
print(f[0](8))
print(f[1](8))
print(f[2](8))
print(f[3](8))

#例子2
f = [lambda x:i*i for i in range(4)]
print(f[0](8))
print(f[1](8))
print(f[2](8))
print(f[3](8))

#例子3
f = [lambda :i*i for i in range(4)]
print(f[0]())
print(f[1]())
print(f[2]())
print(f[3]())

#例子4
f = [lambda i=i:i*i for i in range(4)]
print(f[0]())
print(f[1]())
print(f[2]())
print(f[3]())
print(f[3](8))

#例子5
f = [lambda x=i:i*i for i in range(4)]
print(f[0]())
print(f[1]())
print(f[2]())
print(f[3]())
print(f[3](8))
