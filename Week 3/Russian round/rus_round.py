import math

x = float(input())
if x % 1 < 0.5:
    print(math.floor(x))
else:
    print(math.ceil(x))
