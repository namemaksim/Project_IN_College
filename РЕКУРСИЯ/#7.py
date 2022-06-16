# Рекурсивная функция. Определить максимальный элемент списка

def Elem_MaxList(L):
    if len(L) > 1:
        Max = Elem_MaxList(L[1:])

        if L[0] < Max:
            return Max
        else:
            return L[0]

    if len(L) == 1:
        return L[0]


L = [5050, 320, 687, 152, 146]
res = Elem_MaxList(L)
print("Результат: ", res)