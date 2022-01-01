#####################################
#数据类型
    #整数类型——int
    #浮点数类型——float
    #布尔类型——bool
    #字符串类型——str
#####################################

#整数类型int，Python中默认输出十进制
    #1.整数，负数，0
n1=10
print(n1,type(n1))
n2=-10
print(n2,type(n2))
n3=0
print(n3,type(n3))
    #2.整数可以表示十进制，二进制，八进制
print('十进制',10)
print('二进制',0b10)#以0b开头
print('八进制',0o10)#以0o开头
        #十六进制取值范围为0~F
print('十六进制',0x10)#以0x开头

#浮点数据类型：float
    #1.有整数部分和小数部分组成
pi=3.1415926
print(pi,type(pi))
    #2.浮点数存储可能不精确性,因为计算机存储都是按照二进制存储的,二进制底层问题
print(1.1+2.2) #3.3000000000000003
print(1.1+2.1) #3.2
    #3.解决方案:导入decimal模块
from decimal import Decimal
print(Decimal(1.1)+Decimal(2.2))

#布尔类型：来表示真或者假的值
    #1.查看类型
t=True
f=False
print(t,type(t))
print(f,type(f))
    #2.布尔类型可以转换成整数：true->1,false->0
print(t+1) #1+1=2
print(f+1) #0+1=1

#字符串类型：又称为不可变的字符序列；可以用单引号，双引号，三引号来定义，
    #单引号和双引号定义的字符串必须在一行
    #三引号定义的字符串可以分布在连续的多行

    #1.单引号
str1='人生苦短，我用Python'
print(str1,type(str1))
    #2.双引号
str2="人生苦短，我用Python"
print(str2,type(str2))
    #3.三引号
str3='''人生苦短，
我用Python'''
print(str3,type(str3))

str4="""人生苦短，
我用Python"""
print(str4,type(str4))



