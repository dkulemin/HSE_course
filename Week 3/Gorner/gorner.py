n = int(input())
x = float(input())
a = float(input())
summ = a * x
while n > 0:
    if n == 1:
        a = float(input())
        summ += a
    else:
        a = float(input())
        summ = (summ + a) * x
    n -= 1
print(round(summ, 2))
