from cProfile import label

import wx

class MyFrame(wx.Frame):

    # 按钮位置
    pos_x, pos_y = 10,70
    # 按钮宽度,高度
    btn_w, btn_h = 50,50

    # 构造方法
    def __init__(self):
        # 创建窗口
        wx.Frame.__init__(self,None,title='简单计算器',size=(600,500))
        # 窗口居中显示
        self.Center()
        # 创建面板
        self.pl = wx.Panel(self,pos=(0,0),size=(600,500))
        # 创建文本框
        self.entry = wx.TextCtrl(self.pl,pos=(10,10),size=(400,50),style=wx.TE_RIGHT)
        # 创建按钮
        # 第一行
        self.btn_clear = wx.Button(self.pl,label='C',pos=(self.pos_x,self.pos_y),size=(self.btn_w,self.btn_h))
        self.btn_div = wx.Button(self.pl,label='/',pos=(self.pos_x+60,self.pos_y),size=(self.btn_w,self.btn_h))
        self.btn_mul = wx.Button(self.pl,label='*',pos=(self.pos_x+120,self.pos_y),size=(self.btn_w,self.btn_h))
        self.btn_back = wx.Button(self.pl,label='<--',pos=(self.pos_x+180,self.pos_y),size=(self.btn_w,self.btn_h))

        # 第二行
        self.btn_7 = wx.Button(self.pl,label='7',pos=(self.pos_x,self.pos_y+60),size=(self.btn_w,self.btn_h))
        self.btn_8 = wx.Button(self.pl,label='8',pos=(self.pos_x+60,self.pos_y+60),size=(self.btn_w,self.btn_h))
        self.btn_9 = wx.Button(self.pl,label='9',pos=(self.pos_x+120,self.pos_y+60),size=(self.btn_w,self.btn_h))
        self.btn_sub = wx.Button(self.pl,label='-',pos=(self.pos_x+180,self.pos_y+60),size=(self.btn_w,self.btn_h))

        # 第三行
        self.btn_4 = wx.Button(self.pl,label='4',pos=(self.pos_x,self.pos_y+120),size=(self.btn_w,self.btn_h))
        self.btn_5 = wx.Button(self.pl,label='5',pos=(self.pos_x+60,self.pos_y+120),size=(self.btn_w,self.btn_h))
        self.btn_6 = wx.Button(self.pl,label='6',pos=(self.pos_x+120,self.pos_y+120),size=(self.btn_w,self.btn_h))
        self.btn_add = wx.Button(self.pl,label='+',pos=(self.pos_x+180,self.pos_y+120),size=(self.btn_w,self.btn_h))

        # 第四行
        self.btn_1 = wx.Button(self.pl,label='1',pos=(self.pos_x,self.pos_y+180),size=(self.btn_w,self.btn_h))
        self.btn_2 = wx.Button(self.pl,label='2',pos=(self.pos_x+60,self.pos_y+180),size=(self.btn_w,self.btn_h))
        self.btn_3 = wx.Button(self.pl,label='3',pos=(self.pos_x+120,self.pos_y+180),size=(self.btn_w,self.btn_h))
        self.btn_eq = wx.Button(self.pl,label='=',pos=(self.pos_x+180,self.pos_y+180),size=(self.btn_w,self.btn_h))

        # 第五行
        self.btn_0 = wx.Button(self.pl,label='0',pos=(self.pos_x,self.pos_y+240),size=(self.btn_w,self.btn_h))
        self.btn_point = wx.Button(self.pl,label='.',pos=(self.pos_x+120,self.pos_y+240),size=(self.btn_w,self.btn_h))

        # 绑定按钮点击事件
        self.Bind(wx.EVT_BUTTON,self.On_btn_clear,self.btn_clear)
        self.Bind(wx.EVT_BUTTON,self.On_btn_div,self.btn_div)
        self.Bind(wx.EVT_BUTTON,self.On_btn_mul,self.btn_mul)
        self.Bind(wx.EVT_BUTTON,self.On_btn_back,self.btn_back)
        self.Bind(wx.EVT_BUTTON,self.On_btn_7,self.btn_7)
        self.Bind(wx.EVT_BUTTON,self.On_btn_8,self.btn_8)
        self.Bind(wx.EVT_BUTTON,self.On_btn_9,self.btn_9)
        self.Bind(wx.EVT_BUTTON,self.On_btn_sub,self.btn_sub)
        self.Bind(wx.EVT_BUTTON,self.On_btn_4,self.btn_4)
        self.Bind(wx.EVT_BUTTON,self.On_btn_5,self.btn_5)
        self.Bind(wx.EVT_BUTTON,self.On_btn_6,self.btn_6)
        self.Bind(wx.EVT_BUTTON,self.On_btn_add,self.btn_add)
        self.Bind(wx.EVT_BUTTON,self.On_btn_1,self.btn_1)
        self.Bind(wx.EVT_BUTTON,self.On_btn_2,self.btn_2)
        self.Bind(wx.EVT_BUTTON,self.On_btn_3,self.btn_3)
        self.Bind(wx.EVT_BUTTON,self.On_btn_eq,self.btn_eq)
        self.Bind(wx.EVT_BUTTON,self.On_btn_0,self.btn_0)
        self.Bind(wx.EVT_BUTTON,self.On_btn_point,self.btn_point)

    # 事件方法
    # 第一行
    def On_btn_clear(self,event):
        pass

    def On_btn_div(self,event):
        pass


    def On_btn_mul(self,event):
        pass


    def On_btn_back(self,event):
        pass


    # 第二行
    def On_btn_clear(self,event):
        pass


    def On_btn_clear(self,event):
        pass


    def On_btn_clear(self,event):
        pass


    def On_btn_clear(self,event):
        pass


    def On_btn_clear(self,event):
        pass


    def On_btn_clear(self,event):
        pass


    def On_btn_clear(self,event):
        pass


    def On_btn_clear(self,event):
        pass


    def On_btn_clear(self,event):
        pass


    def On_btn_clear(self,event):
        pass


    def On_btn_clear(self,event):
        pass


    def On_btn_clear(self,event):
        pass


    def On_btn_clear(self,event):
        pass


    def On_btn_clear(self,event):
        pass




if __name__ == '__main__':
    # 创建对象
    app = wx.App()
    # 创建窗口
    frame = MyFrame()
    # 显示窗口
    frame.Show()
    app.MainLoop()