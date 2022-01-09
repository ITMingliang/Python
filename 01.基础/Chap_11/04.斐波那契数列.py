'''
斐波那契数列：
第一项值为1，第二项的值为1，从第三项开始，当前项的值，等于前两项的和
'''

'''斐波那契函数定义'''
def fib(n):
    if n==1:
        return 1
    if n==2:
        return 1
    else:
        res=fib(n-1)+fib(n-2)
        return res

'''函数定义'''
print(fib(1))
print(fib(2))
print(fib(6))


#输出前6位的数列值：
for i in range(1,7):
    print(fib(i),end='\t')


