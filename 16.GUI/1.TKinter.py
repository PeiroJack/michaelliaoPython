#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
# 导入Tkinter包的所有内容
from tkinter import *

# 从Frame派生一个Application类,这是所有Widget的父容器
class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack() #把Widget加入到父容器中
        #pack()是最简单的布局，grid()可以实现更复杂的布局。
        self.createWidgets()
    
    # 创建一个Label和一个Button，当Button被点击时，触发self.quit()使程序退出。
    def createWidgets(self):
        self.helloLabel = Label(self, text='Hello, world!')
        self.helloLabel.pack()
        self.quitButton = Button(self, text='Quit', command=self.quit)
        self.quitButton.pack()

# 实例化Application，并启动消息循环
app = Application()
# 设置窗口标题：
app.master.title('Hello World')
# 主消息循环：
app.mainloop()
#GUI程序的主线程负责监听来自操作系统的消息，并依次处理每一条消息。
# 因此，如果消息处理非常耗时，就需要在新线程中处理。
'''

from tkinter import *
import tkinter.messagebox as messagebox

class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()
    
    def createWidgets(self):
        self.nameInput = Entry(self)
        self.nameInput.pack()
        self.alterButton = Button(self, text='Hello', command=self.hello)
        self.alterButton.pack()

    def hello(self):
        name = self.nameInput.get() or 'world'
        messagebox.showinfo('Message', 'Hello, %s' % name)

app =Application()
# 设置窗口标题：
app.master.title('Hello, world!')
# 主消息循环：
app.mainloop()