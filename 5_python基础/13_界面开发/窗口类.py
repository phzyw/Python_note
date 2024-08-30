from cProfile import label

import wx

class MyFrame(wx.Frame):

    def __init__(self):
        def onclick(event):
            print('按钮被点击了')

        wx.Frame.__init__(self,None,title='python学习系统')
        self.Center()
        pl = wx.Panel(self)
        staticText = wx.StaticText(pl,label='欢迎使用',pos=(10,10))
        btn = wx.Button(pl,label='按钮',pos=(100,100))
        self.Bind(wx.EVT_BUTTON,onclick,btn)



# 创建应用程序对象
app = wx.App()


# 创建窗口
frame = MyFrame()
# '显示窗口
frame.Show()

# 让窗口一直显示
app.MainLoop()
