from os.path import split

# 存储登录用户信息：用户名，密码，黑名单
users = {
    'jack':{'name':'jack','password':'123','status':True},
    'zs':{'name':'zs','password':'123456','status':True},
    'son':{'name':'son','password':'root','status':False}
}

print(users)
for i in range(3):
    user = input('请输入用户名：')
    pwd = input('请输入密码：')
    if user in users and pwd == users[user]['password'] and users[user]['status'] == True:
        print('登录成功！')
        break
    elif user in users and users[user]['status'] == False:
        print('账号失效，请联系管理员!')
    elif user in users and pwd != users[user]['password'] and users[user]['status'] == True:
        print('密码输入错误！')
    else:
        print('用户不存在，请先注册！')
