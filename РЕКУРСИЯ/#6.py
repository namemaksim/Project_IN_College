# Рекурсия. Возведение числа x в степень y

def Poww(x, y):
    if y > 0:
        return x * Poww(x, y-1)
    else:
        return 1


x = int(input("Введите первое число: "))
y = int(input("Введите второе число: "))
res = Poww(x, y)
print("Результат: ", res)