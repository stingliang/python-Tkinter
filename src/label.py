# -*- coding: utf-8 -*-

# @File        : label.py
# @CreateDate  : 2022-03-03
# @Author      : stingliang
# @Github      : https://github.com/stingliang

import tkinter as tk


def sample_label():
    window = tk.Tk()
    window.title("wowsting")
    window.geometry('400x200')
    window.iconbitmap('../data/sun.ico')
    # 若内容是文字则以字符为单位，图像则以像素为单位
    label = tk.Label(window, text="网址：wowsting.club", font=('宋体', 20, 'bold italic'), bg="#7CCD7C",
                     # 设置标签内容区大小
                     width=30, height=5,
                     # 设置填充区距离、边框宽度和其样式（凹陷式）
                     padx=10, pady=15, borderwidth=10, relief="sunken")
    label.pack()
    window.mainloop()


def image_label():
    window = tk.Tk()
    window.title("wowsting")
    window.iconbitmap('../data/sun.ico')
    # 显示图片(注意这里默认支持的图片格式为GIF)
    photo = tk.PhotoImage(file='../data/air_penguin.gif')
    print(type(photo))
    # 将图片放在主窗口的右边
    lab = tk.Label(window, image=photo).pack(side="right")
    # 显示文字，设置文本格式
    text = "welecome to wowsting!\n" \
           "Boost Tutorials\n" \
           "Python Practice"
    lab_text = tk.Label(window, text=text, fg='#7CCD7C', font=('Times_new_roman', 15, 'italic'),
                        justify='left', padx=10).pack(side='left')
    window.mainloop()


def message_label():
    # 创建主窗口
    window = tk.Tk()
    window.config(bg='#8DB6CD')
    window.title("wowsting")
    window.geometry('400x300')
    window.iconbitmap('../data/sun.ico')
    txt = "wowsting, url：wowsting.club"
    msg = tk.Message(window, text=txt, width=60, font=('Times', 10, 'bold'))
    msg.pack(side=tk.LEFT)
    # 开始程序循环
    window.mainloop()


if __name__ == '__main__':
    sample_label()
    image_label()
    message_label()
