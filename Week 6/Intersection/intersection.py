def Intersection(A, B):
    C = []
    if len(A) > len(B):
        A, B = B, A
    for i in range(len(A)):
        for j in range(len(B)):
            if A[i] == B[j]:
                C.append(A[i])
                break
            elif A[i] < B[j]:
                break
    return C


A = list(map(int, input().split()))
B = list(map(int, input().split()))
print(*Intersection(A, B))
