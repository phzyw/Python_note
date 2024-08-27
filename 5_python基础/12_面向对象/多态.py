
# 动物类
class Animal(object):
    def speak(self):
        print('动物叫')


class Dog(Animal):
    def speak(self):
        print('狗叫')

class Cat(Animal):
    def speak(self):
        print('猫叫')

def speak(object):
    object.speak()

dog = Dog()
cat = Cat()
animal = Animal()

animal.speak()
dog.speak()
cat.speak()

print("-"*70)

# 多态的实现
speak(animal)
speak(dog)
speak(cat)
