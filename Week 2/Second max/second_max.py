n = -1
maxNum = 0
maxSecNum = 0
while n != 0:
    if n == -1:
        n = int(input())
        maxNum = n
    else:
        n = int(input())
        if n > maxNum:
            maxSecNum = maxNum
            maxNum = n
        elif maxSecNum < n <= maxNum:
            maxSecNum = n
print(maxSecNum)
