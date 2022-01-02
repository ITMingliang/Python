lst=['hello','world',98,'hello']

print(lst.index('hello')) #如果列表中存在多个相同元素，返回第一个元素的索引

#不存在的元素，报错
#print(lst.index((5))) #ValueError: 5 is not in list

#指定范围内查找元素
print(lst.index('hello',1,4)) #1 为start，4为stop,但是不包括stop，左闭右开

