#1.前面学习的判断元素是否在str中
print('#=====================1.前面学习的判断元素是否在str中=====================')
#区分大小写
print('p' in 'Python') #False
print('P' in 'Python')#True

print('P' not in 'Python')#False

#2.判断元素是否在列表中
print('=====================2.判断元素是否在列表中=====================')
lst=[10,20,'hello','world','您好']
print(20 in lst)
print('您好' not in lst)

#3.遍历
print('=====================3.遍历=====================')
'''
in后面要求是可迭代的变量
'''

for item in lst:
    print(item)



