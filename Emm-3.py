#循环
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

sum = 0
n = 99
while n > 0:
    sum = sum +n
    n = n -2
print(sum)
