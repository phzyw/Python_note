
class Player(object):
    def __init__(self,name,age,city):
        self.name = name
        self.age = age
        self.city = city

tom = Player(name='tom',age=23,city='杭州')
print(tom.__dict__)

