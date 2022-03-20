import random
Matrix = [[random.randint(-20,40) for j in range(6)] for i in range(7)]  # создаем матрицу
print(*Matrix, sep='\n')  # выводим ее
a = []
for i in Matrix:  # решение задачи
    for j in i:
        if j % 4 == 0:
            a.append(j)
try:
    print('Ответ таков: ', max(a))  # выводим ответ
except ValueError:
    print("Нету числа кратного 4")

