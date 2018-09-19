#type函数 判断对象类型
#判断基础类型
import types

print(type(123))
print(type('str'))
print(type(None))
#判断函数或者类
print(type(abs))

def fn():
    pass


print(type(fn)==types.FunctionType)
print(type(abs)==types.BuiltinFunctionType)
print(type(fn)==types.LambdaType)
print(type(x for x in range(10))==types.GeneratorType)


#isinstance函数 判断class类型
class Animal(object):
    def run(self):
        pass

class Dog(Animal):
    def run(self):
        pass

class Lucky(Dog):
    def run(self):
        pass

a = Animal()
b = Dog()
c = Lucky()
#isinstance()判断的是一个对象是否是该类型本身，或者位于该类型的父继承链上。
print(isinstance(a,Animal))
print(isinstance(b,Animal))
print(isinstance(a,Dog))

#能用type()判断的基本类型也可以用isinstance()判断
print(isinstance('a',str))
print(isinstance(1,float))

#还可以判断一个变量是否是某些类型中的一种，比如下面的代码就可以判断是否是list或者tuple
print(isinstance([1,2,3],(list,tuple)))
print(isinstance((1,2,3),(list,tuple)))

#dir函数，获取一个对象的所有属性和方法
print(dir('ABC'))
print('ABC'.__len__())

class MyDog(object):

    def __len__(self):
        return 100

dog = MyDog
print(dog.__len__(dog))

print('ABC'.lower())

#仅仅把属性和方法列出来是不够的，配合getattr()、setattr()以及hasattr()，我们可以直接操作一个对象的状态：
class MyObject(object):
    def __init__(self):
        self.x = 9
    def power(self):
        return self.x * self.x

obj = MyObject()
#print(obj.power())
print(hasattr(obj,'x'))#有属性 'x'吗
print(obj.x)
setattr(obj,'y',19)#设置属性'y'=19
print(hasattr(obj,'y'))#有属性'y'吗
print(getattr(obj,'y'))#获取属性'y'
print(getattr(obj,'z',404))#设置default参数，获取属性'z'，如果不存在，返回默认值404

print(hasattr(obj,'power')) #有属性 'power'吗
print(getattr(obj,'power')) #获取属性'power'
fn = getattr(obj,'power')#获取属性 'power' 并赋值到变量fn
print(fn)
print(fn())
'''
正确用法如下：
def readImage(fp):
    if hasattr(fp, 'read'):
        return readData(fp)
    return None

假设我们希望从文件流fp中读取图像，我们首先要判断该fp对象是否存在read方法，如果存在，则该对象是一个流，如果不存在，则无法读取。hasattr()就派上了用场。

请注意，在Python这类动态语言中，根据鸭子类型，有read()方法，不代表该fp对象就是一个文件流，它也可能是网络流，也可能是内存中的一个字节流，但只要read()方法返回的是有效的图像数据，就不影响读取图像的功能。
'''