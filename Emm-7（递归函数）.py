#递归函数
def fact(n):
    if n ==1:
        return 1
    return n * fact(n-1)
print(fact(1))
print(fact(5))
print(fact(100))
'''
使用递归函数需要注意防止栈溢出。
在计算机中，函数调用是通过栈（stack）这种数据结构实现的，每当进入一个函数调用，栈就会加一层栈帧，每当函数返回，栈就会减一层栈帧。
由于栈的大小不是无限的，所以，递归调用的次数过多，会导致栈溢出。
解决递归调用栈溢出的方法是通过尾递归优化
'''
#尾递归：在函数返回的时候，调用自身本身，并且return语句不能包含表达式
def fact(n):
    return fact_iter(n,1)

def fact_iter(num,product):
    if num == 1:
        return product
    return fact_iter(num -1 ,num * product)

# 请编写hanoi(n, a, b, c)函数，它接收参数n，表示3个柱子A、B、C中第1个柱子A的盘子数量，然后打印出把所有盘子从A借助B移动到C的方法

def hanoi(n, a, b, c):
    if n == 1:
        print(a, '-->', c)
    else:
        hanoi(n -1 ,a,c,b)
        print(a, '-->' , c)
        hanoi(n - 1, b,a,c)

print(hanoi(3,'A','B','C'))