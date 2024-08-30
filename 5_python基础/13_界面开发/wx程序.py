import wx


def onclick(event):
    print('按钮被点击了')

# 创建应用程序对象
app = wx.App()
# 创建窗口
# frame = wx.Frame(None,title='python学习系统',size=(600,600),pos=(100,100))
frame = wx.Frame(None,title='python学习系统',size=(600,600))
frame.Center()

# 显示窗口
frame.Show()


# 创建面板
pl = wx.Panel(frame,size=(400,400))
pl.Center()
# 显示面板
pl.Show()

# 创建静态文本
staticText = wx.StaticText(pl,label="欢迎使用",pos=(100,100))
# 显示文本
staticText.Show()

# 创建按钮
btn = wx.Button(pl,label='按钮',pos=(10,20))
btn.Show()

# 给按钮绑定点击事件
frame.Bind(wx.EVT_BUTTON,onclick,btn)



# 进入主循环，让窗口一直显示
app.MainLoop()

