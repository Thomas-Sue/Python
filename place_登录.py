# -*- coding: utf-8 -*-
"""
Created on Fri Feb 24 20:41:44 2017

@author: shutan
"""

from Tkinter import * root = Tk()
root.title('地大主页http://www.cug.edu.cn/') root['width'] = 200
root['height'] = 80 Label(root,text = '用户名',width = 6).place(x = 1,y =1
) Entry(root,width= 20 ).place(x = 45,y = 1) Label(root,text = '密
码',width = 6).place(x = 1,y = 20) Entry(root,width = 20,show =
'*').place(x = 45,y = 20) Button(root,text = '登录',width = 8).place(x =
40, y = 40) Button(root,text = '取消',width = 8).place(x = 110,y = 40)
mainloop()
