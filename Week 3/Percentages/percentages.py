p = int(input())
x = int(input())
y = int(input())
deposit = x * 100 + y
profit = deposit + int(deposit / 100 * p)
print(profit // 100, profit % 100)
