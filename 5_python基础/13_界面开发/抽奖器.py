import wx
import random


class MyFrame(wx.Frame):
    # 姓名列表
    NameList = ['tom','jack','jon','张三','李四','张虎','李军林']
    # 构造方法
    def __init__(self):
        wx.Frame.__init__(self,None,title='抽奖器',size=(400,300))
        # 窗口居中显示
        self.Center()
        # 创建面板
        self.pl = wx.Panel(self,size=(400,600),pos=(0,0))
        # 创建静态文本
        self.staticText = wx.StaticText(self.pl,label=random.choice(self.NameList),pos=(10,0),size=(400,100),style=wx.TE_CENTER)
        # 设置字体
        self.font = wx.Font(40,wx.FONTFAMILY_SWISS,wx.FONTSTYLE_NORMAL,wx.FONTWEIGHT_BOLD)
        self.staticText.SetFont(self.font)

        # 创建按钮
        self.btn = wx.Button(self.pl,label='点击抽奖',pos=(100,100))
        # 创建结束按钮
        self.btn_stop = wx.Button(self.pl, label='结束抽奖', pos=(200, 100))
        # 按钮绑定事件
        self.Bind(wx.EVT_BUTTON,self.onClick,self.btn)
        # 绑定结束按钮
        self.Bind(wx.EVT_BUTTON,self.stopClick,self.btn_stop)

    # 抽奖方法
    def onClick(self,event):
        # print('click')
        # self.staticText.SetLabelText(random.choice(self.NameList))
        # 创建定时器
        self.timer = wx.Timer(self)
        # 定时器绑定事件
        self.Bind(wx.EVT_TIMER,self.update_time,self.timer)
        # 启动定时器，100毫秒更新一次
        self.timer.Start(80)

    # 定时更改静态文本随机名字
    def update_time(self,event):
        self.staticText.SetLabelText(random.choice(self.NameList))

    # 结束抽奖
    def stopClick(self,event):
        self.timer.Stop()

# python程序主入口
if __name__ == '__main__':
    # 创建应用程序对象
    app = wx.App()
    # 创建窗口
    frame = MyFrame()
    # '显示窗口
    frame.Show()

    # 让窗口一直显示
    app.MainLoop()
