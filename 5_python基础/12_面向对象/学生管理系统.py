
'''
    需求：学生，老师，班级，课程
'''
from tkinter.font import names


class User(object):
    def __init__(self,name,age,gender,id_number): # 属性：姓名，年龄，性别，学号
        self.name = name
        self.age = age
        self.gender = gender
        self.id_number = id_number

    # 获取学生信息
    def show_infos(self):
        print('*'*71)
        print(f'姓名：{self.name}')
        print(f'年龄：{self.age}')
        print(f'性别：{self.gender}')
        print(f'学(工)号：{self.id_number}')
        print('*' * 71)

# 学生类
class Student(User):
    # 初始化函数
    def __init__(self,name,age,gender,id_number): # 属性：姓名，年龄，性别，学号
        super().__init__(name,age,gender,id_number)

    # 获取学生信息
    def show_infos(self):
        super().show_infos()


# 老师类
class Teacher(User):
    # 属性：姓名，年龄，性别，工号，是否为导员，班级列表
    def __init__(self,name,age,gender,id_number,counsellor,cla):
        super().__init__(name,age,gender,id_number)
        self.counsellor = counsellor
        self.cla = cla

    def show_infos(self):
        super().show_infos()
        print(f'是否为导员：{['否','是'][self.counsellor]}')
        print('班级列表：')
        if not self.cla:
            print(' '*7 +'空')
        else:
            for i in self.cla:
                print(' '*7 +i)

# 班级类
class Cla(object):
    # 属性：班级名称，班级号，辅导员，学生
    def __init__(self,name,id_number,teacher,students):
        self.name = name
        self.id_number = id_number
        self.teacher = teacher
        self.students = students

    def show_infos(self):
        print('*' * 30 + '班级信息' + '*' * 30)

        print(f'班级名称：{self.name}')
        print(f'班级号：{self.id_number}')
        print(f'辅导员：{self.teacher.name}')
        print('学生：')
        if not self.students:
            print('空')
        else:
            for i in self.students:
                print(i)

        print('*' * 30 + '班级信息' + '*' * 30)

    # 增加学生
    def add_student(self,student):
        self.students.append(student)

    # 删除学生
    def del_student(self,student):
        self.students.remove(student)

# 课程类
class Course (object):
    pass


# tom = Student('tom',23,'男',1)
tom = Student('tom',23,'男',1)
tom.show_infos()

# 增加的学生
rose = Student('rose',23,'女',3)

jack = Teacher('jack',45,'男',5,False,[])
jack.show_infos()

jon = Teacher('jon',27,'男',7,True,['土木一班','计算机一班'])
jon.show_infos()

computer1 = Cla('计算机一班',1001,jon,['tom'])
computer1.show_infos()

computer2 = Cla('计算机二班',1002,jack,['jen','jay'])
# computer2.show_infos()
computer2.add_student(rose.name)
computer2.show_infos()

computer2.del_student(rose.name)
computer2.show_infos()