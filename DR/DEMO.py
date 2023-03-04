import os
from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image
import subprocess
import sys
value_one = 0
value_two = 0
value_three = 0
si = subprocess.STARTUPINFO()
def The_first_block_one():
    global value_one
    if value_one==0:
        value_one += 1
        subprocess.Popen(r"lora_gui_run.bat", creationflags=subprocess.CREATE_NEW_CONSOLE,startupinfo=si)
    else:
        error_one()

def The_second_block_one():
    global value_two
    if value_two==0:
        value_two += 1
        subprocess.Popen(r"Okohya_ss_run.bat", creationflags=subprocess.CREATE_NEW_CONSOLE,startupinfo=si)
    else:
        error_one()

def The_third_block_one():
    filepath = 'venv'
    if not os.path.isdir(filepath):
        error_two()
    else:
        subprocess.Popen(r"setup.bat", creationflags=subprocess.CREATE_NEW_CONSOLE,startupinfo=si)

def The_Fourth_block_one():
    os.system("taskkill /F /IM cmd.exe")
    os.system("taskkill /F /IM python.exe")
    global value_one
    global value_two
    global value_three
    value_one = 0
    value_two = 0
    value_three = 0

def The_fifth_block_one():
    buer = (os.system("conda"))
    if buer == 0:
        subprocess.Popen(r"venv_setup.bat", creationflags=subprocess.CREATE_NEW_CONSOLE,startupinfo=si)
    else:
        error_three()
def The_sixth_block_one():
    sys.exit(0)

def The_Seventh_block_one():
    os.system("fastgithub_win-x64\FastGithub.UI.exe")

def The_Eightth_block_one():
    global value_three
    if value_three == 0:
        value_three += 1
        subprocess.Popen(r"fastTagger_run.bat", creationflags=subprocess.CREATE_NEW_CONSOLE, startupinfo=si)
    else:
        error_one()

def open():
    os.startfile(start_directory)

def start():
    window = tk.Tk()
    window.title('LORA and DreamBooth Train')
    window.geometry('600x900')
    imgpath = r"background.gif"
    img = Image.open(imgpath)
    photo = ImageTk.PhotoImage(img)
    canvas = tk.Canvas(window, width=1000, height=1000, bd=0, highlightthickness=0)
    canvas.create_image(300, 524, image=photo)
    canvas.pack()
    one = tk.Button(window, text='只启动LORA训练', font=('Arial', 12), width=10, height=1, relief="raised",
                    command=The_first_block_one)
    one.pack()
    canvas.create_window(130, 40, width=250, height=30,
                         window=one)
    two = tk.Button(window, text='启动DreamBooth含有LORA', font=('Arial', 12), width=10, height=1, relief="raised",
                    command=The_second_block_one)
    two.pack()
    canvas.create_window(130, 90, width=250, height=30, window=two)
    three = tk.Button(window, text='启动安装程序', font=('Arial', 12), width=10, height=1, relief="raised",
                      command=The_third_block_one)
    three.pack()
    canvas.create_window(130, 190, width=250, height=30, window=three)
    four = tk.Button(window, text='关闭所有已启动的训练', font=('Arial', 12), width=10, height=1, relief="raised",
                     command=The_Fourth_block_one)
    four.pack()
    canvas.create_window(130, 140, width=250, height=30, window=four)
    five = tk.Button(window, text='安装虚拟环境', font=('Arial', 12), width=10, height=1, relief="raised",
                     command=The_fifth_block_one)
    five.pack()
    canvas.create_window(130, 240, width=250, height=30, window=five)
    six = tk.Button(window, text='启动github加速', font=('Arial', 12), width=10, height=1, relief="raised",
                    command=The_Seventh_block_one)
    six.pack()
    canvas.create_window(130, 290, width=250, height=30, window=six)

    Seven = tk.Button(window, text='开启图片标注软件(未开放)', font=('Arial', 12), width=10, height=1, relief="raised",
                     command=The_Eightth_block_one)
    Seven.pack()
    canvas.create_window(130, 340, width=250, height=30, window=Seven)

    Eight = tk.Button(window, text='打开标注图片存放文件(未开放)', font=('Arial', 12), width=10, height=1, relief="raised",
                      command=open)
    Eight.pack()
    canvas.create_window(130, 390, width=250, height=30, window=Eight)
    nine = tk.Button(window, text='退出程序', font=('Arial', 12), width=10, height=1, relief="raised",
                      command=The_sixth_block_one)
    nine .pack()
    canvas.create_window(130, 440, width=250, height=30, window=nine)

    window.mainloop()

def error_one():
    window = Toplevel()
    window.title('警告')
    def exit():
        window.destroy ()
    one = tk.Button(window, text='你已经开启了训练\n点我退出警告界面', font=('Arial', 12), width=25, height=20, relief="raised",
                    command=exit)
    one.pack()

def error_two():
    window = Toplevel()
    window.title('警告')

    def exit():
        window.destroy()
    two = tk.Button(window, text='无法运行安装指令\nanaconda创建环境失败\n点我退出警告界面\n查看第一步是否运行正常', font=('Arial', 12), width=25, height=20,relief="raised",
                    command=exit)
    two.pack()

def error_three():
    window = Toplevel()
    window.title('警告')

    def exit():
        window.destroy()
    two = tk.Button(window, text='无法运行指令\nanaconda环境变量出错\nconda命令无法识别\n请检查环境变量', font=('Arial', 12), width=25, height=20,relief="raised",
                    command=exit)
    two.pack()
start_directory = r'Label the catalog'
start()
