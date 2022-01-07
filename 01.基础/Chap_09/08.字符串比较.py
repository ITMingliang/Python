'''
比较运算符：>、>=、<、<=、==、！=
'''
print('====================#1.>======================')
print('app'>'apple') #False

print('app'>'banana') #False
#字符=>对应原始值
print(ord('a')) #97
print(ord('b')) #98

#原始值=>对应字符
print(chr(97)) #a
print(chr(98)) #b
'''
比较原理：
逐位进行比较原始值，是和Unicode编码相似
'''
#其他运算符比价原理和>比较类似
print('====================#2.== ======================')
'''
==和is的区别:
==:比较的是value
is：比较的是id,即内存地址
'''

a=b='Pthon'
c='Pthon'

print(a==b) #True
print(a==c)#True

print(a is b) #True
print(a is c)#True
print(b is c)#True

print(id(a))#三个指向内存统一地址
print(id(b))
print(id(c))
