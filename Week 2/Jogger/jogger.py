x, y = int(input()), int(input())
days = 1
while x < y:
    x += (x * 10) / 100
    days += 1
print(days)
