#注意if和while的区别

a=1
print('=============if===============')
#判断条件表达式
if a<10:
    #执行条件执行体
    print(a)
    a+=1

a=1
print('=============while===============')
#判断条件表达式
while a<10:
    #执行条件执行体
    print(a)
    a+=1

print('=============1~100之间的累加和===============')
'''
四步循环法：
1.初始化变量
2.条件判断
3.条件执行体(循环体）
4.改变变量
总结：初始化变量、判断的变量、改变的变量为同一个变量
'''

sum=0
a=1#初始化变量
while a<=100: #条件判断
    sum+=a  #执行条件执行体
    a+=1 #改变变量
print('1~100的和为：',sum)

print('=============1~100之间的偶数和===============')
sum=0
a=1#初始化变量
while a<=100: #条件判断
    #if a%2==0: #判断是否为偶数
    if not a%2:
        sum += a  # 执行条件执行体
    a+=1 #改变变量
print('1~100的偶数和为：',sum)



print('=============1~100之间的奇数和===============')
sum=0
a=1#初始化变量
while a<=100: #条件判断
    if a%2: #判断是否为偶数
        sum += a  # 执行条件执行体
    a+=1 #改变变量
print('1~100的奇数和为：',sum)