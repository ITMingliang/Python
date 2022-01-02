#1.zip进行生成字典
print('=====================1.zip进行生成字典=====================')
items=['Fruit','Books','Others']
prices=[100,200,300,400]
'''
items： 长度为3
prices：长度为4
以短的元组进行zip打包
'''
d= {item:price for item ,price in zip(items,prices)}
print(d)
#{'Fruit': 100, 'Books': 200, 'Others': 300}

