A = list(map(int, input().split()))
min_a = A.index(min(A))
max_a = A.index(max(A))
A[min_a], A[max_a] = A[max_a], A[min_a]
print(*A)
