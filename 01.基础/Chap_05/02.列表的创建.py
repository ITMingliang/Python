#创建方式一:使用方括号
lst1=['hello','world',98]
print(id(lst1),type(lst1))  #列表对象的内存地址

print(id(lst1[0]),type(lst1[0])) #列表对象的各个元素的地址
print(id(lst1[1]),type(lst1[1]))
print(id(lst1[2]),type(lst1[2]))

#创建方式二：使用内置函数list()
lst2=list['hello','world',98]

print(id(lst2),type(lst2))  #列表对象的内存地址

#print(id(lst2[0]),type(lst2[0])) #列表对象的各个元素的地址
#print(id(lst2[1]),type(lst2[1]))
#print(id(lst2[2]),type(lst2[2]))

'''
特点：
1.列表元素按照顺序有序排列
2.索引映射唯一数据
3.列表可以存储重复数据
4.任意类型数据混合存放
5.根据需要动态分配和回收
6.顺序：第一个元素索引为0，最后一个元素索引为length -1
7.逆序：第一个元素索引为-length ，最后一个元素索引为 -1
'''



