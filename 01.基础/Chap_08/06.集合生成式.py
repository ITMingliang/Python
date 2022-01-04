'''列表生成式'''
lst =[ i*i for i in range(6)]
print(lst,type(lst))


'''集合生成式'''
s ={ i*i for i in range(6)}
print(s,type(s))

'''字典生成式'''
items=['Fruit','Books','Others']
prices=[100,200,300,400]
'''
items： 长度为3
prices：长度为4
以短的元组进行zip打包
'''
d= {item:price for item ,price in zip(items,prices)}
print(d)
print(id(d))
