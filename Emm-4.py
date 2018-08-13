#dict
#Python内置了字典：dict的支持，dict全称dictionary，在其他语言中也称为map，使用键-值（key-value）存储，具有极快的查找速度。
d = {'Amy':90,'Bob':85,'Candy':60}
print(d['Amy'])
d['Denny'] = 100
print(d)

#判断key是否存在，有两种方法：1.in 2.dict的get（）方法
print('Denny' in d)
print('Can' in d)
print(d.get('Amy'),-1)
print(d.get('Ken'),-1)

#删除key，用pop(key)方法
d.pop('Denny')
print(d)

'''
和list比较，dict有以下几个特点：

查找和插入的速度极快，不会随着key的增加而变慢；
需要占用大量的内存，内存浪费多。

而list相反：

查找和插入的时间随着元素的增加而增加；
占用空间小，浪费内存很少。
所以，dict是用空间来换取时间的一种方法。

dict可以用在需要高速查找的很多地方，在Python代码中几乎无处不在，正确使用dict非常重要，需要牢记的第一条就是dict的key必须是不可变对象。

'''


#set
#set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key。
s= set([1,3,2])
print(s)
#注意，传入的参数[1, 2, 3]是一个list，而显示的{1, 2, 3}只是告诉你这个set内部有1，2，3这3个元素，显示的顺序也不表示set是有序的。。
#重复元素在set中自动被过滤：
s = set([1,2,3,3,2,1,2])
print(s)
#通过add(key)方法可以添加元素到set中，可以重复添加，但不会有效果
s.add(4)
print(s)
#通过remove(key)方法可以删除元素
s.remove(4)
print(s)
#set可以看成数学意义上的无序和无重复元素的集合，因此，两个set可以做数学意义上的交集、并集等操作：
s1 = set([1,2,3])
s2 = set([2,3,4])
print(s1 & s2)
print(s1 | s2)

