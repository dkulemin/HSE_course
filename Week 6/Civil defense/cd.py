import math

n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

answer = [0 for i in range(len(a))]
settles = [(a[i], i) for i in range(len(a))]
shelters = [(b[i], i) for i in range(len(b))]

settles.sort()
shelters.sort()

tmp = shelters[0]
for i in range(len(settles)):
    j = shelters.index(tmp) + 1
    stDist = settles[i][0]
    while j < len(shelters):
        shDist = shelters[j][0]
        if math.fabs(tmp[0] - stDist) > math.fabs(shDist - stDist):
            tmp = shelters[j]
        else:
            break
        j += 1
    answer[settles[i][1]] = tmp[1] + 1

print(*answer)
