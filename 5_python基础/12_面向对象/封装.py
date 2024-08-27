




class Person(object):
    def __init__(self, name,age,city):
        self.__name = name          # _name 代表受保护的标量，__name 代表私有变量
        self.__age = age
        self.__city = city

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_city(self):
        return self.__city

    def set_age(self,age):
        # self.__age = age
        if isinstance(age,int):
            self.__age = age
        else:
            raise Exception('年龄只能为整数')

tom = Person('tom',23,'杭州')
print(tom.get_name())
print(tom.get_age())
print(tom.get_city())

tom.set_age(2)
print(tom.get_age())