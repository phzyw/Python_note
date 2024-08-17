# 制作简易的四则运算计算器
while True:
    info= input('请输入算式：')
    if '+' in info:     # 加法
        # print(info.split('+'))
        a = info.split('+')
        result = int(a[0])+int(a[1])
        print(result)
    elif '-' in info:
        a = info.split('-')
        result = int(a[0]) - int(a[1])
        print(result)
    elif '*' in info:
        a = info.split('*')
        result = int(a[0]) * int(a[1])
        print(result)
    elif '/' in info:
        a = info.split('/')
        result = int(a[0]) / int(a[1])
        print(result)
    elif info == 'c':
        print('程序结束')
        break