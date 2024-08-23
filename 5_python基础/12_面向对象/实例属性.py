#
# class Player(object):
#     pass
#
# # 实例化对象
# tom = Player()
# # 实例的属性
# tom.name = 'tom'
# tom.age = 23
# tom.city = '杭州'
# print(tom.name,tom.age,tom.city)        # tom 23 杭州

class Player(object):
    def __init__(self,name,age,city):  # 初始化函数
        self.name = name
        self.age = age
        self.city = city

tom = Player('tom',24,'杭州')
print(tom.name,tom.age,tom.city)        # tom 24 杭州

jack = Player('jack',35,'上海')

# 修改属性
jack.city = '合肥'        # jack 35 合肥
print(jack.name,jack.age,jack.city)

# __dict__ 获取对象（实例）的所有属性
print(jack.__dict__)        # {'name': 'jack', 'age': 35, 'city': '合肥'}


# 武器类：名字 攻击值 等级
class wuqi(object):
    def __init__(self,name,number,level):
        self.name = name
        self.number = number
        self.level = level

gun = wuqi('巴雷特',100,3)
print(gun.__dict__)