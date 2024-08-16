

# 集合的创建
s = set()
print(s,type(s))        # set() <class 'set'>

s = {1,2,3,4,1,2}
print(s,type(s))        # {1, 2, 3, 4} <class 'set'>
print('*'*70)
# 类型转换
s = set([1,2,3,4])      # list-->set
print(s,type(s))        # {1, 2, 3, 4} <class 'set'>

s = set((1,2,3,4))      # tupel-->set
print(s,type(s))        # {1, 2, 3, 4} <class 'set'>

s = set('123')          # str-->set
print(s,type(s))        # {'1', '2', '3'} <class 'set'>

s = set({               # dict-->set
    'name':'jack',
    'age':30,
    'sex':'male'
})
print(s,type(s))        # {'age', 'sex', 'name'} <class 'set'>
