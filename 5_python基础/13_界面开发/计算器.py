from cProfile import label

import wx

class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self,None,title='计算器',size=(600,500))
        self.Center()
        self.pl = wx.Panel(self,size=(600,500))
        # self.staticText = wx.StaticText(self.pl,label='计算器')
        self.entry = wx.TextCtrl(self.pl,pos=(10,10),size=(300,50),style=wx.TE_RIGHT)
if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame()
    frame.Show()
    app.MainLoop()