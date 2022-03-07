# -*- coding: utf-8 -*-

# @File        : button.py
# @CreateDate  : 2022-03-07
# @Author      : stingliang
# @Github      : https://github.com/stingliang

import tkinter as tk
from tkinter import messagebox


def sample_button():
    # 创建窗口
    window = tk.Tk()

    # 设置回调函数
    def callback():
        print("click me!")

    # 使用按钮控件调用函数
    tk.Button(window, text="点击执行回调函数", command=callback).pack()
    # 显示窗口
    tk.mainloop()


def custom_button():
    window = tk.Tk()
    # 设置窗口的标题
    window.title('wowsting')
    # 设置并调整窗口的大小、位置
    window.geometry('400x300+300+200')

    # 当按钮被点击的时候执行click_button()函数
    def click_button():
        # 使用消息对话框控件，showinfo()表示温馨提示
        messagebox.showinfo(title='Welcome', message='welcome to wowsting.club')

    # 点击按钮时执行的函数
    tk.Button(window, text='点击前往', bg='#7CCD7C', width=20, height=5, command=click_button).pack()
    # 显示窗口
    window.mainloop()


def image_button():
    window = tk.Tk()
    # 设置窗口的标题
    window.title('wowsting.club')
    # 设置窗口的大小
    window.geometry('400x300+300+200')

    # 当按钮被点击的时候执行click_button()函数
    def click_button():
        # 使用消息对话框控件，showinfo()表示温馨提示
        messagebox.showinfo(title='Welcome', message='welcome to wowsting.club')

    # 创建图片对象
    im = tk.PhotoImage(file='../data/start.png')
    # 通过image参数传递图片对象
    tk.Button(window, image=im, command=click_button).pack()
    # 启动窗口
    window.mainloop()


def position_button():
    win = tk.Tk()
    win.title("wowsting.club")
    win.iconbitmap('../data/sun.ico')
    win.geometry('400x200+100+100')
    win.resizable(True, True)
    # 将俩个标签分别布置在第一行、第二行
    tk.Label(win, text="Account：").grid(row=0)
    tk.Label(win, text="Password：").grid(row=1)
    # 创建输入框控件
    e1 = tk.Entry(win)
    # 以 * 的形式显示密码
    e2 = tk.Entry(win, show='*')
    e1.grid(row=0, column=1, padx=10, pady=5)
    e2.grid(row=1, column=1, padx=10, pady=5)

    # 编写一个简单的回调函数
    def login():
        messagebox.showinfo('welcome to wowsting.club')

    # 使用 grid()的函数来布局，并控制按钮的显示位置
    tk.Button(win, text="Login", width=10, command=login).grid(row=3, column=0, sticky="w", padx=10, pady=5)
    tk.Button(win, text="Logout", width=10, command=win.quit).grid(row=3, column=1, sticky="e", padx=10, pady=5)
    win.mainloop()


if __name__ == '__main__':
    # sample_button()
    # custom_button()
    # image_button()
    position_button()
    pass
