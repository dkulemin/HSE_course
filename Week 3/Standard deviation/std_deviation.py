import math

n = -1
summ1 = 0
summ2 = 0
count = 0
while n != 0:
    n = int(input())
    if n != 0:
        summ1 += n**2
        summ2 += n
        count += 1
print(math.sqrt((summ1 - (summ2**2 / count)) / (count - 1)))
