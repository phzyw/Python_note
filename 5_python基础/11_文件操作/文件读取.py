import os
# 打开文件
path = os.getcwd()      # 获取文件路径

file = open(path+'/test.txt',encoding='utf-8',mode='r')

# 读取文件
test = file.read()
print(test)

# 关闭文件
file.close()