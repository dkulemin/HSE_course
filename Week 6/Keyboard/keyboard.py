def KeyPressCount(n, c, p):
    grades = [0] * n
    for i in p:
        grades[i - 1] += 1
    for i in range(n):
        if c[i] < grades[i]:
            print('YES')
        else:
            print('NO')


n = int(input())
c = list(map(int, input().split()))
k = int(input())
p = list(map(int, input().split()))
KeyPressCount(n, c, p)
