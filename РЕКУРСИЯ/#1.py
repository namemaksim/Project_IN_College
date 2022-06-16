def summa(n):
    if len(n) == 0:
        return 0
    else:
        summ = summa(n[1:]) + n[0]
        return summ


L = [2, 367, 865, 1341, 4, 6]

print("summa = ", summa(L))