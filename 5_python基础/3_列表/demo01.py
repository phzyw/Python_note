# 列表的创建
# list1 = [1,2]
# print(list1)

# 列表的索引
# list1 = [1,2,3]
# print(list1[0])

# 列表的切片
# list1 = [1,2,3,4,5,6,7]
# print(list1[::-1])
# print(list1[2::2])

# 列表的加法和乘法
# list1 = [1,2,3,4,5,6,7]
# list2 = [0,1,2]
# print(list1 + list2)
# print(list2 * 3)

# 列表的成员运算
# list1 = [1,2,3,4,5,6,7]
# print('1' in list1)
# print(0 in list1)
# print(0 not in list1)
# print(0 in [1,2,3])

# 内置函数
# list1 = [1,2,3,4,5,6,7]
# print(len(list1))       # 7
# print(max(list1))       # 7
# print(min(list1))       # 1
# print(list1+ [9])       # [1, 2, 3, 4, 5, 6, 7, 9]
#
# del list1[0]
# print(list1)            # [2, 3, 4, 5, 6, 7]
print('-' * 30)
# 列表的遍历
# list1 = [1,2,3,4,5,6,7]
# for i in list1:
#     print(i,end=' ')

# 带着索引遍历列表
# list1 = [1,2,3,4,5,6,7]
# for i,j in enumerate(list1):
#     print(i,j,end=' --- ')

# list1 = [1,2,3,4,5,6,7]
# for i in range(len(list1)):
#     print(i, list1[i])


# 计算平均年龄
# age = [12,34,56,34,23,4,23]
# # 求和
# total = sum(age)
# # 求人数
# num = len(age)
#
# print(int(total/num))

list1 = [1,2,3,4,5,6,7]
# 在列表末尾添加元素
# list1.append(0)
# print(list1)

# 添加列表
# list1.extend(['12','abc','哈哈哈'])
# print(list1)

# 插入元素
# list1.insert(2,444)
# print(list1)

# 删除元素，根据索引删除
# list1.pop(0)
# print(list1)

# 根据值删除元素
# list1.remove(3)
# print(list1)

# 清空整个列表
# list1.clear()
# print(list1)

# 计算平均值
total = 0
for i in list1:
    total += i
print(total / len(list1) )