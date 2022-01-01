'''
从键盘录入密码，最多输入3次，如果正确就结束循环,超过3次锁定账户
'''
print('==========for============')
for item in range(3):
    pwd=input('请输入密码：')
    if pwd=='8888':
        print('登录成功！')
        break
    elif item < 2:
        print('密码输入错误，请从新输入!')
    else:
        print('账户锁定！')

print('==========while============')
a=0
while a < 3:
    pwd=input('请输入密码：')
    if pwd=='8888':
        print('登录成功！')
        break
    elif a < 2:
        print('密码输入错误，请从新输入!')
    else:
        print('账户锁定！')
    a+=1