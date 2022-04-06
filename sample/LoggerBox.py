# -*- coding: utf-8 -*-

# @File        : LoggerBox.py
# @CreateDate  : 2022-04-06
# @Author      : stingliang
# @Github      : https://github.com/stingliang
import datetime
import time
import tkinter as tk
from tkinter.filedialog import askopenfilename
import logging
import threading


class LoggerBox(tk.Text):

    def write(self, message):
        self.insert('end', message)


class SampleAppFramework:

    def __init__(self):
        self.__window = tk.Tk()
        self.__bin_filename = tk.StringVar()
        self.__log = logging.getLogger(self.__class__.__name__)
        self.__log.setLevel(logging.INFO)
        pass

    def __del__(self):
        pass

    def __main(self):
        while True:
            time.sleep(1)
            now = datetime.datetime.now()
            self.write_log(f"LoggerBox:{now}")

    def __select_file(self):
        self.__bin_filename.set(askopenfilename(title='Please choose a .bin file', filetypes=[('bin file', '*.bin')]))

    def __start_up(self):
        # 打开日志窗口输出日志
        log_window = tk.Tk()
        log_window.title('Log output')
        stream_handler_box = LoggerBox(log_window, width=50, height=20)
        stream_handler_box.pack(fill=tk.BOTH)
        self.__log.addHandler(logging.StreamHandler(stream_handler_box))
        threading.Thread(target=self.__main)
        log_window.mainloop()

    def __init(self):
        # 设置标题
        self.__window.title(self.__class__.__name__)
        # 设置程序图标
        self.__window.iconbitmap('../data/sun.ico')
        # 设置程序窗口大小
        self.__window.geometry('400x120')

        # bin文件选择
        tk.Label(self.__window, text="Bin文件 ").grid(row=0, column=0, padx=10, pady=20)
        tk.Entry(self.__window, width=40, textvariable=self.__bin_filename).grid(row=0, column=1)
        tk.Button(self.__window, text='选择文件', command=self.__select_file).grid(row=1, column=1, padx=80, sticky="e")

        # 启动按钮
        tk.Button(self.__window, text='启动更新', command=self.__start_up).grid(row=1, column=1, sticky="e")

    def write_log(self, message: str):
        self.__log.info(message)

    def mainloop(self):
        self.__init()
        self.__window.mainloop()


if __name__ == '__main__':
    framework = SampleAppFramework()
    framework.mainloop()
