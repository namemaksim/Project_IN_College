import random
Matrix = [[random.randint(0, 2) for j in range(6)] for i in range(7)]  # создаем матрицу
print(*Matrix, sep='\n')  # выводим матрицу
for i in range(7):   # решение задачи
    if i % 2 == 1:
        a = 0
        for j in Matrix[i]:
            a += j
        print(f'Среднее арифметическое нечетной строки {Matrix[i]}: ', a/6)  # ответ
