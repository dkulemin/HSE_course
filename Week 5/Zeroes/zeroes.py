n = int(input())
zeroes = 0
for _ in range(n):
    if int(input()) == 0:
        zeroes += 1
print(zeroes)
