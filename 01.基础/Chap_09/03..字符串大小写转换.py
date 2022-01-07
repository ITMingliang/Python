s="hello,python"
print('=====================1.字符串转大写upper=====================')
a=s.upper();
print(s,id(s))
print(a,id(a))
'''
id标识发生改变
字符串为不可变对象，当发生改变时，会产生一个新的字符串对象
'''

print('=====================2.字符串转小写lower=====================')
b=s.lower()

print(s,id(s))
print(b,id(b))
print(s==b)
print(s is b)  #False,根据Python的驻留机制，两个不是一个对象
'''
内容相同，但是地址不是相等的，没有驻留
'''

print('=====================3.大小写同时转变swapcase=====================')
s="Hello,Python"
print(s.swapcase())

print('=====================4.单词的首字母大写，其余小写title=====================')
s="heLLo,PYTHON"
print(s.title())