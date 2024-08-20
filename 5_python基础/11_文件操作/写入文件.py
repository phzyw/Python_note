
# 打开文件
file = open('test2.txt',mode='w',encoding='utf-8')

# 写入文件
file.write('hello,world')

# 关闭文件
file.close()

f = open('test2.txt',mode='r',encoding='utf-8')
context = f.read()
print(context)

file.close()