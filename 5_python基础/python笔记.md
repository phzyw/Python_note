### 前言：

​		[网课笔记来源](https://www.bilibili.com/video/BV1eZ421b7ag?p=126&vd_source=449e7c1c8c7cf9d09153fd8e95ca2022)



### 一、python 列表  

#### 1.语法

```
列表名 = [元素1,元素2,元素3,...]
```

#### 2.列表的创建

```python
list1 = [1,2]
```

#### 3.列表的索引

```python
list1 = [1,2,3]
print(list1[0])

# 输出结果为1
```

#### 4.列表的切片

```python
list1 = [1,2,3,4,5,6,7]
print(list1[::-1]) 	# 输出结果为[7, 6, 5, 4, 3, 2, 1]
print(list1[2::2])	# [3, 5, 7]

```

#### 5.列表的加法和乘法

```python
list1 = [1,2,3,4,5,6,7]
list2 = [0,1,2]
print(list1 + list2)	# [1, 2, 3, 4, 5, 6, 7, 0, 1, 2]
print(list2 * 3)		# [0, 1, 2, 0, 1, 2, 0, 1, 2]
```

#### 6.列表的成员运算

```python
list1 = [1,2,3,4,5,6,7]
print('1' in list1)		# False
print(0 in list1)		# False
print(0 not in list1)	# True
print(0 in [1,2,3])		# False
```

#### 7.内置函数

​	表达式：函数名 ()

```python
list1 = [1,2,3,4,5,6,7]
print(len(list1))       # 7	--求列表的个数
print(max(list1))       # 7	--求列表的最大值
print(min(list1))       # 1	--求列表的最小值
print(list1+ [9])       # [1, 2, 3, 4, 5, 6, 7, 9]

del list1[0]
print(list1)            # [2, 3, 4, 5, 6, 7]	--删除列表值，del list1 为删除列表
```

#### 8.列表的遍历

```python
# 遍历列表数据
list1 = [1,2,3,4,5,6,7]
for i in list1:
    print(i)		# 1 2 3 4 5 6 7 
    
# 带着索引遍历列表数据
list1 = [1,2,3,4,5,6,7]
for i,j in enumerate(list1):		# 枚举
    print(i,j)
    
# 使用range()遍历
list1 = [1,2,3,4,5,6,7]
for i in range(len(list1)):
    print(i, list1[i])

```

#### 9.列表的常用方法

​	表达式：变量.方法名()

```python
list1 = [1,2,3,4,5,6,7]
# 在列表末尾添加元素
 list1.append(0)
 print(list1)		# [1, 2, 3, 4, 5, 6, 7, 0]

# 添加列表
list1.extend(['12','abc','哈哈哈'])
print(list1)		# [1, 2, 3, 4, 5, 6, 7, '12', 'abc', '哈哈哈']


# 插入元素
list1.insert(2,444)
print(list1)		# [1, 2, 444, 3, 4, 5, 6, 7]

# 删除元素，根据索引删除
list1.pop(0)
print(list1)		# [2, 3, 4, 5, 6, 7]

# 删除元素，根据值删除元素
list1.remove(3)
print(list1)		# [1, 2, 4, 5, 6, 7]

# 清空整个列表
list1.clear()
print(list1)		# []

```





### 二、python 元组

#### 1.定义

​	Tuple(元组)与列表类似，不同之处是 元组的元素不能修改。

​	元组：表示多个元素组成的序列，用于存储一串信息，数据之间使用逗号，分隔。

​	元组使用 ()定义 例：

```python
info_tuple = ('张三', 29, 1.72)

# 定义元组
tuple1 = (123, 'hello world', True)
print(tuple1)
print(type(tuple1))		# <class 'tuple'>

tuple2 = (1,)        # 当元组里只有一个元素时，需要在元素后面加上逗号,
print(tuple2)
print(type(tuple2))		# <class 'tuple'>

tuple3 = "hello world"
tuple4 = tuple(tuple3)  # 类型转换，str--->tuple
print(tuple4)
```



#### 2.元组的通用操作

```python
# 索引
tuple1 = (123, 'hello world', True)
print(tuple1[1])        # hello world

# 切片
print(tuple1[::-1])     # True, 'hello world', 123)

# 长度len
print(len(tuple1))      # 3

# 获取元组元素最大值 max()
tuple2 = (1,2,3,5,7)
print(max(tuple2))      # 7

# 获取元组元素最小值 min()
print(min(tuple2))      # 1

# 删除元组 del()
del tuple2
print(tuple2)

# 元组相加
tuple1 = (123, 'hello world', True)
tuple2 = (1,2,3,5,7)
print(tuple1 + tuple2)      # (123, 'hello world', True, 1, 2, 3, 5, 7)

# 重复 *
print(tuple2 * 3)       # (1, 2, 3, 5, 7, 1, 2, 3, 5, 7, 1, 2, 3, 5, 7)

# in
print( 1 in tuple1 )        # True
```



#### 3.元组的常用方法

```python
# count() 计数
tuple1 = (1,2,'hello',True)
print(tuple1.count('hello'))        # 1

#  index() 获取索引值
print(tuple1.index('hello'))        # 2
```



#### 4.元组的遍历

```python
# 元组的遍历
for i in tuple1:
    print(i,end='---')        # 1---2---hello---True---
 
# 加上索引遍历元组
for i,j in enumerate(tuple1):
    print(i,j)
    
# range() 遍历，和加上索引遍历元组相同
for i in range(len(tuple1)):
    print(i,tuple1[i])
```





### 三、range函数

#### 1.定义

range 是系统提供的内建函数，range一般用于for-in循环遍历

```
原型：
	range([start,]stop[,step])
        range有三个参数,其中
        --start:表示列表的起始值，默认为0
        --stop:表示列表的结束值，但是不包含
        --strp:步长，默认为1
```

```python
# range(start,end,step)
print(list(range(10)))      # end [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(range(1,10)))    # start [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(range(1,10,2)))  # start,end,step [1, 3, 5, 7, 9]
```



### 四、字符串（String）

#### 1.定义

字符串可以用单引号''，双引号"" 和三引号"' '"括起来

#### 2.字符串的遍历

```python
# 字符串的遍历
str1 = 'hello world'
# for i in str1:
#     print(i)

# 带索引的遍历
# for index,value in enumerate(str1):
#     print(index,value)

# range遍历
for i in range(len(str1)):
    print(i,str1[i])
```



#### 3.常用方法

```python
str1 = 'hello world'

# 计数，计算所求的在字符串中有多少个数
print(str1.count('o'))      # 2

# 分割字符串 split()
print(str1.split(" "))      # ['hello', 'world']

# 字符串拼接
print('#'.join(str1))       # h#e#l#l#o# #w#o#r#l#d
```



### 五、字典（dict）

- dictionary（字典）是除列表外python中最灵活的数据类型
- 字典同样可以用来存储多个数据
- 通常用来存储 描述一个 物体的相关信息
- 和列表的区别
  1. 列表是 **有序** 的对象集合
  2. 字典是 **无序** 的对象集合

#### 1.定义

- 字典用 { } 定义
- 字典使用 **键值对** 存储数据，键值对之间使用，逗号隔开
- 键 key是索引
- 值 value是数据
- 键和值之间使用: 分隔
- 键必须是唯一的
- 值可以取任意数据类型，但键只能使用 字符串，数字或元组



#### 2.字典的创建

```python
# 字典的创建
info = {
    'name': '张三',
    'age': '12',
    'sex': 'male',
   # 'name': 'jack'      # {'name': 'jack', 'age': '12', 'sex': 'male'} 键重复会覆盖之前的值
}
print(info)     # {'name': '张三', 'age': '12', 'sex': 'male'}

# 空字典的创建
d = {}
print(d)        # {}

# 空字典的创建
d = dict()
print(d)        # {}

```



#### 3.字典的常用方法

```python

# 新增键值对
info['height'] = 1.70
print(info)     # {'name': '张三', 'age': '12', 'sex': 'male', 'height': 1.7}

# 获取键值对
print(info['name'])     # 张三

# 修改键值对
info['name'] = '李四'
print(info)     # {'name': '李四', 'age': '12', 'sex': 'male', 'height': 1.7}

# 删除字典
del info
```



#### 4.字典的遍历

```python
# 字典的遍历
for i in info:
    print(i, info[i])

# 字典的遍历
for k,v in info.items():
    print(k, v)
    
# 遍历字典key值
for k in info.keys():
    print(k)

# 遍历字典value值
for v in info.values():
    print(v)
```





### 六、集合 (set)

#### 1.定义

- 集合不允许有重复元素，如添加重复元素，则会自动过滤（删除），可以进行交集，并集的运算
- 是一种无序无重复元素的数据结构
- 与字典dict类似，是一组key的集合（不存储value）

#### 2.集合的创建

```python
# 集合的创建
s = set()
print(s,type(s))        # set() <class 'set'>

s = {1,2,3,4,1,2}
print(s,type(s))        # {1, 2, 3, 4} <class 'set'>
```



#### 3.集合的类型转换

```python
# list-->set
s = set([1,2,3,4])      
print(s,type(s))        # {1, 2, 3, 4} <class 'set'>

# tupel-->set
s = set((1,2,3,4))     
print(s,type(s))        # {1, 2, 3, 4} <class 'set'>

# str-->set
s = set('123')          
print(s,type(s))        # {'1', '2', '3'} <class 'set'>

# dict-->set
s = set({               
    'name':'jack',
    'age':30,
    'sex':'male'
})
print(s,type(s))        # {'age', 'sex', 'name'} <class 'set'>
```



#### 4.集合的常用操作

```python

# in
s = {1,2,3,4}
print(1 in s)       # True

# len 取长度
print(len(s))       # 4

# max 取最大值
print(max(s))       # 4

# min 取最小值
print(min(s))       # 1

# del 删除
del s
print(s)
```



#### 5.集合的遍历

```python
s = {1,2,'jack'}
for i in s:
    print(i,end='--')       # 1--2--jack--
```



#### 6.集合的常用方法

```python
# remove
s = {1,2,'jack'}
s.remove(1)
print(s)        # {2, 'jack'}

# update
s.update({3,5,7,8})
print(s)        # {2, 3, 5, 7, 8, 'jack'}

# add
s.add('张三')
print(s)        # {2, 3, 5, 'jack', 7, 8, '张三'}
```



#### 7.交集与并集操作

```python

s = {1,2,3,4,'jack'}
s1 = {4,5,6,4,1}

# 取交集
print(s & s1)       # {1, 4}

# 取并集
print(s | s1)       # {1, 2, 3, 4, 5, 6, 'jack'}    --去重后取并集
```



注：集合可用于列表的去重

```python
# 列表去重
score = [60,70,80,70,60,90]
print(set(score))       # {80, 90, 60, 70}
```





### 七、数据类型的划分

#### 1.可变类型 & 不可变类型

不可变数据类型在创建后，其值就不能被改变。python中的以下数据类型是不可变的。

- 数字（例如：int，float，complex）
- 字符串（例如：str）
- 元组（例如：tuple）
- 布尔类型（例如：bool）

可变数据类型的值可以在创建后被改变。python中的以下数据类型是可变的。

- 列表（list）
- 字典（dict）
- 集合（set）



### 八、数据类型总结

<img src="https://gitee.com/fattiger666/picgo/raw/master/01.png" alt="组合数据类型总结" style="zoom:80%;" />



<img src="https://gitee.com/fattiger666/picgo/raw/master/02.png" alt="组合数据类型单词总结" style="zoom:80%;" />





### 九、异常

#### 1.定义

代码没有语法问题，可以运行，但会出现运行时的错误，这种在运行期间检测到的错误被称为异常。

出现异常程序会终止执行，用户体验很差。

可以使用try-except语句进行异常的检测和处理。



#### 2.try-except语句

```python
try:
    n = int(input('请输入数字：'))
    n = n / 2
    print(n)

except ValueError as e:
    print('不能输入零')
    print(e)

except:
    print('请输入数字')

else:
    print('执行else')     # 运行没有被except语句捕获，执行else模块
finally:
    print('执行finallly') # 无论如何都要执行finally模块
```



#### 3.raise关键字

```python
raise 是 Python 中的一个关键字，用于引发一个指定的异常。当你的代码遇到了不可恢复的错误或者特定条件不满足时，你可以使用 raise 来抛出一个异常。
```





### 十、函数

#### 1.定义

使用关键字def，确定函数名称，参数名称，参数个数，编写函数体（用于实现函数功能的代码）

```python
def func():
	print('python')
```



#### 2.函数的调用

```python
# 函数的创建
def fun():
    print('python')

# 函数的调用，函数不调用是不会主动执行的
fun()       # python
```



#### 3.函数的参数

函数有 **形参** 和 **实参** ，也可以没有形参和实参

**形参**：就是函数定义时小括号里的参数，是用来接收参数用的，在函数内部作为变量使用。

**实参**：函数调用的时候，小括号里的参数，是用来把数据传递到函数内部用的。

```python
# 两数求和
def sum(num1,num2): # 形式参数
   result=num1+num2
   print(result)

# 函数的调用
sum(1,3)    # 实参
```

#### 4.函数的返回值（return）

函数中的返回值关键字为 return，是函数完成工作后，给调用者的一个结果。

```python
def sum(num1,num2): # 形式参数
   result=num1+num2
   return result
```



#### 5.变量的作用域

**全局变量** **&** **局部变量**

**全局变量**：是在函数外部定义的变量，所有函数内部都可以使用这个变量

**局部变量**：是在函数内部定义的变量，只能在函数内部使用，不能在函数外使用

```python
num1 = 10

def fun():
    num2 = 20
    print('num2的值为',num2)

print('num1的值为',num1)

fun()

# num1的值为 10
# num2的值为 20
```

若想在函数内部修改全局变量的值，可以使用关键字 global

```python
num1 = 10

def fun():
    global num1     # 声明在函数中使用的num1是全局变量num1
    num2 = 20
    num1 = 20
    print('num2的值为',num2)

fun()
print('num1的值为',num1)

# num1的值为 20
# num2的值为 20
```



#### 6.匿名函数

lambda函数是一种快速定义单行的最小函数，可以用在任何需要函数的地方

```python
 # 常规函数
def fun(x,y):
    return x+y

# 匿名函数
a = lambda x,y:x+y
print(fun(2,3))
```





#### 7.内置函数

<img src="https://gitee.com/fattiger666/picgo/raw/master/03.png" alt="内置函数" style="zoom:80%;" />

<img src="https://gitee.com/fattiger666/picgo/raw/master/04.png" alt="内置函数" style="zoom:80%;" />

<img src="https://gitee.com/fattiger666/picgo/raw/master/05.png" alt="内置函数" style="zoom:80%;" />

<img src="https://gitee.com/fattiger666/picgo/raw/master/06.png" alt="内置函数" style="zoom:80%;" />



#### 8.递归

- 一个函数调用自身称为递归调用
- 一个会调用自身的函数称为递归函数



### 十一、模块

- 模块就好比工具包，要想使用这个工具包中的工具，就需要导入（import）这个模块
- 每一个以.py结尾的python文件都是一个模块
- 在模块中定义的全局变量、函数都是模块能够提供给外界直接使用的工具。

模块导入的几种方式：

```python
# 导入模块所有函数
import my_module

# 导入模块指定函数
from my_module import fun,total

# 导入模块所有函数
from my_module import *

# 导入模块函数并改名
from my_module import fun as f,total as t
```





### 十二、文件及IO操作

#### 1.读取文件

```python
import os
# 打开文件
path = os.getcwd()      # 获取文件路径

file = open(path+'/test.txt',encoding='utf-8',mode='r')

# 读取文件
test = file.read()
print(test)

# 关闭文件
file.close()
```



#### 2.写入文件

```python
# 打开文件
file = open('test2.txt',mode='w',encoding='utf-8')

# 写入文件
file.write('hello,world')

# 关闭文件
file.close()
```



#### 3.追加文件

```python
# 打开文件
f = open('test3.txt',mode='a',encoding='utf-8')

# 写入文件
f.write('hello,world \n')

# 关闭文件
f.close()
```



#### 4.with语句

```python
# with语句可以简化文件操作的打开文件，读取文件，关闭文件步骤
with open('note.txt',mode='r',encoding='utf-8') as f:
    text = f.read()
    print(text)
```



#### 5.csv文件的读写

```python
import csv		# 引入csv库

csv.reader()
csv.writer()
```





### 十三、面向对象

#### 1.类的定义

```python
# 类的定义
class ClassName(object):
    pass

--class:表明这是一个类
--ClassName:类的名字
--():父类集合的开始和结束
--object:父类的名字，定义的类继承自父类，可以不写，默认为object。
		object是所有类的直接或间接父类。
```



#### 2.实例属性

```python
class Player(object):
    pass

tom = Player()
# 实例的属性
tom.name = 'tom'
tom.age = 23
tom.city = '杭州'
print(tom.name,tom.age,tom.city)        # tom 23 杭州

```



```python
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

```



#### 3.类属性

```python
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
```



#### 4.实例方法

```python

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
```



#### 5.类方法

```python
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

tom = Player('tom',23,'上海')

Player.get_player()
```



#### 6.静态方法

```python
    @staticmethod
    def get_name():
        pass
```



#### 7.继承

```python

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
print(tom.__dict__)		# {'name': 'tom', 'age': 23, 'city': '淄博'}
```



#### 8.多态

多态是面向对象编程中的一个核心概念，指的是一个实体能够表现出多种形态。

```python

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

```



#### 8.封装

```python

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
```



#### 9.魔法方法

python中的魔法方法（也可以称为特殊方法或双下划线方法）是一种在类定义中使用的特殊命名的约定方法。

当python遇到某些内置操作时，它会尝试在对象上调用这些魔法方法。

这些操作包括但不限于算数运算、属性访问、类型转换等。
