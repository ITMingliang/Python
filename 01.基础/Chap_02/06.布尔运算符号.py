#and :并且
print('===============and 并且===================')
a,b=10,20
print(a==10 and b==20) #True
print(a==10 and b!=20) #False
print(a>10 and b==20) #False

#or :或者
print('===============or 或者===================')
print(a==10 or b!=20) #True
print(a!=10 and b!=20) #False

#not :取反
print('===============not 取反===================')
f1=True
f2=False
print( not f2) #True
print( not f1) #False


#in与not in
print('===============in 与 not in===================')
s='helloworld'
print( 'w'  in s) #True
print( 'a' in s) #False

print( 'w'  not in s) #False
print( 'a' not in s) #True