n = int(input())
a = list(map(int, input().split()))
a.sort()
shoe = 0
index = 0
count = 0
for i in a:
    if i >= n:
        count = 1
        index = a.index(i)
        shoe = i
        break
for i in range(index + 1, len(a)):
    if a[i] - shoe >= 3:
        count += 1
        shoe = a[i]
print(count)
