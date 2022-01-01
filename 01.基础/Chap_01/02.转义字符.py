#1.制表符：\t
print("Hello\tworld")  # \t为一个制表符，占用4字节
print("Helloo\tworld") #不足4个字节，制表符填满
print("Hello0\tworld")
print("Helloooo\tworld") #4个字节已经满，重新开辟4个字节

#2.换行:\n
print("Hello\nworld")

#3.回车：\r
print("1 Hello\rworld")  #把前面\r内容覆盖

#4.退格：\b
print("Hello\bworld") #相当于删除前面一个字符

#5.原文输出：要求末尾不能为奇数个\
# print(R"Hello\bworld\\\")
print(R"Hello\bworld\\\\")