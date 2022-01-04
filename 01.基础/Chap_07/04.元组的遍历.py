#1.使用索引获取元组元素：须知道元组的元素个数，否则会出现元组下标越界
print('=====================1.使用索引获取元组=====================')
t=('hello','World',98)

print(t[0])
print(t[1])
print(t[2])

print(type(t))

#print(t[3]) #元组下标越界

#2.for in 遍历
print('=====================2.for-in遍历=====================')
for item in t:
    print(item)