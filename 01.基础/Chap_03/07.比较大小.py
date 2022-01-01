
#比较大小

#方案一：
num_a=int(input('请输入第一个整数：'))
num_b=int(input('请输入第二个整数：'))

if num_a>=num_b:
    print(num_a,'大于等于',num_b)
else:
    print(num_a,'小于',num_b)

#方案二：使用条件表达式进行判断==> if else的简写
num_a=int(input('请输入第一个整数：'))
num_b=int(input('请输入第二个整数：'))
print('=========使用条件表达式进行比较========')
#为True时执行if前，为False执行else后
print( str(num_a)+'大于等于'+str(num_b) if num_a>=num_b else str(num_a)+'小于'+str(num_b))

