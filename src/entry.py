# -*- coding: utf-8 -*-

# @File        : button.py
# @CreateDate  : 2022-03-09
# @Author      : stingliang
# @Github      : https://github.com/stingliang

import tkinter as tk
import time
from tkinter import messagebox


def dynamic_string():
    root = tk.Tk()
    root.title("wowsting.club")
    root.iconbitmap('../data/sun.ico')
    root.geometry('450x150+100+100')
    root.resizable(True, True)
    root.title('My Clock')

    # 获取时间的函数
    def gettime():
        # 获取当前时间
        dstr.set(time.strftime("%H:%M:%S"))
        # 每隔 1s 调用一次 gettime()函数来获取时间
        root.after(1000, gettime)

    # 生成动态字符串
    dstr = tk.StringVar()
    # 利用 textvariable 来实现文本变化
    lb = tk.Label(root, textvariable=dstr, fg='blue', font=("Times_new_roman", 75))
    lb.pack()
    # 调用生成时间的函数
    gettime()
    # 显示窗口
    root.mainloop()


def entry_sample_1():
    window = tk.Tk()
    # 设置主窗口
    window.geometry('500x100')
    window.title("wowsting.club")
    window.iconbitmap('../data/sun.ico')
    window.resizable(True, True)
    # 创建输入框控件
    entry1 = tk.Entry(window)
    # 放置输入框，并设置位置
    entry1.pack(padx=20, pady=20)
    entry1.delete(0, "end")
    # 插入默认文本
    entry1.insert(0, 'wowsting.club，github：https://github.com/stingliang')
    # 得到输入框字符串
    print(entry1.get())
    # 删除所有字符
    # entry1.delete(0, tk.END)
    window.mainloop()


def entry_sample_2():
    window = tk.Tk()
    # 设置主窗口
    window.geometry('250x100')
    window.title("wowsting.club")
    window.iconbitmap('../data/sun.ico')
    window.resizable(True, True)
    # 新建文本标签
    labe1 = tk.Label(window, text="Account：")
    labe2 = tk.Label(window, text="Passsword：")
    # grid()控件布局管理器，以行、列的形式对控件进行布局，后续会做详细介绍
    labe1.grid(row=0)
    labe2.grid(row=1)
    # 为上面的文本标签，创建两个输入框控件
    entry1 = tk.Entry(window)
    entry2 = tk.Entry(window, show='*')
    # 对控件进行布局管理，放在文本标签的后面
    entry1.grid(row=0, column=1)
    entry2.grid(row=1, column=1)
    # 显示主窗口
    window.mainloop()


def input_verify():
    window = tk.Tk()
    # 设置主窗口
    window.geometry('250x200+250+200')
    window.title("wowsting")
    window.iconbitmap('../data/sun.ico')
    window.resizable(True, True)

    # 创建验证函数
    def check():
        if entry1.get() == "wowsting":
            messagebox.showinfo("输入正确")
            return True
        else:
            messagebox.showwarning("输入不正确")
            entry1.delete(0, tk.END)
            return False

    # 新建文本标签
    labe1 = tk.Label(window, text="账号：")
    labe2 = tk.Label(window, text="密码：")
    labe1.grid(row=0)
    labe2.grid(row=1)
    # 创建动字符串
    dy_string = tk.StringVar()
    # 使用验证参数 validata,参数值为 focusout 当失去焦点的时候，验证输入框内容是否正确
    entry1 = tk.Entry(window, textvariable=dy_string, validate="focusout", validatecommand=check)
    entry2 = tk.Entry(window, show='*')
    # 对控件进行布局管理，放在文本标签的后面
    entry1.grid(row=0, column=1)
    entry2.grid(row=1, column=1)
    window.mainloop()


def sample_calculator():
    # 创建窗体
    window = tk.Tk()
    window.title('wowsting.club')
    window.geometry('300x300')
    window.iconbitmap('../data/sun.ico')
    # 创建一个容器来包括其他控件
    frame = tk.Frame(window)

    # 创建一个计算器
    def calc():
        # 用户输入的表达式，计算结果后转换为字符串
        result = "= " + str(eval(expression.get()))
        # 将计算的结果显示在Label控件上
        label.config(text=result)

    # 创建一个Label控件
    label = tk.Label(frame)
    # 创建一个Entry控件
    entry = tk.Entry(frame)
    # 读取用户输入的表达式
    expression = tk.StringVar()
    # 将用户输入的表达式显示在Entry控件上
    entry["textvariable"] = expression
    # 创建-一个 Button控件.当用户输入完毕后，单击此按钮即计算表达式的结果
    button1 = tk.Button(frame, text="等于", command=calc)
    # 设置Entry控件为焦点所在
    entry.focus()
    frame.pack()
    # Entry控件位于窗体的上方
    entry.pack()
    # Label控件位于窗体的左方
    label.pack(side="left")
    # Button控件位于窗体的右方
    button1.pack(side="right")
    # 开始程序循环
    frame.mainloop()


def spinbox_1():
    root = tk.Tk()
    root.title('wowsting.club')
    root.geometry('300x200+300+300')
    root.iconbitmap('../data/sun.ico')
    # 如果是数字使用 from_和to参数，范围 0-20,并且与2步长递增或递减
    w = tk.Spinbox(root, from_=0, to=20, increment=2, width=15, bg='#9BCD9B')
    w.pack()
    # 显示窗口
    root.mainloop()


def spinbox_2():
    root = tk.Tk()
    root.title('wowsting.club')
    root.geometry('300x200+300+300')
    root.iconbitmap('../data/sun.ico')
    # 使用 values 参数以元组的形式进行传参
    strings = tk.Spinbox(root, values=('Python', 'java', 'C语言', 'PHP'))
    strings.pack()
    # 开启事件循环
    root.mainloop()


if __name__ == '__main__':
    # dynamic_string()
    # entry_sample_1()
    # entry_sample_2()
    # input_verify()
    # sample_calculator()
    spinbox_1()
    spinbox_2()
    pass

