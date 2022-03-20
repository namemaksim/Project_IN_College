import random
Matrix = [[random.randint(-20,40) for j in range(6)] for i in range(7)]
print(*Matrix, sep='\n')
a = []
for i in range(7):
    a.append(max(Matrix[i]))
print(max(a))
