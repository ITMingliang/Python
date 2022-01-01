print(520) #打印Int整数

print(3.1415926) #打印小数

print(1+1) #打印包含运算符的表达式

print("Hello World")  #打印字符串，默认换行打印

print("Hello","World")  #打印在一行

# 将数据输出到文件中
#注意：1.所指定的盘符必须存在；2.使用file=fp
fp=open('C:/Users/mingliang/Desktop/TEST/Python/test.txt','a+')  #书写时注意路径转意
print('hello world',file=fp)
fp.close()