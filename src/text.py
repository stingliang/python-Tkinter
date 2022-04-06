# -*- coding: utf-8 -*-

# @File        : text.py
# @CreateDate  : 2022-04-06
# @Author      : stingliang
# @Github      : https://github.com/stingliang

from tkinter import *


def sample_text():
    win = Tk()
    win.title("wowsting")
    win.iconbitmap('../data/sun.ico')
    win.geometry('400x420')
    # 创建一个文本控件
    # width 一行可见的字符数；height 显示的行数
    text = Text(win, width=50, height=20, undo=True, autoseparators=False)
    text.grid()
    # INSERT 光标处插入；END 末尾处插入
    text.insert(INSERT, 'welcome to wowsting.club')

    # 定义撤销和恢复方法，调用edit_undo()和 edit_redo()方法
    def backout():
        text.edit_undo()

    def regain():
        text.edit_redo()

    # 定义撤销和恢复按钮
    Button(win, text='撤销', command=backout).grid(row=3, column=0, sticky="w", padx=10, pady=5)
    Button(win, text='恢复', command=regain).grid(row=3, column=0, sticky="e", padx=10, pady=5)
    win.mainloop()


if __name__ == '__main__':
    sample_text()
