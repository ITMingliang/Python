#1.键的判断
print('=====================1.键的判断=====================')
score_dic={'张三':100,'李四':99,'李明':89}
print('张三' in score_dic)
print('李四' not in score_dic)


#2.增加
print('=====================2.增加=====================')
print('原字典：',score_dic)
score_dic['爱德华']=69   #当key值不存在时为新增，key存在时 则变成了修改
print('添加后字典：',score_dic)

#3.修改
print('=====================3.修改=====================')
score_dic['爱德华']=79  #key值存在时，完成修改
print('修改后的字典',score_dic)

#4.删除
print('=====================4.删除=====================')
del score_dic['爱德华']
print('删除后的字典',score_dic)
#del score_dic['爱德华']  #不存在的key，再次删除，抛出异常：KeyError: '爱德华'

score_dic.clear()  #清空字典元素
print('清空后的字典',score_dic,type(score_dic))
