#1.remove
print('=====================1.remove=====================')
lst1=[10,20,30,40,20]

print('原列表：',lst1)
lst1.remove((20)) #从列表中移除元素，如果重复，只移除第一个
print('remove后的列表：',lst1)
#lst1.remove(100) #r如果不存在，那么就会报错


#2.pop：根据索引移除元素
print('=====================2.pop=====================')
lst1.pop(1)  #移除索引位置为1的元素
print('pop后的列表：',lst1)
lst1.pop()  #不写参数，默认移除最后一个元素
print('pop后的列表：',lst1)
#lst1.pop(5) #如果指定索引的位置不存在，将会抛出异常 ==> pop index out of range


#3.切片操作
print('=====================3.切片操作=====================')
list=[1,3,5,7]
'''
产生新的列表
'''
new_list=list[1::3] #切片结果放到一个新列表，创建了一个新的对象
print('原列表：',list) #原列表不发生变化
print('切片后的列表：',new_list)

'''
不产生新的列表
'''
print('原列表：',list)
list[1:4]=[]  #切除的列表用空列表替换
print('切片后的列表：',list)


#4.clear:清空列表对象
print('=====================4.clear=====================')
list=[1,3,5]
print('原列表：',list)
list.clear()
print('clear后列表：',list)

#5.del：删除列表对象，再次使用该对象，将会报错
print('=====================5.del=====================')
list=[1,3,5]
print('原列表：',list)
del list
print('del后的列表：',list)#将会输出：<class 'list'>
