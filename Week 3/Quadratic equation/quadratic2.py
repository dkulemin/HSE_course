import math

a = float(input())
b = float(input())
c = float(input())
if a == b == c == 0:
    print(3)
elif a == 0 and b != 0:
    x = -c / b
    print(1, x)
elif a == b == 0 and c != 0:
    print(0)
else:
    D = b**2 - 4 * a * c
    if D < 0:
        print(0)
    elif D == 0:
        x = -b / (2 * a)
        print(1, x)
    elif D > 0:
        x1 = (-b - math.sqrt(D)) / (2 * a)
        x2 = (-b + math.sqrt(D)) / (2 * a)
        if x2 > x1:
            print(2, x1, x2)
        else:
            print(2, x2, x1)
