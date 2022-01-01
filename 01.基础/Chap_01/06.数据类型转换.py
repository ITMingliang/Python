#为什么要进行数据类型转换？
name="刘德华"
age=58

print(name,age)
print(type(name),type(age))

    #1.案例分析
#print('我叫'+name+',今年'+age+'岁') #将str类型与int类型进行连接时，报错

    #2.解决方案：类型转换
print('我叫'+name+',今年'+str(age)+'岁')

#str():将其他类型转为str
a=10
b=3.14
c=False
    #1.转换前
print(a,b,c)
print(type(a),type(b),type(c))
    #2.转换后
print(str(a),str(b),str(c))
print(type(str(a)),type(str(b)),type(str(c)))

#int():将其他类型转为int

s1='123'
f1=3.1415
s2='7.87'
f2=True
s3='hello'

    #1.原始类型
print(type(s1),type(f1),type(s2),type(f2),type(s3))
    #2.转换后的类型
print(int(s1),type(int(s1))) #将str转成int，字符串为：数字串
print(int(f1),type(int(f1))) #将float转成int，截取整数部分，舍掉小数部分
#print(int(s2),type(int(s2))) #将str转成int，报错，原因：字符串为小数串
print(int(f2),type(int(f2))) #将bool转成int
#print(int(s3),type(int(s3))) #将str转成int，字符串必须为数字串(整数)，非数字串不允许转化

