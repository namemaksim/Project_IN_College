# https://soulcompas.com/wp-content/uploads/2020/06/html5-admin-template-free.jpg
from tkinter import *
import tkinter as tk

root = Tk()  # создаю окно
root.title('Вариант 13')
root.geometry('612x779')
root.resizable(False, False)
root['bg'] = '#2e3138'


def top(self):  # решение задачи
    tk.Label(self, text='Xtra', font=('Enta', '25', 'bold'), fg='#9197a4', bg='#2e3138').place(x=232, y=5)
    tk.Label(self, text='Form', font=('Enta', '25', 'bold'), fg='#349bc7', bg='#2e3138').place(x=298, y=5)
    tk.Label(self, text='Bootstrap 3 Xtra Form', font=('Enta', '9'), fg='#8d8f9a', bg='#2e3138').place(x=245, y=50)
    tk.Label(self, text='Sign up', font=('Enta', '10'), fg='#8c909a', bg='#454953', width=40, padx=15, height=2).place(
        x=130, y=95)
    tk.Label(self, text='Username', font=('Enta', '10', 'bold'), fg='#90909a', bg='#24252a').place(x=160, y=145)
    tk.Entry(self, fg='#8b8e95', bg='#444852', bd=0, font=('Enta', '15'), width=26).place(x=164, y=175)

    tk.Label(self, text='Email', font=('Enta', '10', 'bold'), fg='#90909a', bg='#24252a').place(x=160, y=210)
    tk.Entry(self, fg='#8b8e95', bg='#444852', bd=0, font=('Enta', '15'), width=26).place(x=164, y=240)

    tk.Label(self, text='Password', font=('Enta', '10', 'bold'), fg='#90909a', bg='#24252a').place(x=160, y=290)
    tk.Entry(self, fg='#8b8e95', bg='#444852', bd=0, font=('Enta', '15'), width=26).place(x=164, y=320)

    tk.Label(self, text='Retype password', font=('Enta', '10', 'bold'), fg='#90909a', bg='#24252a').place(x=160, y=360)
    tk.Entry(self, fg='#8b8e95', bg='#444852', bd=0, font=('Enta', '15'), width=26).place(x=164, y=390)

    var1 = BooleanVar()
    var1.set(0)
    tk.Checkbutton(self, text='Accept the terms and policies', bd=0, onvalue=1, offvalue=0, variable=var1,
                   fg='#90909a', bg='#24252a', activebackground='#24252a').place(x=160, y=450)

    tk.Button(self, text='SIGN UP', fg='White', bg='#2ba6d0', font=('Enta', '12', 'bold'), bd=0,
              activebackground='#2ba6d0').place(x=164, y=490)

    tk.Label(self, text='------------------------------------------', fg='#2d2e33', bg='#24252a').place(x=164, y=540)

    tk.Button(self, text='Already have an account?', fg='White', bg='#24252a', bd=0,
              activebackground='#24252a').place(x=240, y=570)

    tk.Button(self, text='SIGN IN', font=('Enta', '13', 'bold'), fg='White', bg='#525863',
              width=28, bd=0, activebackground='#525863').place(x=164, y=600)

    tk.Label(self, text='Built with', font=('Enta', '9', 'bold'), fg='#8d8f9a', bg='#2e3138').place(x=200, y=745)
    tk.Label(self, text='Bootstrap 3', font=('Enta', '9', 'bold'), fg='#349bc7', bg='#2e3138').place(x=255, y=745)
    tk.Label(self, text='| Made by', font=('Enta', '9', 'bold'), fg='#8d8f9a', bg='#2e3138').place(x=325, y=745)
    tk.Label(self, text='Aydev', font=('Enta', '9', 'bold'), fg='#349bc7', bg='#2e3138').place(x=383, y=745)


def center(self):  # рисую фигуры для дизайна
    canvas = Canvas(self, width=612, height=779, bg='#2e3138', highlightthickness=3, highlightbackground="White")
    canvas.create_rectangle(130, 133, 483, 670, fill="#24252a", outline='#24252a')
    canvas.pack()


def close():  # обработка закрытия
    root.destroy()
    root.quit()


center(None)
top(None)
root.mainloop()  # запуск программы
