'''
输出3x4的矩阵
'''
print('==========矩阵============')
for i in range(1,4):
    for j in range(1,5):
        print('*',end='\t') #不换行
    print() #换行

'''
直角三角形
'''
print('==============直角三角形============')
for x in range(1,10):  #行数
    for y in range(1,x+1):
        print('*',end='\t')
    print()
'''
九九乘法表
'''
print('==============九九乘法表============')
for x in range(1,10):  #行数
    for y in range(1,x+1):
        print(x,'x',y,'=',x*y,end='\t')
    print()