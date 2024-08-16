
# 集合的遍历
# s = {1,2,'jack'}
# for i in s:
#     print(i,end='--')       # 1--2--jack--

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

