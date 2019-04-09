def firstMax(A):
    maxA = A[0]
    index = 0
    for i in range(1, len(A)):
        if A[i] > A[i - 1]:
            maxA = A[i]
            index = i
    return str(maxA), str(index)


output = firstMax(list(map(int, input().split())))
print(' '.join(output))
