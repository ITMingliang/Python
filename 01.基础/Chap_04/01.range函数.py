#range()的三种创建方式：range(start,stop，step)
'''
优点：
不管range对象表示的想有多长，所有的 range对象占用的内存空间相同
因为仅仅需要存储start，stop，step
只有用到元素的时候才去计算序列中的相关元素
'''
        #第一种创建方式，只有一个参数
r=range(10)   # 结果：[0, 1, 2, 3, 4, 5, 6, 7, 8, 9] 默认从0开始，默认步长为1，
print(r)  #range(0,10)
print(list(r)) #用于查看range对象中的整数序列  --->list是列表的意思

        #第二种创建方式   给出两个参数
r=range(1,10) #指定了起始值，从1开始，到10结束(不包含10)，默认步长1
print(list(r)) #[1, 2, 3, 4, 5, 6, 7, 8, 9]

        #第三种创建方式
r=range(1,10,2) #指定了起始值，从1开始，到10结束(不包含10)，步长2
print(list(r)) #[1, 3, 5, 7, 9]

'''判断指定值是否在序列中'''
print(5 not in list(r)) #False
print(5  in list(r))  #True


