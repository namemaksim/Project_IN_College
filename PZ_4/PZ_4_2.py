# Дано целое число N (>1). Вывести наименьшее из целых чисел K, для которых сумма 1 + 2 +...+K
# будет больше или равна N, и саму эту сумму.
def my_work4_2(self):  # создаю функцию, чтобы в дальнейшем ее автоматизировать
    n = input('Введите целое положительное число: ')
    sum = 0
    k = 0
    while type(n) != int:  # проверка условий
        try:
            n = int(n)
            if n > 0:
                while n >= sum:  # решение самой задачи
                    k += 1
                    sum += k
                break
            else:
                print("Вы ввели отрицательное число - ",  n )
        except ValueError:
            print('Вы ввели не целое число -', n )
            n = input('Введите целое положительное число: ')
    k = sum // n
    print("Сумма чисел: ", sum, "Наименьшее целое число: ", k)  # вывод ответа

while True:  # автоматизация функции
    print(my_work4_2(None))