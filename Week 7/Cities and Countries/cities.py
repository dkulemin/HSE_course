n = int(input())
cityDict = {}
for _ in range(n):
    tmp = input().split()
    for i in tmp[1:]:
        cityDict[i] = tmp[0]
m = int(input())
output = []
for _ in range(m):
    output.append(cityDict[input()])
print(*output, sep='\n')
