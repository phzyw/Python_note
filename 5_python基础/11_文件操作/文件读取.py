
# 打开文件
file = open('test.txt',encoding='utf-8')

# 读取文件
test = file.read()
print(test)

# 关闭文件
file.close()