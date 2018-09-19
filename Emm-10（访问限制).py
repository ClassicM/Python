#访问限制
class Student(object):

    def __init__(self,name,score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print('%s:%i'%(self.__name,self.__score))

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def set_score(self,score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score')

bart = Student('Bart',59)
bart.print_score()

#请把下面的Student对象的gender字段对外隐藏起来，用get_gender()和set_gender()代替，并检查参数有效性：
class Student(object):
    def __init__(self,name,gender):
        self.name = name
        self.__gender = gender

    def print_gender(self):
        print('%s:%s'%(self.name,self.__gender))

    def get_gender(self):
        return self.__gender

    def set_gender(self,gender):
        if gender != 'female' and gender != 'male':
            raise ValueError('Bad Gender')
        else:
            self.__gender = gender
#       if gender in ['feamale','male']
#            self.__name = gender
#       else:
#            raise ValueError('Bad Gender')


bart = Student('Bart','male')
print(bart.name)
bart.print_gender()
bart.get_gender()
bart.set_gender('female')
bart.print_gender()