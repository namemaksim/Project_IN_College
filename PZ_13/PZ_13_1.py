# Проверить есть ли в последовательности целых N чисел число K
from random import randint  # импортирую модуль для рандомной последовательности
k = int(input('Введите число, которое хотите проверить: '))
list1 = [randint(-30, 30) for i in range(30)]  # создаю рандомный список с органичениями
y = filter(lambda x: x == k, list1)  # решение задачи
print(f'Цифра, введённая вами есть в последовательности \n{list1}' if list(y) == [k]  # вывод ответа
      else f'Цифра, введённая вами отсутствует в последовательности \n{list1}')
