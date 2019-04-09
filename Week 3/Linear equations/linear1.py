a, b, c = float(input()), float(input()), float(input())
d, e, f = float(input()), float(input()), float(input())
"""
ax+by=e
cx+dy=f
"""
if a == 0:
    y = e / b
    if c == 0:
        x = y
    else:
        x = (f - d * y) / c
elif b == 0:
    x = e / a
    if d == 0:
        y = x
    else:
        y = (f - c * x) / d
elif c == 0:
    y = f / d
    if a == 0:
        x = y
    else:
        x = (e - b * y) / a
elif d == 0:
    x = f / c
    if b == 0:
        y = x
    else:
        y = (e - a * x) / b
else:
    y = (f - (c * e / a)) / (d - (b * c / a))
    x = (f - d * y) / c
print(x, y)
