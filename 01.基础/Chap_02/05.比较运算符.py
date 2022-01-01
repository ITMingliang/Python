#比较运算符，比较的结果返回bool类型
print('===========比较运算符==============')
a,b=10,20
print('a>b吗？',a>b)

a,b=10,20
print('a不等于b吗？',a!=b)


#运算符==，=和is的区别
print('===========运算符==，=和is的区别==============')
'''
=   赋值运算符
==  比较运算符，比较的是值是否相同
is  比较对象额标识是否相同
'''
a=10
b=10 #===>首先检查系统是否有10的内存值，如果没有，则创建;有的话，把内存地址赋值给b
print(a==b)   #True，说明a和b的value相同
print(a is b) #True,说明a与b的标识相同
print('标识：',id(a),id(b))

print('===========list标识地址==============')
list1=[1,2,3,4]
list2=[1,2,3,4]
print(list1==list2) #True
print(list1 is list2) #False

print('标识：',id(list1),id(list2))