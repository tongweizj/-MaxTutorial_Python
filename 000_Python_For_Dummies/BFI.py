'''
BIF 内置函数
'''

print()

len()

isinstance(names,list)   #判断names 是不是 list

#文本处理函数

the_file = open('sketch.txt') #读取文件

the_file = open('sketch.txt','w') #写入文件
print('hello world!',file = the_file) #用print 写入文件
pass

the.file.close() #完成之后，关闭文件

data.readline()   #读取一行数据
data.seek()  #返回数据起始位置


#分割字符串

data.split()


#help使用
>>> data = 'hellp'
>>> help(data.split)


pass  #忽视


find() #在字符串中找

#os 模块
>> import os
>> os.getcwd() #查看当前路径
>> os.chdir('../..') #进入这个目录

#排序
data.sort() #原地排序

sorted(data) #修改排序，但不改变元数据的次序