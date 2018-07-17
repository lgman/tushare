str1 = '123'
print('string to int! "{}"-->{}'.format(str1,int(str1)))

print('string to float! "{}"-->{}'.format(str1,float(str1)))

print('string to complex! "{}"-->{}'.format(str1,complex(str1)))

dict1 = {'name':'long','id':'001'}
print('obj to str! "{}"-->{}'.format(dict1,str(dict1)))

#x = '(123-31) / 3 ** 5 = '
#???  print('object to expression string! {}-->{}'.format(x,repr(x)))

x1 = '((123-31) / 3) ** 5'
x2 = '(123-31) / 3 ** 5'
print('{}={}'.format(x1,eval(x1)))
print('{}={}'.format(x2,eval(x2)))

str2 = '我是中国人！'
print('string to tuple! {}-->{}'.format(str2,tuple(str2)))
print('string to list! {}-->{}'.format(str2,list(str2)))
print('string to set! {}-->{}'.format(str2,set(str2)))
print('string to frozenset! {}-->{}'.format(str2,frozenset(str2)))

#str2 ='(long,21),(li,20),(zhang,30)'
#??? print('string to tuple! {}-->{}'.format(str2,dict(str2)))

print('int to char,{}-->"{}"'.format(110,chr(110)))
#??? print('int to Unicode char,{}-->"{}"'.format(110,unichr(110)))

print('char to int,{}-->"{}"'.format('a',ord('a')))



