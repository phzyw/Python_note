
class Player(object):
    numbers = 0
    def __init__(self,name,age,city):
        self.name = name
        self.age = age
        self.city = city
        Player.numbers += 1

    @classmethod
    def get_player(cls):        # 类方法
        print(cls.numbers)

    @staticmethod
    def get_name():
        pass

tom = Player('tom',23,'上海')

Player.get_player()