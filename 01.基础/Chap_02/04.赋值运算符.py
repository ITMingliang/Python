#普通赋值
i=3+4  #执行顺序：从右到左
print(i)

#链式赋值
a=b=c=d=10
print(a,b,c,d)
print('内存地址：',id(a),id(b),id(c),id(d))  #标识：内存地址

#参数赋值
print("----------支持参数赋值----------")
a=10
a+=10
print(a)

a-=2
print(a)

a*=2
print(a)

a/=2
print(a)

a//=2
print(a)

a%=2
print(a)

#系列解包赋值
print("----------解包赋值----------")
a,b,c=20,30,40
print(a,b,c)
print('内存地址:',id(a),id(b),id(c))

print("----------交换两个变量值----------")
a,b=10,20
print('交换前的值：',a,b)
#交换
b,a=a,b
print('交换后的值：',a,b)
