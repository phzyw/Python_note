
num1 = 10

def fun():
    global num1     # 声明在函数中使用的num1是全局变量num1
    num2 = 20
    num1 = 20
    print('num2的值为',num2)

fun()
print('num1的值为',num1)

# num1的值为 10
# num2的值为 20