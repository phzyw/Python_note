# 导入模块所有函数
# import my_module

# 导入模块指定函数
# from my_module import fun,total

# 导入模块所有函数
# from my_module import *

# 导入模块函数并改名
from my_package.my_math import fun as f,total as t
# h = my_module.fun(3,4)
h = f(5,6)
print(h)

print(t([1,4,6,6]))