def placeChange(A, l):
    for i in range(0, l, 2):
        A[i], A[i + 1] = A[i + 1], A[i]


A = input().split()
if len(A) % 2 == 0:
    placeChange(A, len(A))
else:
    placeChange(A, len(A) - 1)
print(*A)
