#类和实例
class Student(object):#class后面紧接着是类名，即Student，类名通常是大写开头的单词，紧接着是(object)，表示该类是从哪个类继承下来的
    pass    #  通常，如果没有合适的继承类，就使用object类，这是所有类最终都会继承的类。

bart = Student()
print(bart) #变量bart指向的就是一个Student的实例，后面的0x10a67a590是内存地址，每个object的地址都不一样，而Student本身则是一个类。

bart.name = 'Bart Simpson'
print(bart.name)

class Student(object):

    def __init__(self,name,score):
        self.name = name
        self.score = score

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'

bart = Student("Brat Simpson",59)
print(bart.name)
print(bart.score)

def print_score(std):
    print('%s : %s' % (std.name,std.score))
print_score(bart)

lisa = Student('Lisa',99)
bart = Student('Bart',59)
print(lisa.name,lisa.get_grade())
print(bart.name,bart.get_grade())