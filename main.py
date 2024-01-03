import wx

class Access2003Frame(wx.Frame):
    def __init__(self, parent, title):
        super(Access2003Frame, self).__init__(parent, title=title, size=(600, 400))

        self.panel = wx.Panel(self)
        self.create_toolbar()
        self.create_statusbar()

    def create_toolbar(self):
        toolbar = self.CreateToolBar()

        toolbar.AddTool(wx.ID_NEW, 'New', wx.Bitmap('icons/new.png'))
        toolbar.AddTool(wx.ID_OPEN, 'Open', wx.Bitmap('icons/open.png'))
        toolbar.AddTool(wx.ID_SAVE, 'Save', wx.Bitmap('icons/save.png'))
        toolbar.AddSeparator()
        toolbar.AddTool(wx.ID_CUT, 'Cut', wx.Bitmap('icons/cut.png'))
        toolbar.AddTool(wx.ID_COPY, 'Copy', wx.Bitmap('icons/copy.png'))
        toolbar.AddTool(wx.ID_PASTE, 'Paste', wx.Bitmap('icons/paste.png'))
        toolbar.Realize()

    def create_statusbar(self):
        statusbar = self.CreateStatusBar()
        statusbar.SetFieldsCount(3)
        statusbar.SetStatusWidths([-1, -2, -3])
        statusbar.SetStatusText('Ready', 0)
        statusbar.SetStatusText('Line: 1', 1)
        statusbar.SetStatusText('Column: 1', 2)

    def create_menus(self):
        menubar = wx.MenuBar()

        file_menu = wx.Menu()
        file_menu.Append(wx.ID_NEW, '&New')
        file_menu.Append(wx.ID_OPEN, '&Open')
        file_menu.Append(wx.ID_SAVE, '&Save')
        file_menu.AppendSeparator()
        file_menu.Append(wx.ID_EXIT, '&Exit')
        menubar.Append(file_menu, '&File')

        edit_menu = wx.Menu()
        edit_menu.Append(wx.ID_CUT, 'Cut')
        edit_menu.Append(wx.ID_COPY, 'Copy')
        edit_menu.Append(wx.ID_PASTE, 'Paste')
        menubar.Append(edit_menu, '&Edit')

        self.SetMenuBar(menubar)

app = wx.App()
frame = Access2003Frame(None, "Access 2003")
frame.Show()
app.MainLoop()
