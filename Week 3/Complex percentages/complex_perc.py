p = int(input())
x = int(input())
y = int(input())
k = int(input())
profit = x * 100 + y
i = 1
while i <= k:
    profit += int(profit / 100 * p)
    i += 1
print(profit // 100, profit % 100)
