def minus(n):
    if len(n) == 0:
        return 0
    else:
        count = minus(n[1:])
        if n[0]<0:
            count = count + 1

        return count


L = [-2, 3, -8, -11, -4, 6]

print("n = ", minus(L))