'''函数定义'''
def fun1(a,b=10):  #b的默认值为10
    print('a=', a)
    print('b=', b)

def fun2(*args):  #个数可变的位置形参
    print(args)

def fun3(**args):  #个数可变的关键字形参
    print(args)

'''函数调用'''
fun2(10,20,30,40)
fun3(a=10,b=20,c=30,d=40)

print('===========================')

'''函数定义'''
def fun4(a,b,c,d):
    print('a=',a)
    print('b=',b)
    print('c=',c)
    print('d=',d)

'''函数调用'''
fun4(10,20,30,40)#位置实参传递
fun4(a=10,b=20,d=40,c=30) #关键字实参传递
fun4(10,20,d=40,c=30) #前两个参数为位置实参传递，后两个参数为关键字实参传递

print('====================')

'''函数定义'''
def fun5(a,b,*,c,d): #从*之后的参数，在函数调用的时候，只能采用关键字实参传递
    print('a=',a)
    print('b=',b)
    print('c=',c)
    print('d=',d)

'''函数调用'''
#fun5(10,20,30,40)#*后采用位置实参传递，报错
fun5(a=10,b=20,d=40,c=30) #关键字实参传递
fun5(10,20,d=40,c=30) #前两个参数为位置实参传递，后两个参数为关键字实参传递
