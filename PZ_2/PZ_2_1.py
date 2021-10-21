# Дано двузначное число. Вывести число, полученное при перестановке цифр исходного числа
def my_work(self):  # создаю функцию, чтобы в дальнейшем ее автоматизировать
    number = (input('Введите двузначное число: '))
    while type(number) != int:  # дословно: цикл выполняется пока не равен int
        try:  # обработка будет выполняться, если число int
            number = int(number)
            if 9 < number < 100:  # Выполнение поставленной задачи
                number1 = number % 10
                number2 = number // 10
                answer = number1 * 10 + number2
                print('таков ответ: ', answer)  # ответ
            else:
                print('Неправильно. Введите ДВУЗНАЧНОЕ число')
        except ValueError:
            print('Не балуйся, а напиши лучше ДВУЗНАЧНОЕ число')
            break


while True:  # автоматизация функции
    print(my_work(None))