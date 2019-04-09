def twoPosOrNeg(A):
    isPos = True
    if A[0] < 0:
        isPos = False
    for i in range(1, len(A)):
        if (A[i] < 0 and not isPos) or (A[i] >= 0 and isPos):
            return str(A[i - 1]), str(A[i])
        else:
            if A[i] < 0:
                isPos = False
            else:
                isPos = True
    return ''


output = twoPosOrNeg(list(map(int, input().split())))
print(' '.join(output))
