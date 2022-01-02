#1.使用()创建
print('=====================1.使用()创建=====================')
t=('Python','world',100)
print(t)
print(type(t))

t1='Python','world',100   #省略括号的创建方式
print(t1)
print(type(t1))

'''
元组在使用过程中，如果只包含一个元素，要进行在第一个元素后面添加逗号
'''
t=('Python')
print(t)
print(type(t))

t=('Python',)
print(t)
print(type(t))

#2.使用内置函数tuple()创建
print('=====================2.使用内置函数tuple()创建=====================')
t2=tuple(('Python','world',100))
print(t2)
print(type(t2))


#3.空元组的创建
print('=====================3.空元组的创建=====================')

'''前面回顾下，空字典和空列表创建'''
#空列表
ls1=[]
ls2=list()
print('====空列表====')
print(ls1,type(ls1))
print(ls2,type(ls2))
#空字典
dic1={}
dic2=dict()
print('====空字典====')
print(dic1,type(dic1))
print(dic2,type(dic2))
''''''
#空元组
t1=()
t2=tuple()
print('====空元组====')
print(t1,type(t1))
print(t2,type(t2))
