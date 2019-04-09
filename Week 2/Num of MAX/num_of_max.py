n = int(input())
count = 1
maxNum = n
while n != 0:
    n = int(input())
    if n > maxNum:
        maxNum = n
        count = 1
    elif n == maxNum:
        count += 1
print(count)
