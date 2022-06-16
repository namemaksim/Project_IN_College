# Рекурсия. Реверсирование числа
import math

def ReverseNumber(num):
    if num < 0:
        return -1

    if num == 0:
        return 0

    n_digit = 0
    num2 = num

    while num2 > 0:
        n_digit = n_digit + 1
        num2 = num2 // 10

    t = num % 10
    res = t * int(math.pow(10, n_digit-1))

    return res + ReverseNumber(num//10)


num = int(input("Введите последовательность, которую надо реверсировать: "))

print('Исходная последовательность: ', num)
rnum = ReverseNumber(num)
print('Риверсивная последовательность: ', rnum)