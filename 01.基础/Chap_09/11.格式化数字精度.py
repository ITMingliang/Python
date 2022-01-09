'''
1.%i或者%d：整数
2.%f：浮点数
'''
print('====================1.%d ======================')
print('%d' %99)

print('%1d' %99)
print('%10d' %99) #10或者1表示的是宽度，当小于数字的实际宽度，原样输出

print('====================2.%i ======================')
print('%i' %99)

print('%1i' %99)
print('%10i' %99) #10或者1表示的是宽度，当小于数字的实际宽度，原样输出

print('====================3.%f ======================')
print('%f' %3.1415926) #默认保留6位小数，会进行四舍五入

print('%.3f' %3.1415926) #指定保留位数,.3是表示精度
print('%10.3f' %3.1415926) #同时指定宽度和精度，宽度为10，保留小数点后3位

print('%.3f' %99) #整数

print('====================4.{} ======================')
print('{}'.format(3.1415926)) #如果只有一个占位符，0可以不写
print('{0}'.format(3.1415926))

print('{0:.3}'.format(3.1415926)) #指定位数，此处的.3为一共三位数，不包含小数点，0是占位符的位置顺序，可以省略不写
print('{:.3}'.format(3.1415926))

print('{0:.3f}'.format(3.1415926)) #指定精度,此处的.3f为精度，保留小数点后3位，0是占位符的位置顺序，可以省略不写

'''同时设定宽度和精度'''
print('{0:10.3f}'.format(3.1415926)) #指定精度,此处的.3f为精度，保留小数点后3位，10为指定的宽度