a=0 #变量存储的是一个对象的引用
print(id(a)) #内存地址

lst=['hello','world',98] #列表存储多个对象的引用，方便对对哦个对象进行引用处理
print(id(lst),type(lst))  #列表对象的内存地址

print(id(lst[0]),type(lst[0])) #列表对象的各个元素的地址
print(id(lst[1]),type(lst[1]))
print(id(lst[2]),type(lst[2]))


