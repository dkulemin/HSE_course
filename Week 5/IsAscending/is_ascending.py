def IsAscending(A):
    i = 1
    while i < len(A):
        if A[i] <= A[i - 1]:
            return 'NO'
        i += 1
    return 'YES'


print(IsAscending(list(map(int, input().split()))))
