import math

n = int(input())
A = list(map(int, input().split()))
x = int(input())
B = []
for a in A:
    B.append(math.fabs(x - a))
print(A[B.index(min(B))])
