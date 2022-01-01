'''
水仙花数：
    原数=各个位数的数字的三次方求和
    如：153=1*1*1+5*5*5+3*3*3
'''

print('以下为100~999中的所有水仙花数字：')
for item in range(100,1000):
    ge=item%10        #个位
    shi=item//10%10   #十位
    bai=item//100     #百位
    #print(bai,shi,ge) #判断个十百为数字是否对的上
    if item==ge**3+shi**3+bai**3:
        print(item)


