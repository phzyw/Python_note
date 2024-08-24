
class Player(object):
    numbers = 0     # 类属性
    def __init__(self,name,age,city):   # 初始化函数（构造函数）
        self.name = name    # 实例属性
        self.age = age
        self.city = city
        Player.numbers += 1

    # 实例方法
    def show(self):
        print(f'{self.name}来自{self.city},年龄为{self.age}岁')

tom = Player('tom',34,'北京')
tom.show()