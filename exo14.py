#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
#
# generated by wxGlade 1.1.0 on Tue Jan 14 15:16:42 2025
#

import wx

# begin wxGlade: dependencies
# end wxGlade

# begin wxGlade: extracode
# end wxGlade


class MyFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MyFrame.__init__
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.SetSize((787, 553))
        self.SetTitle("frame")

        self.panel_1 = wx.Panel(self, wx.ID_ANY)

        sizer_1 = wx.BoxSizer(wx.VERTICAL)

        grid_sizer_1 = wx.GridSizer(4, 2, 0, 0)
        sizer_1.Add(grid_sizer_1, 1, wx.EXPAND, 0)

        lbl_regex = wx.StaticText(self.panel_1, wx.ID_ANY, "Regex")
        grid_sizer_1.Add(lbl_regex, 0, wx.ALIGN_CENTER, 0)

        grid_sizer_1.Add((0, 0), 0, 0, 0)

        lbl_tocheck = wx.StaticText(self.panel_1, wx.ID_ANY, u"Chaine à analyser")
        grid_sizer_1.Add(lbl_tocheck, 0, wx.ALIGN_CENTER, 0)

        grid_sizer_1.Add((0, 0), 0, 0, 0)

        sizer_2 = wx.BoxSizer(wx.VERTICAL)
        grid_sizer_1.Add(sizer_2, 1, wx.EXPAND, 0)

        self.radio_box_1 = wx.RadioBox(self.panel_1, wx.ID_ANY, "", choices=["choice 1"], majorDimension=1, style=wx.RA_SPECIFY_COLS)
        self.radio_box_1.SetSelection(0)
        sizer_2.Add(self.radio_box_1, 0, 0, 0)

        self.radio_box_2 = wx.RadioBox(self.panel_1, wx.ID_ANY, "", choices=["choice 1"], majorDimension=1, style=wx.RA_SPECIFY_COLS)
        self.radio_box_2.SetSelection(0)
        sizer_2.Add(self.radio_box_2, 0, 0, 0)

        grid_sizer_1.Add((0, 0), 0, 0, 0)

        label_1 = wx.StaticText(self.panel_1, wx.ID_ANY, u"Résultat")
        grid_sizer_1.Add(label_1, 0, 0, 0)

        grid_sizer_1.Add((0, 0), 0, 0, 0)

        self.panel_1.SetSizer(sizer_1)

        self.Layout()
        # end wxGlade

# end of class MyFrame

class MyApp(wx.App):
    def OnInit(self):
        self.frame = MyFrame(None, wx.ID_ANY, "")
        self.SetTopWindow(self.frame)
        self.frame.Show()
        return True

# end of class MyApp

if __name__ == "__main__":
    app = MyApp(0)
    app.MainLoop()