'''函数的定义'''

def fun(num):
    odd=[] #存奇数
    even=[] #存偶数
    for i in num:
        if i%2:
            odd.append(i)
        else:
            even.append(i)
    return odd,even


'''函数调用'''
print(fun([1,2,3,4,5,6,7,8,9,10]))


'''
函数返回值
   1.如果函数没有返回值，return可以省略不写
   2.函数的返回值，如果是1个，直接返回原类型
   3.函数的返回值，如果是多个，返回结果为元组
   
函数是否需要返回值，视情况而定
'''

'''1.返回值可以省略'''
def fun1():
    print('hello')
   #return


'''2.一个返回值'''
def fun2():
   return 'hello'

'''调用处要有变量进行存储'''

s1=fun2()
print(s1)


'''3.多个返回值'''
def fun3():
   return 'hello','Python'

'''函数调用'''
s2=fun3()
print(s2)
print(type(s2))
