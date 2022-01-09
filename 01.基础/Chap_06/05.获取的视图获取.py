score_dic={'张三':100,'李四':99,'李明':89}
#1.获取所有的key
print('=====================1.获取所有的key=====================')
keys=score_dic.keys() #获取字典的所有key视图
print(keys)
print(type(keys))  #字典的key视图类型:<class 'dict_keys'>
print(list(keys))  #字典的key类型视图转为列表

#2.获取所有的values
print('=====================2.获取所有的values=====================')
values=score_dic.values() #获取字典的所有value视图
print(values)
print(type(values))     #字典的value视图类型:<class 'dict_values'>
print(list(values))     #字典的value类型视图转为元组

#3.获取所有的key-value对
print('=====================3.获取所有的key-value=====================')
items=score_dic.items()
print(items)
print(list(items))  #转换后的列表元素由元组组成===>[('张三', 100), ('李四', 99), ('李明', 89)]
