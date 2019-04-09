def distance(x1, y1, x2, y2):
    sumSquares = (x2 - x1)**2 + (y2 - y1)**2
    return sumSquares**(1/2)


print(distance(float(input()), float(input()), float(input()), float(input())))
