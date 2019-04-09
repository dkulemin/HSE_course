A = list(map(int, input().split()))
count = 1
for i in range(1, len(A)):
    if A[i] > A[i - 1]:
        count += 1
print(count)
