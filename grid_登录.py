# -*- coding: utf-8 -*-
"""
Created on Fri Feb 24 19:43:42 2017

@author: shutan
"""

from Tkinter import *
root = Tk()
root.title("登录地大主页http://www.cug.edu.cn/")
Label(root,text = '用户名').grid(row = 0,column = 0)
Entry(root).grid(row = 0,column = 1,columnspan = 2)
Label(root,text = '密码').grid(row = 1,column = 0)
Entry(root,show = '*').grid(row = 0,column = 1,columnspan = 2)
Button(root,text = '登录').grid(row = 3,column = 1,sticky = E)
Button(root,text = '取消').grid(row = 3,column = 2,sticky = W)
root.mainloop()
