
# with语句可以简化文件操作的打开文件，读取文件，关闭文件步骤
with open('note.txt',mode='r',encoding='utf-8') as f:
    text = f.read()
    print(text)