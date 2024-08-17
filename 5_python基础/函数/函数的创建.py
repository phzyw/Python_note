
# 函数的创建
def fun():
    print('python')

# 函数的调用，函数不调用是不会主动执行的
fun()       # python


# 两数求和
def sum(num1,num2): # 形式参数
   result=num1+num2
   return result

# 函数的调用
sum(1,3)    # 实参


# 求和计算器
a = input('请输入第一个数：')
print(f'第一个数为：{a}')
b = input('请输入第二个数：')
print(f'第二个数为：{b}')
if a.isdigit() and b.isdigit():
    a= int(a)
    b= int(b)
    c = sum(a, b)
    print(f'结果为：{c}')
else:
    print('请输入数字！')


