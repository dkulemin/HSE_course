n = int(input())
k = 1
a = 2
if n == 1:
    print(0)
else:
    while a < n:
        a *= 2
        k += 1
    print(k)
