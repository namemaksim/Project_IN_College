def Fibonachi(n, L):
    count = len(L)

    if len(L)<2:
        return []

    num1 = L[count-2]
    num2 = L[count-1]

    if (num1+num2) < n:
        L = L + [num1+num2]
        return Fibonachi(n, L)
    else:
        return L


print(Fibonachi(100, [0, 2]))
