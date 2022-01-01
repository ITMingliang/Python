'''
会员：
    购物金额        >=200  8折
                   >=100  9折
                   不打折
非会员：
    购物金额        >=200  9.5折
                    不打折
'''
anwer=input('您是会员吗？y/n:')
money=float(input('请输入您的购物金额：'))

#判断是否为会员
if anwer=='y' :#会员
    if money>=200:
        print('打8折，您的付款金额为:',money*0.8)
    elif money>=100:
        print('打9折，您的付款金额为：',money*0.9)
    else:
        print('不打折，您的付款金额为：',money)
else:       #非会员
    if money >= 200:
        print('打9.5折，您的付款金额为:', money * 0.95)
    else:
        print('不打折，您的付款金额为：', money)

