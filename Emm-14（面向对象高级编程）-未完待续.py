#使用 __slots__
class Student(object):
    pass

    def set_score(self, score):  # 定义一个函数作为实例方法
        self.score = score


s = Student
s.name = 'Michael' #动态给实例绑定一个属性
print(s.name)


def set_age(self, age):  # 定义一个函数作为实例方法
    self.age = age


from types import MethodType
s.set_age = MethodType(set_age,s)
s.set_age(25)
print(s.age)
