print('====================1.位置传参 ======================')
'''函数定义'''
def multi(a,b): #a,b称为形式参数，简称形参，形参的位置在函数的定义处
    c=a*b
    return c

'''函数调用'''
result=multi(3,2)  #3,2称为实际参数，简称实参，实参的位置在函数的调用处
print('multi(3,2):',result)

print('====================2.关键字传参======================')

'''关键字调用'''
result=multi(b=2,a=3)  #位置传参，根据形参的变量名对应传入进去，赋值名称相同的形参处
print('multi(b=2,a=3):',result)
