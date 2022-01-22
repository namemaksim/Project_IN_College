# 2. Дан номер года. Определить количество дней в этом году(високосный или нет). Високосным считается год, делящийся
# на 4, за исключением тех годов, которые делятся на 100 и не делятся на 400
import tkinter as tk
from tkinter import *

root = Tk()  # создаю окно
root.geometry('500x500')
root['bg'] = 'Gray'
root.title('Високосный год или нет')
root.resizable(False, False)


def button_entry():  # решение задачи
    year = entry.get()
    year = int(year)
    if year < 0:
        tk.Label(text=f'Вы ввели отрицательный год ( {year} )', bg='Gray', fg='Black',
                 font=('Enta', '12', 'bold'), padx=30, width=30).place(x=80, y=150)
    elif year > 0 and year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        tk.Label(text=f"Високосный год, ( {year} ), В нём 366 дней", bg='Gray', fg='Black',
                 font=('Enta', '12', 'bold'), padx=30, width=30).place(x=80, y=150)
    else:
        tk.Label(text=f"Не високосный год, ( {year} ), В нём 365 дней", bg='Gray', fg='Black',
                 font=('Enta', '12', 'bold'), padx=30, width=30).place(x=80, y=150)

# и далее - создание кнопок, полей, текста


entry = tk.Entry(root, bg='White', fg='Black', font=('Enta', '14'))
entry.place(x=167, y=49)

button1 = tk.Button(root, text='Проверить', fg='Gray', bg='#2e3138', command=button_entry)
button1.place(x=150, y=80)

button2 = tk.Button(root, text='Очистить', fg='Gray', bg="#2e3138", command=lambda: entry.delete(0, 'end'))
button2.place(x=230, y=80)

tk.Label(text='Данная программа позволяет определить является ли год високосным или нет', bg='Gray', fg='Black',
         font=('Enta', '9', 'bold')).place(x=10, y=20)
tk.Label(text='Введите год: ', bg='White', fg='Black', font=('Enta', '12', 'bold')).place(x=50, y=50)

root.mainloop()  # запуск программы
