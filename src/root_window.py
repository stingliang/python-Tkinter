# -*- coding: utf-8 -*-

# @File        : root_window.py
# @CreateDate  : 2022-03-02
# @Author      : stingliang
# @Github      : https://github.com/stingliang

import tkinter as tk
from tkinter import messagebox


def normal_window():
    window = tk.Tk()
    # 设置窗口title
    window.title('stingliang')
    # 设置窗口大小:宽x高,注,此处不能为 "*",必须使用 "x"
    window.geometry('450x300')
    # 获取电脑屏幕的大小
    print("电脑的分辨率是%dx%d" % (window.winfo_screenwidth(), window.winfo_screenheight()))
    # 要求窗口的大小，必须先刷新一下屏幕
    window.update()
    print("窗口的分辨率是%dx%d" % (window.winfo_width(), window.winfo_height()))
    # 如使用该函数则窗口不能被拉伸
    # window.resizable(0,0)
    # 改变背景颜色
    window.config(background="#6fb765")
    # 设置窗口处于顶层
    window.attributes('-topmost', True)
    # 设置窗口的透明度
    window.attributes('-alpha', 1)
    # 设置窗口被允许最大调整的范围，与resizble()冲突
    window.maxsize(600, 600)
    # 设置窗口被允许最小调整的范围，与resizble()冲突
    window.minsize(50, 50)
    # 更改左上角窗口的的icon图标,加载C语言中文网logo标
    window.iconbitmap(r'C:\Users\liangrui\Pictures\Camera Roll\sun.ico')
    # 添加文本内容,并对字体添加相应的格式 font(字体,字号,"字体类型")
    text = tk.Label(window, text="stingliang，网址：wowsting.club", bg="yellow", fg="red",
                    font=('Times_new_roman', 15, 'bold italic underline'))
    # 将文本内容放置在主窗口内
    text.pack()
    # 添加按钮，以及按钮的文本，并通过command 参数设置关闭窗口的功能
    button = tk.Button(window, text="关闭", command=window.quit)
    # 将按钮放置在主窗口内
    button.pack(side="bottom")
    # 进入主循环，显示主窗口
    window.mainloop()


def protocol_window():
    # 创建主窗口
    root = tk.Tk()

    # 定义回调函数，当用户点击窗口x退出时，执行用户自定义的函数
    def warning_window():
        # 显示一个警告信息，点击确后，销毁窗口
        if messagebox.showwarning("警告", "出现了一个错误"):
            # 这里必须使用 destory()关闭窗口
            root.destroy()

    # 使用协议机制与窗口交互，并回调用户自定义的函数
    root.protocol('WM_DELETE_WINDOW', warning_window)
    root.mainloop()


def button_command():
    # 定义窗口
    window = tk.Tk()
    window.title('stingliang')
    window.geometry('300x300')
    window.iconbitmap(r'C:\Users\liangrui\Pictures\Camera Roll\sun.ico')

    # 定义回调函数
    def callback():
        messagebox.showinfo("执行回调函数", "wowsting!")

    # 点击执行按钮
    button = tk.Button(window, text="执行", command=callback)
    button.pack()
    window.mainloop()


def window_pisition():
    window = tk.Tk()
    window.title('stingliang')
    window.iconbitmap(r'C:\Users\liangrui\Pictures\Camera Roll\sun.ico')
    # 设置窗口大小变量
    width = 300
    height = 300
    # 窗口居中，获取屏幕尺寸以计算布局参数，使窗口居屏幕中央
    screenwidth = window.winfo_screenwidth()
    screenheight = window.winfo_screenheight()
    size_geo = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
    window.geometry(size_geo)
    window.mainloop()


if __name__ == '__main__':
    normal_window()
    # protocol_window()
    # button_command()
    # window_pisition()
    pass
