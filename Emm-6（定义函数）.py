import math

#定义函数 绝对值
def my_abs(x):
    if x >= 0:
        return x
    else :
        return -x
print(my_abs(-89))

#空函数
def nop():
   pass

# 给绝对值函数 加上错误判断
'''
def Abs(x):
    if not isinstance(x,(int,float)):
        raise TypeError('bad opearand type')
    if x >= 0:
        return x
    else:
        return -x
Abs('ad')
'''

def move(x,y,step,angle=0):
    nx = x + step * math.cos(angle)
    ny = y + step * math.sin(angle)
    return nx,ny
x,y = move(100,100,60,math.pi / 6)
print(x,y)

#函数的参数
#位置参数
def power(x):
    return x * x
print(power(7))

#默认参数
def powers(x,n=2):
    s = 1
    while n > 0:
        n = n -1
        s = s * x
    return s
print(powers(2))

def add_end(L=[]):
    L.append('End')
    return L
print(add_end([1,2,3]))
print(add_end())
print(add_end())

def add_end(L=None):
    if L is None:
        L = []
    L.append('End')
    return L
print(add_end([1,2,3]))
print(add_end())

#可变参数
def calc(numbers):
    sum = 0
    for n in numbers:
        sum = numbers + n * n
    return  sum
A = calc([1,2,3])
print(A)