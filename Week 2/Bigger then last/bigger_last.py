n = int(input())
count = 0
while n != 0:
    last = n
    n = int(input())
    if n > last:
        count += 1
print(count)
