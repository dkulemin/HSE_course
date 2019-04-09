def placeInRanks(A, x):
    for i in range(len(A)):
        if x > A[i]:
            return i + 1
    return len(A) + 1


A = list(map(int, input().split()))
x = int(input())
print(placeInRanks(A, x))
