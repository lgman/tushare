f = open('000917.html')

for index,line in enumerate(f.readlines()):
    if index < 5:
        print(line.strip())
    else:
        break


'''
for line in f:
    print(line.strip())
'''


'''
first_line = f.readline()
print('first line:',first_line)
print('分割线'.center(50,'-'))
data = f.read()
print(data)
f.close()
'''
