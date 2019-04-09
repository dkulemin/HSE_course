A = list(map(int, input().split()))
min_a = max(A)
for a in A:
    if a < min_a and a % 2 == 1:
        min_a = a
print(min_a)
