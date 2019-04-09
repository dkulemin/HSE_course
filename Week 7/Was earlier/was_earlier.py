myList = list(input().split())
mySet = set()
for num in myList:
    if num in mySet:
        print('YES')
    else:
        print('NO')
        mySet.add(num)
