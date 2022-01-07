
print('=====================1.split()=====================')
s1="hello world Python"
'''
1.默认是以空格分割，返回值是一个列表
'''
print(s1.split())

'''
2.指定分割符号
'''
s='hello,world,python'
print(s.split())

'''下两句等价'''
print(s.split(','))
print(s.split(sep=','))

'''
3.指定最大劈分次数
'''
print(s.split(',',1))
print(s.split(sep=',',maxsplit=1))

print('=====================2.rsplit()=====================')
'''从右侧开始劈分'''
print(s.rsplit(','))


print(s.rsplit(',',1))#从右边开始劈分，左边的看成一个整体
print(s.rsplit(sep=',',maxsplit=1))
