# -*- coding: utf-8 -*-
"""
Created on Fri Feb 24 17:49:37 2017

@author: shutan
"""

from Tkinter import *
root = Tk()
root.title('登录地大主页http://www.cug.edu.cn')

f1 = Frame(root)
f1.pack()
f2 = Frame(root)
f2.pack()
f3 = Frame(root)
f3.pack()

Label(f1,text = "学 号").pack(side = LEFT )
Entry(f1).pack(side = LEFT)
Label(f2,text = "密 码").pack(side = LEFT)
Entry(f2,show = "*").pack(side = LEFT)
Button(f3,text = "取消").pack(side = RIGHT)
Button(f3,text = "登录").pack(side = RIGHT)

mainloop()

