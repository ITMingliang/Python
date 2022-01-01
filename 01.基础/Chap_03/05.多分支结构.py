'''多分支结构，多选一执行
 从键盘录入一个整数，代表成绩
90~100：A
80~89: B
70~79: C
60~69: D
0~59:  E
<0 或者大于100: 非法数据
'''

score=int(input('请输入一个成绩：'))
if 90<= score<=100:
#if score>=90 and score<=100:
    print('您的分数等级为：A级')
elif score>=80 and score<=89:
    print('您的分数等级为：B级')
elif score>=70 and score<=79:
    print('您的分数等级为：C级')
elif score>=60 and score<=69:
    print('您的分数等级为：D级')
elif score>=0 and score<=59:
    print('您的分数等级为：E级')
else:
    print('对不起，您的分数输入错误，不在成绩的有效范围！')
