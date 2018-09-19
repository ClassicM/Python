#继承
class Animal(object):
    def run(self):
        print('Animal is running...')

class Dog(Animal):
    def run(self):
        print('Dog is running')
    def eat(self):
        print('Eating meat..')

class Cat(Animal):
    def run(self):
        print('Cat is running')
    def eat(self):
        print('Eating fish..')

#当子类和父类都存在相同的run()方法时，我们说，子类的run()覆盖了父类的run()，在代码运行的时候，总是会调用子类的run()
dog = Dog()
dog.run()

cat = Cat()
cat.run()

#多态
a = list()
b = Animal()
c = Dog()

print(isinstance(a,list))
print(isinstance(b,Animal))
print(isinstance(c,Dog))
#a、b、c确实对应着list、Animal、Dog这3种类型

print(isinstance(c,Animal))
#Dog是从Animal继承下来的，当我们创建了一个Dog的实例c时，我们认为c的数据类型是Dog没错，但c同时也是Animal也没错，Dog本来就是Animal的一种！

def run_twice(animal):
    animal.run()
    animal.run()

run_twice(Animal())
run_twice(Dog())
run_twice(Cat())

class Tortoise(Animal):
    def run(self):
        print('Tortoise is running solwly')
#多态真正的威力：调用方只管调用，不管细节
# 而当我们新增一种Animal的子类时，只要确保run()方法编写正确，不用管原来的代码是如何调用的。这就是著名的“开闭”原则
#对扩展开放：允许新增Animal子类；
#对修改封闭：不需要修改依赖Animal类型的run_twice()等函数。
run_twice(Tortoise())

#静态语言 VS 动态语言
class Timer(object):
    def run(self):
        print('Strat..')

time = Timer()
time.run()



#鸭子类型

class Duck():
  def walk(self):
    print('I walk like a duck')
  def swim(self):
    print('i swim like a duck')

class Person():
  def walk(self):
    print('this one walk like a duck')
  def swim(self):
    print('this man swim like a duck')

duck = Duck()
duck.walk()
duck.swim()
person = Person()
person.walk()
person.swim()
'''
可以很明显的看出，Person类拥有跟Duck类一样的方法，当有一个函数调用Duck类，并利用到了两个方法walk()和swim()。
我们传入Person类也一样可以运行，函数并不会检查对象的类型是不是Duck，只要他拥有walk()和swim()方法，就可以正确的被调用。 
'''

