import wx
APP_EXIT = 1
class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super().__init__(parent, -1, title=title, size=(500, 200))
        menubar = wx.MenuBar()
        fileMenu = wx.Menu()
        aboutItem = fileMenu.Append(wx.ID_ABOUT, "О программе", "Отображение информации о программе")
        fileMenu.AppendSeparator()
        item = fileMenu.Append(wx.ID_EXIT, "Выход\tCtrl+Q", "Выход из приложения")
        item.SetBitmap(wx.Bitmap('exit16.png'))
        self.Bind(wx.EVT_MENU, self.onQuit, item)
        self.Bind(wx.EVT_MENU, self.OnAbout, aboutItem)
        self.sb = self.CreateStatusBar()
        self.sb.SetStatusText("Запущено")
        panel = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)
        panel.SetSizer(vbox)


        menubar.Append(fileMenu, "&File")
        self.SetMenuBar(menubar)


    def onQuit(self, event):
        self.Close()

    def OnAbout(self, e):
        dlg = wx.MessageDialog(self, "This is a mini editor keeping your text", "About pyNote", wx.OK)
        dlg.ShowModal()

app = wx.App()

wnd = MyFrame(None, title='Копируем тесты!')
wnd.Show()

app.MainLoop()