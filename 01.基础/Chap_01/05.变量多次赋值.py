name='黎明'
print(name)
print('标识:',id(name))

name='刘德华'
print(name) #多次赋值，变量名会指向新的空间，旧值成为内存垃圾
print('标识',id(name))