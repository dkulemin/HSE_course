n = int(input())
myList = []
for _ in range(n):
    tmpSet = set()
    m = int(input())
    for _ in range(m):
        tmpSet.add(input())
    myList.append(tmpSet)
resSet1 = myList[0]
resSet2 = set()
for l in myList:
    resSet1 &= l
    resSet2 |= l
print(len(resSet1))
print(*resSet1, sep='\n')
print(len(resSet2))
print(*resSet2, sep='\n')
