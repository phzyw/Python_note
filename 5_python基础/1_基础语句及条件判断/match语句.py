

# x = 3
# match x:
#     case 1:
#         print(111)
#     case 2:
#         print(222)
#     case 3:
#         print(333)
#     case _:
#         print('others')

# 练习，判断年龄是否输入正确 0-120岁之间为正确

#
# age = int(input('请输入年龄：'))
# if 0 <= age <= 120:
#     print('年龄输入正确')
# else:
#     print('年龄输入错误，请重新输入')


# 练习：判断是否是闰年
year = input('请输入年份：')
if year.isdigit():
    if int(year) % 4 == 0:
        print('闰年')
    else:
        print('非闰年')
else:
    print('请输入年份数字')