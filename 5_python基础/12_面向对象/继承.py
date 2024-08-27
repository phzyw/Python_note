
# 父类
class Player(object):
    def __init__(self,name,age,city):
        self.name = name
        self.age = age
        self.city = city

# 子类
class VIP(Player):
    pass

# 子类继承父类
tom = VIP('tom',23,'淄博')
print(tom.__dict__)
