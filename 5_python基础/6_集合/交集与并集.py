from itertools import count

s = {1,2,3,4,'jack'}
s1 = {4,5,6,4,1}

# 取交集
print(s & s1)       # {1, 4}

# 取并集
print(s | s1)       # {1, 2, 3, 4, 5, 6, 'jack'}    --去重后取并集
print('*'*70)


# 列表去重
score = [60,70,80,70,60,90]
s = set(score)
print(s)       # {80, 90, 60, 70}

# 统计学生各个分数有几人
for i in s:
    # 计算列表数量
    num = score.count(i)
    print(f'分数为{i}的人数为{num}')