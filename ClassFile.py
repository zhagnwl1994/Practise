class Student():
    """this is doc"""
    x = 13;
    name = "xiaoming"
    def getName(self):
        return self,self.x,self.name;

    def __init__(self):  #类似于java 中的 无参 构造方法
       print(self.x,self.name)
    def __init_subclass__(cls, **kwargs):
        print("__init_subclass__")

std = Student();





class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'

std2 = Student("lisi",int("90"));

print(std2.get_grade())

