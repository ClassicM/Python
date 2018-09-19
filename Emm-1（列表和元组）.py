print('list 和 tuple')
print('---------------------------------')

print('list的练习：')
classis =  ['Amy','Bob','Candy','David','Ella']
#list classis 索引是从0开始的
print("1-",len(classis))
#打印 clasis的元素个数
print("2-",classis[2])
#打印 classis中第3个元素的值
print("3-",classis)
#打印 整个classis list
classis.append('Floia')
print("4-",classis)
#在 classis末尾加上新元素"Floia"
classis.insert(5,'Zero')
print('5-',classis)
#在指定位置 classis第6个元素位置加上'zero'
print('6-',classis.pop())
#删除list末尾的元素
print('7-',classis.pop(0))
#删除list指定位置的元素，首位元素
classis [3] = 'Frank'
print('8-',classis)
#替换list指定元素的值

L = ['Apple',123,True]
print('9-不同的list元素',L)
#list 的数据类型可以完全不同
s = ['python','java',['asp','php'],'scheme']
print('10-',len(s))
print('11-',s)
#list 元素也可以是另一个list，二维数组



print('tuple的练习：')
classim = ('Amy','Bob','Candy')
print(classim)
#tuple 元组的元素无法更改，没有append、insert的方法

print('练习:')
Q = [
    ['Apple','Google','Microsoft'],
    ['Java','Python','Ruby','PHP'],
    ['Adam','Bart','Lias']
]
print(Q[0][0])
#打印Apple
print(Q[1][1])
#打印Python
print(Q[2][2])
#打印Lisa
