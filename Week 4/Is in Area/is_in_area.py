def IsPointInArea(x, y):
    """
    (x+1)^2 + (y-1)^2 = 4
    y = -x
    y = 2x + 2
    """
    sqrR = (x + 1)**2 + (y - 1)**2
    bool1 = -x <= y and 2*x + 2 <= y and sqrR <= 4
    bool2 = -x >= y and 2*x + 2 >= y and sqrR >= 4
    return bool1 or bool2


if IsPointInArea(float(input()), float(input())):
    print('YES')
else:
    print('NO')
