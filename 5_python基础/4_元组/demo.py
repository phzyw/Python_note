# tuple1 = (123, 'hello world', True)
# print(tuple1)
# print(type(tuple1))
#
# tuple2 = (1,)        # 当元组里只有一个元素时，需要在元素后面加上逗号,
# print(tuple2)
# print(type(tuple2))

# tuple3 = "hello world"
# tuple4 = tuple(tuple3)  # 类型转换，str--->tuple
# print(tuple4)


# 索引
# print(tuple1[1])        # hello world
#
# # 切片
# print(tuple1[::-1])     # True, 'hello world', 123)
#
# # 长度len
# print(len(tuple1))      # 3


# 获取元组元素最大值 max()
# tuple2 = (1,2,3,5,7)
# print(max(tuple2))      # 7

# 获取元组元素最小值 min()
# print(min(tuple2))      # 1

# 删除元组
# del tuple2
# print(tuple2)

# 元组相加
tuple1 = (123, 'hello world', True)
tuple2 = (1,2,3,5,7)
print(tuple1 + tuple2)      # (123, 'hello world', True, 1, 2, 3, 5, 7)

# 重复 *
print(tuple2 * 3)       # (1, 2, 3, 5, 7, 1, 2, 3, 5, 7, 1, 2, 3, 5, 7)