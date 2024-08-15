
# 字典的创建
# info = {
#     'name': '张三',
#     'age': '12',
#     'sex': 'male',
#     # 'name': 'jack'      # {'name': 'jack', 'age': '12', 'sex': 'male'} 键重复会覆盖之前的值
# }
# print(info)     # {'name': '张三', 'age': '12', 'sex': 'male'}

# 空字典的创建
# d = {}
# print(d)        # {}
#
# # 空字典的创建
# d = dict()
# print(d)        # {}

# 新增键值对
# info['height'] = 1.70
# print(info)     # {'name': '张三', 'age': '12', 'sex': 'male', 'height': 1.7}

# 获取键值对
# print(info['name'])     # 张三

# 修改键值对
# info['name'] = '李四'
# print(info)     # {'name': '李四', 'age': '12', 'sex': 'male', 'height': 1.7}

# 删除字典
# del info
# print(info)
# print("-"*60)
# 字典的遍历
info = {
    'name': '张三',
    'age': '12',
    'sex': 'male'
}

# 字典的遍历
# for i in info:
#     print(i, info[i])

# 字典的遍历
# for k,v in info.items():
#     print(k, v)

# 遍历字典key值
for k in info.keys():
    print(k)

# 遍历字典value值
for v in info.values():
    print(v)