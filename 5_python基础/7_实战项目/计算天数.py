from calendar import month

# 用户输入日期，输出这是一年中的第几天。例：2024-01-05，应输出为是第五天

# date = input('请输入日期：').split('-')
# print(date)
# year = int(date[0])
# month = int(date[1])
# day = int(date[2])
# # 2024-08-16
# days = [0,31,28,31,30,31,30,31,31,30,31,30,31]
# result = 0
#
# if year % 4 ==0:
#     days[2]+=1
# result = 0
#
# for i in range(month):
#     result += days[i]
# result += day
#
# print(f'这是{year}年的第{result}天')

date = input('请输入日期：').split('-')
print(date)

year = int(date[0])
month = int(date[1])
day = int(date[2])

days = [0,31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]







