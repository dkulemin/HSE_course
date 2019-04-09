A = list(map(int, input().split()))
min_a = 1000
for a in A:
    if 0 < a < min_a:
        min_a = a
print(min_a)
