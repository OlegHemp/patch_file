import wx

APP_EXIT = 1

class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super().__init__(parent, -1, title=title)
        menubar = wx.MenuBar()
        fileMenu = wx.Menu()
        #item = fileMenu.Append(wx.ID_EXIT, "Выход\tCtrl+Q", "Выход из приложения")
        item = wx.MenuItem(fileMenu, APP_EXIT, "Выход\tCtrl+Q", "Выход из приложения")
        item.SetBitmap(wx.Bitmap('exit16.png'))
        fileMenu.Append(item)
        menubar.Append(fileMenu, "&File")
        self.SetMenuBar(menubar)
        self.Bind(wx.EVT_MENU, self.onQuit, item)

    def onQuit(self, event):
        self.Close()


app = wx.App()

wnd = MyFrame(None, title='Копируем тесты!')
wnd.Centre()
wnd.Show()
app.MainLoop()
