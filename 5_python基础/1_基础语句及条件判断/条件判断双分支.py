# weather = '不下雨'
# if weather == '下雨':
#     print('带伞')
#
# else:
#     print('不用带伞')

# age = 13
# age = int(input('请输入年龄：'))
# if age >= 18:
#     print('可以去网吧')
# else:
#     print('成年才能进网吧')

'''
需求：
    <60   D
    60-70 C
    70-95 B
    95以上 A
'''
score  = int(input('请输入你的成绩：'))
# print(score)
if score <= 60:
    print('D')
elif 60 <= score < 70:
    print("C")
elif 70 <= score < 95:
    print('B')
else :
    print('A')
