print('=====================1.判断合法标识符=====================')
'''
合法的标识符：
字母（包含中文汉字）、数字和下划线组成，但是不能以数字开头
'''

s="1.2"  #包含小数点
print("1." ,s.isidentifier())

s="123_hello" #不能以数字开头
print("2.",s.isidentifier())

s="hello123" #合法
print("3.",s.isidentifier())

s="张三_" #合法
print("4.",s.isidentifier())

print('=====================2.判断空白字符=====================')
'''空白符包含：\t \n \r 空格'''
print("5.",'\t'.isspace()) #True
print("6.",' '.isspace())  #True
print("7.",'123'.isspace()) #False

print('=====================3.判断是否全字母组成=====================')
print("8.",'\tabc'.isalpha()) #False  包含制表符
print("9.",'abc'.isalpha()) #True
print("10.",'张三'.isalpha()) #True

print('=====================4.判断是否全部由十进制数字组成=====================')
print("11.",'123'.isdecimal()) #True
print("12.",'123四'.isdecimal()) #False

print('=====================5.判断是否全部由数字组成=====================')
print("13.",'123'.isnumeric()) #True
print("14.",'123四'.isnumeric()) #True
print("15.",'ⅠⅡⅢ'.isnumeric()) #True,，罗马数字也是数字

print('=====================6.判断是否全部由字母和数字组成=====================')
print("16.",'ⅠⅡⅢ'.isalnum()) #True，此处的罗马数字被认为是字母
print("17.",'Ⅰ2三'.isalnum()) #True，此处的三被认为是字母

print("18.",'您好！'.isalnum()) #False，此处的！被认为是非字母