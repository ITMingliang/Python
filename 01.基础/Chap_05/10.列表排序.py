print('=====================1.sort=====================')
list=[1,4,7,8,5,2,3,6,9,10]
#调用列表对象的sort()方法
print('排序前列表：',list)
print('排序前列表标识：',id(list))

#默认升序排列
list.sort()
print('默认排序后列表：',list)
print('排序后列表标识：',id(list))

'''
标识一样，不产生新的列表对象
'''
#升序：关键字reverse=False
list.sort(reverse=False)
print('升序排序后列表：',list)

#降序：关键字reverse=True
list.sort(reverse=True)
print('降序排序后列表：',list)

print('=====================2.sorted=====================')
list=[1,4,7,8,5,2,3,6,9,10]
#调用列表对象的sorted()方法

print('排序前列表：',list)
#产生一个新的列表
new_list=sorted(list)
print('默认排序后原列表：',list)
print('默认排序后新列表：',new_list)

'''
原列表没有发生变化，将会产生一个新的列表
'''
#升序：关键字reverse=False
new_list=sorted(list,reverse=False)
print('升序排序后列表：',new_list)

#降序：关键字reverse=True
new_list=sorted(list,reverse=True)
print('降序排序后列表：',new_list)