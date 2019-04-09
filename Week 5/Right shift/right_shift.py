A = input().split()
A.insert(0, A.pop(-1))
print(*A)
