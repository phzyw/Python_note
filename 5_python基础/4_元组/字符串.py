# 字符串的遍历
# str1 = 'hello world'
# for i in str1:
#     print(i)

# 带索引的遍历
# for index,value in enumerate(str1):
#     print(index,value)

# range遍历
# for i in range(len(str1)):
#     print(i,str1[i])

# 类型转换
# print(str([1,2,3]),type(str([1,2,3])))

# 常用方法

str1 = 'hello world'

# 计数，计算所求的在字符串中有多少个数
print(str1.count('o'))      # 2

# 分割字符串 split()
print(str1.split(" "))      # ['hello', 'world']

# 字符串拼接
print('#'.join(str1))       # h#e#l#l#o# #w#o#r#l#d
