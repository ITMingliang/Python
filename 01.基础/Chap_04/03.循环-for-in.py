#可迭代对象:字符串、range()、

#1.字符串
for item in 'Python':
    print(item)

#2.range()
for i in range(10):
    print(i)

    #如果循环体中，不需要使用自定义变量，可将自定义的变量改写为_,如下：
for _ in  range(5):
    print('人生苦短，我用Python')


print('使用for循环，打印输出1~100的累加和')
sum=0
for item in range(1,101):
    if not  item%2:
        sum+=item
print('1到100之间的偶数和为：',sum)


