import random
Matrix = [[random.randint(0, 2) for j in range(6)] for i in range(7)]
print(*Matrix, sep='\n')
for i in range(7):
    if i % 2 == 1:
        a = 0
        for j in Matrix[i]:
            a+= j
        print(f'Среднее арифметическое нечетной строки {Matrix[i]}: ', a/6)
