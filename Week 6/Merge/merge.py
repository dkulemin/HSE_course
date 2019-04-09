def merge(A, B):
    C = []
    i, j = 0, 0
    for _ in range(len(A) + len(B)):
        if i < len(A) and j < len(B):
            if A[i] < B[j]:
                C.append(A[i])
                i += 1
            else:
                C.append(B[j])
                j += 1
        elif i < len(A):
            C.extend(A[i:])
            return C
        elif j < len(B):
            C.extend(B[j:])
            return C
    return C


A = list(map(int, input().split()))
B = list(map(int, input().split()))
print(*merge(A, B))
