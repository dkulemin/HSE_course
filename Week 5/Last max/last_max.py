A = list(map(int, input().split()))
maxA = A[0]
index = 0
i = 0
for a in A:
    if a >= maxA:
        maxA = a
        index = i
    i += 1
print(maxA, index)
