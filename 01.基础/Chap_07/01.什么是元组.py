'''
通过前面学习，已经知道：
可变序列：元组，字典
不可变序列：字符串，元组(即将学习)

元组也是是不可变序列

不可变序列不能进行增删改
'''

#1.不可变序列，不能进行改变
s='hello'
print(id(s))
s+='world'
print(id(s))

'''
id发生变化，说明是不可变序列
'''