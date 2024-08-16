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



### 八、总结

<img src="https://gitee.com/fattiger666/picgo/raw/master/01.png" alt="组合数据类型总结" style="zoom:80%;" />



<img src="https://gitee.com/fattiger666/picgo/raw/master/02.png" alt="组合数据类型单词总结" style="zoom:80%;" />



