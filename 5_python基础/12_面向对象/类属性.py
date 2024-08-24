
class Player(object):
    numbers = 0     # 类属性
    def __init__(self,name,age,city):   # 初始化函数（构造函数）
        self.name = name    # 实例属性
        self.age = age
        self.city = city
        Player.numbers += 1

tom = Player('tom',23,'杭州')
print(tom.__dict__)
print(Player.numbers)