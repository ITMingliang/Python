print('====================1.编码======================')
s='海上生明月'
print(s.encode(encoding='GBK'))#在GBK编码中，一个中文占用两个字节
print(s.encode(encoding='UTF-8'))#在UTF-8编码中，一个中文占用三个字节
'''
不同的编码格式，决定了占用的字节数
'''

print('====================2.解码======================')
'''byte代表的是二进制的数据，字节类型的数据'''
byte=s.encode(encoding='GBK')#编码
print(byte.decode(encoding='GBK'))#解码
#print(byte.decode(encoding='UTF-8'))#编码和解码的格式必须一致

byte=s.encode(encoding='UTF-8')#编码
print(byte.decode(encoding='UTF-8'))#解码