import sys
sys.stdin.reconfigure (encoding='utf-8')

def menu():
    print('*' * 60)
    print('''
        欢迎使用日记本，请选择你的操作：
        1.打开日记本
        2.写入日记
        3.退出
    ''')

# 写入笔记
def write_note1():
    f = open('note.txt', mode='a',encoding='utf-8')
    note_text = input('请写入日记内容：')
    f.write(note_text+'\n')
    f.close()

# 打开笔记
def read_note():
    f = open('note.txt',mode='r',encoding='utf-8')
    read_text = f.read()
    print(read_text)
    f.close()


while True:
    menu()
    num = input('请选择你的操作：')
    if num == '1':
        read_note()
    elif num == '2':
        write_note1()
    elif num == '3':
        print('欢迎下次使用！')
        break
    else:
        print('请重新选择！')

print('*'*60)






