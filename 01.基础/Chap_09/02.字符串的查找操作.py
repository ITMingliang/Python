s1="hello,hello"

print('=====================1.字符串查找=====================')
'''
默认第一次出现的位置
'''
print(s1.index('lo')) #3,如果找不到，则会抛出异常
#print(s1.index('k'))

print(s1.find('lo'))  #3，如果找不到，会返回-1
print(s1.find('k'))
'''
最后一次出现的位置
'''
print(s1.rindex('lo')) #9,没有找到则抛出异常
print(s1.rfind('lo'))#9，没有找到，返回-1