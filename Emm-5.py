#函数
#绝对值函数abs()
print(abs(10))
print(abs(-20))

#在多个参数中，返回最大值max()
print(max(1,3,6,163,1426,2353457))


'''
数据类型转换
转换为整数 int()
转换为字符串 str()
转换为浮点型 float()
转换为布尔型 bool()
'''
print(int('123'))
print(int(12.32))
print(str(123))
print(bool(1))
print('21.32')

#函数名其实就是指向一个函数对象的引用，完全可以把函数名赋给一个变量，相当于给这个函数起了一个“别名”：
a = abs
print(a(-1))

#hex()将整数转换为十六进制字符串
s1 = 245
s2 = 10233
print(hex(s1))
print(hex(s2))