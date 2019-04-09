def distance(x1, y1, x2, y2):
    sumSquares = (x2 - x1)**2 + (y2 - y1)**2
    return sumSquares**(1/2)


def perimeter(x1, y1, x2, y2, x3, y3):
    a = distance(x1, y1, x2, y2)
    b = distance(x2, y2, x3, y3)
    c = distance(x3, y3, x1, y1)
    return a + b + c


sum = perimeter(float(input()), float(input()),
                float(input()), float(input()),
                float(input()), float(input()))
print('{0:.6f}'.format(sum))
