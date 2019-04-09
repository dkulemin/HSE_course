n = -1
count = 0
maxCount = 0
monotony = 0
while n != 0:
    if n == -1:
        n = int(input())
        count = 1
        maxCount = 1
    else:
        last = n
        n = int(input())
        if n > last and n != 0:
            if monotony == 1:
                count += 1
                if count > maxCount:
                    maxCount = count
            else:
                count = 2
                monotony = 1
                if count > maxCount:
                    maxCount = count
        elif n < last and n != 0:
            if monotony == -1:
                count += 1
                if count > maxCount:
                    maxCount = count
            else:
                count = 2
                monotony = -1
                if count > maxCount:
                    maxCount = count
        else:
            count = 1
            monotony = 0
            if count > maxCount:
                maxCount = count
print(maxCount)
