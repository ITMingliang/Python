'''函数定义默认参数'''

'''函数定义'''
def fun(a,b=10):   #函数定义b的默认值为10
    print(a,b)

'''函数调用'''

fun(1) #此时未对形参b进行传递实参，将使用默认值
fun(1,2)

'''其实这种默认值的方法，我们在一直使用，如：print()函数'''

print('hello') #使用默认值end='\n'，进行换行
print('Python')

print('hello',end='\t') #传递参数，一个制表符间隔
print('Python')