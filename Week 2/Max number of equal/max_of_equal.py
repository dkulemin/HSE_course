n = int(input())
count = 1
maxCount = 1
while n != 0:
    last = n
    n = int(input())
    if n == last:
        count += 1
        if count > maxCount:
            maxCount = count
    else:
        count = 1
print(maxCount)
