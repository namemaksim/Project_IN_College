from math import sqrt
a1 = 7
b1 = 2
c1 = 8


def triangle_perimeter(a=a1, b=b1, c=c1):
    print("периметр треугольника")
    return a + b + c


def triangle_area(a=a1, b=b1, c=c1):
    print("площадь треугольника")
    p = (triangle_perimeter()) / 2
    return sqrt(p*(p - a)*(p - b) * (p - c))