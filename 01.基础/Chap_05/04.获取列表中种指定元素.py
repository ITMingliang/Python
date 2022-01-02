lst=['hello','world',98,'hello','2233']

#获取有索引为2的元素
print('正序:',lst[2]) #正序
print('逆序:',lst[-3])#逆序

print(lst[5])   #超出索引的范围抛出异常

'''
索引的范围：
正序：0~length-1
逆序：-1~-length
'''