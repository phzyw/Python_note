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
```

