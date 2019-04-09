import math

a = float(input())
b = float(input())
c = float(input())
D = b**2 - 4 * a * c
if D < 0:
    pass
elif D == 0:
    x = -b / (2 * a)
    print(x)
elif D > 0:
    x1 = (-b - math.sqrt(D)) / (2 * a)
    x2 = (-b + math.sqrt(D)) / (2 * a)
    if x2 > x1:
        print(x1, x2)
    else:
        print(x2, x1)
