from zipimport import zipimporter

# n = input('请输入数字：')
# if n.isdigit() and int(n) != 0:
#     n = int(n)
#     n = n / 2
#     print(n)
# else:
#     print('请输入不为零的数字：')
try:
    n = int(input('请输入数字：'))
    n = n / 2
    print(n)

except ValueError as e:
    print('不能输入零')
    print(e)

except:
    print('请输入数字')

else:
    print('执行else')     # 运行没有被except语句捕获，执行else模块
finally:
    print('执行finallly') # 无论如何都要执行finally模块