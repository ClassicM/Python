print('循环')
print('for循环')
print('---------------------------------')
sum = 0
for x in [1,2,3,4,5,6,7,8,9,10]:
    sum = sum + x
print(sum)

A = list(range(10))
print(A)
#range函数提供自动生成整数序列的方法,从0开始

for x in list(range(101)):
    sum = sum + x
print(sum)

print('while循环')
print('---------------------------------')
sum = 0
n = 99
while n > 0:
    sum = sum +n
    n = n -2
print(sum)

'''

练习
请利用循环依次对list中的每个名字打印出Hello, xxx!
L = ['Bart', 'Lisa', 'Adam']

'''
L = ['Bart', 'Lisa', 'Adam']
for i in range(len(L)):
    print("hello,%s!"%L[i])

for name in L:
    print('hello,%s'%name)

#break 终止循环
'''n = 1
while n <= 100:
    print(n)
    n = n + 1
print('end')
'''

n = 1
while n <= 100:
    if n > 10:
        break
    print(n)
    n = n + 1
print('end')

print('continue 跳过循环')
print('---------------------------------')
n = 0
while n < 10:
    n = n + 1
    if n % 2 == 0:
        continue
    print(n)

'''
循环是让计算机做重复任务的有效的方法。

break语句可以在循环过程中直接退出循环，而continue语句可以提前结束本轮循环，并直接开始下一轮循环。这两个语句通常都必须配合if语句使用。

要特别注意，不要滥用break和continue语句。break和continue会造成代码执行逻辑分叉过多，容易出错。大多数循环并不需要用到break和continue语句，上面的两个例子，都可以通过改写循环条件或者修改循环逻辑，去掉break和continue语句。

有些时候，如果代码写得有问题，会让程序陷入“死循环”，也就是永远循环下去。这时可以用Ctrl+C退出程序，或者强制结束Python进程。

请试写一个死循环程序:
n = 0
while n <  100:
    n = n - 1
    print(n)
'''

