def Super_summa(n):
    summ = 0
    for i in n:
        if type(i) != list:
            summ = summ + i
        else:
            summ = summ + Super_summa(i)
    return summ


L = [-20, 67, 1671, [-4, 986, [52, [-567, 40]]]]

print("summa = ", Super_summa(L))