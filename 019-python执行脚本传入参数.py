import sys
import os

print(sys.argv)

#用参数传递操作系统命令，并执行
os.system(''.join(sys.argv[1:]))

#例子1：
#python 019-python执行脚本传入参数.py "md test"
#在当前目录下创建子目录test

#例子2：
#python 019-python执行脚本传入参数.py "regedit"
#打开注册表编辑
