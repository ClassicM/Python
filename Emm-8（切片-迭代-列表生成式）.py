#高级特性
#切片
L = list(range(100))
print(L)
print(L[0:5])#索引从0开始取，取到索引5为止，但不包括索引5
print(L[:3])#第一个索引是0，可以省略
print(L[2:4])#从索引2开始取，到索引4结束
print(L[-10:])#倒数切片，第一个元素索引是-1
print(L[:10:2])#前10个数，每两个取一个
print(L[::5])#所有数，每五个取一个

R = (1,2,3,4,5)
print(R[:3])#元组的切片操作，结果依然是元组

S = 'ABCDEFG'
print(S[:4])#字符串也可以看成一个list，每个元素就是一个字符，同样可以被切片

'''
利用切片操作，实现一个trim()函数，去除字符串首尾的空格，注意不要调用str的strip()方法：
'''
def trim(s):
    n = len(s)
    while len(s) > 0 and s[0] == '':
        s = s[1:]
    while len(s) > 0 and  s[-1] == '':
        s = s[:-1]
    return s
print(trim(" hello"))
print(trim("hello  "))

#迭代
#python中迭代是通过for..in来完成的
d= {'a':1,"b":2,"c":3}
for key in d:
    print(key)
for value in d.values():
    print(value)
for k,v in d.items():
    print(k,v)
#字符串也是可迭代对象，也可作用于for循环
for ch in 'ABCD':
    print(ch)
#当我们使用for循环时，只要作用于一个可迭代对象，for循环就可以正常运行
#如何判断一个对象是可迭代对象呢？可通过collections模块的lierable类型判断
from collections import Iterable
print(isinstance('abc',Iterable))#str是否可迭代
print(isinstance([1,2,3],Iterable))#list是否可迭代
print(isinstance(123,Iterable))#整数是否可迭代
#for循环中，同时引用两个变量
for x,y in ['as','a2','1x']:
    print(x,y)
#请使用迭代查找一个list中最小和最大值，并返回一个tuple
def findMinAndMax(L):
    if L == []:
        return (None,None)
    else:
        for a in L:
            for b in L:
                if a == min(L) and b == max(L):
                    return (a,b)
print(findMinAndMax([1.1,3451,3/4]))

#列表生成式，即List Comprehensions
print(list(range(1,11)))
#[1x1,2x2,3x3...10x10]
print([x * x for x in range(1,11)])
#筛选出仅偶数的平方
print([x * x for x in range(1,11) if x % 2 == 0])
#两层循环，生成全排列
print([m + n for m in 'ABC' for n in 'XXX'])
#列出当前目录下的所有文件和目录名
import  os #导入os模块
print([d for d in os.listdir('.')])# os.listdir可以列出文件和目录
#for 循环可以同时使用两个甚至多个变量
d = {'x':'A','y':'B','z':'C'}
for k ,v in d.items():
    print(k, '=' , v)
print([k + '=' + v for  k , v in d.items()])
L = ['Hello', 'World', 'IBM', 'Apple']
print([s.lower() for s in L])