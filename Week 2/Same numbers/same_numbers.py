a, b, c = int(input()), int(input()), int(input())
count = 0
if a == b or a == c:
    count += 2
    if b == c:
        count += 1
elif b == c:
    count += 2
print(count)
