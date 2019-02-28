# class 類別（種類）

class Student:
    def __init__(self): # initialize 初始化
        print('我誕生了')

    def do_hw(self):
        print('我在做作業')

    def study(self):
        print('我在讀書')

    def sleep(self):
        print('I am sleeping!')

s = Student()
s.do_hw()
s.study()
s.sleep()
