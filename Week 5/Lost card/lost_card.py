n = int(input())
summ1 = 0
summ2 = 0
for i in range(1, n + 1):
    summ1 += i
for _ in range(n - 1):
    summ2 += int(input())
print(summ1 - summ2)
