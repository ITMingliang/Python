print('=====================1.字符串的替换=====================')
'''1.默认替换全部'''
s='hello,Python,Python,Python'
print(s.replace('Python','Java'))

'''2.指定替换次数'''
'''第三个参数为最大的替换次数'''
s='hello,Python,Python,Python'
print(s.replace('Python','Java',2))

print('=====================2.字符串的合并=====================')
'''对元组、列表或者字符串进行字符串合并'''
#1.列表
print('====================#1.列表======================')
lst=['hello','Java','Python','C++']
print('|'.join(lst))
print(','.join(lst))

#2.元组
print('==================#2.元组========================')
t=('hello','Java','Python','C++')
print('|'.join(t))
print(','.join(t))

#3.字符串
print('==================#2.字符串========================')
print('*'.join('Python')) #把字符串当做字符串序列进行连接
