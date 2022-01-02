lst=[10,20,30,40,50,60,70,80]
print('=====================step为正数的情况=====================')
#start:stop:step,左闭右开
lst2=lst[1:6:1]
lst2=lst[1:6:]
lst2=lst[1:6]#默认步长为1
#上面三条语句等价

print('原列表：',lst)
print('原列表id：',id(lst))

print('切片列表：',lst2)
print('切片列表id：',id(lst2))

#采用步长为2
print(lst[1:6:2]) #[20, 40, 60]

#采用默认start，默认为0
print(lst[:6:2])

#采用默认stop,默认为length-1
print(lst[1::2])

print('=====================step为负数的情况=====================')
print('原列表:',lst)
print(lst[::-1])  #逆序输出
#start=7,stop省略，step=-1
print(lst[7::-1])

#start=6,stop=0，step=-2
print(lst[6:0:-2])


'''
总结：
步长为整数：正序切片输出
步长为负数：逆序切片输出
'''
