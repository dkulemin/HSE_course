s, n = map(int, input().split())
a = []
for i in range(n):
    a.append(int(input()))
a.sort()
i = 0
count = 0
while i < len(a):
    if s - a[i] >= 0:
        s -= a[i]
        count += 1
        i += 1
    else:
        break
print(count)
