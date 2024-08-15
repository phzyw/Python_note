
# count() 计数
tuple1 = (1,2,'hello',True)
# print(tuple1.count('hello'))        # 1

#  index() 获取索引值
# print(tuple1.index('hello'))        # 2

# 元组的遍历
# for i in tuple1:
#     print(i,end='---')        # 1---2---hello---True---

# 加上索引遍历元组
# for i,j in enumerate(tuple1):
#     print(i,j)

# range() 遍历
for i in range(len(tuple1)):
    print(i,tuple1[i])