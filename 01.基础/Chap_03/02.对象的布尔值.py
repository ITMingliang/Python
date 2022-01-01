print('=============以下对象的布尔值为False=============')
print(bool(False)) #False
print(bool(0))  #False
print(bool(0.0))  #False
print(bool(None))  #False
print(bool(''))  #False
print(bool(""))  #False

#空列表
print(bool([]))  #False
print(bool(list()))  #False

#空元组
print(bool(()))  #False
print(bool(tuple()))  #False

#空字典
print(bool({}))  #False
print(bool(dict()))  #False

#空集合
print(bool(set()))  #False

print('=============其他对象的布尔值均为True=============')