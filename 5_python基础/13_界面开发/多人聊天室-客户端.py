import wx

class Client(wx.Frame):
    # 构造方法
    def __init__(self):
#         实例属性
        self.name = 'tom' # 客户端名字


# 程序入口
if __name__ == '__main__':
    # 创建应用程序
    app = wx.App()
    # 创建客户端窗口
    client = Client()
    # 显示客户端窗口
    client.Show()
    # 一直显示窗口
    app.MainLoop()
