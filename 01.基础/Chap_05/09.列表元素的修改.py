list=[1,3,5,7]

#1.一次修改一个值
print('=====================1.一次修改一个值=====================')
print('原列表：',list)
list[2]=50
print('修改后列表：',list)


#2.一次修改多个值
print('=====================2.一次修改多个值=====================')
print('原列表：',list)
list[1:4]=[1000,2000,3000]
print('修改后列表：',list)