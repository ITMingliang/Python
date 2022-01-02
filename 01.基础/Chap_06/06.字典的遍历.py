score_dic={'张三':100,'李四':99,'李明':89}
#1.遍历元素中的元素
print('=====================1.遍历元素中的元素=====================')
for item in score_dic :   #此处的item是字典中的key
    print(item,score_dic[item],score_dic.get(item))