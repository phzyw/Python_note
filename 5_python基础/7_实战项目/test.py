import datetime
date = datetime.datetime.now().date()
date = str(date).split('-')

# date = input('请输入日期：').split('-')
# 2023-08-16
year = int(date[0])
month = int(date[1])
day = int(date[2])

days = [0,31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
result = 0
if year % 4 == 0:
    days[2]+=1
for i in range(month):
    result += days[i]
result += day
print(f'今天是{year}年的第{result}天')

