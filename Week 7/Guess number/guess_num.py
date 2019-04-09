n = int(input())
resSet = set()
noSet = set()
while True:
    tmp = input()
    if tmp == 'HELP':
        break
    else:
        tmpSet = set(map(int, tmp.split()))
        answer = input()
        if answer == 'YES':
            if len(resSet) == 0:
                resSet = tmpSet
            else:
                resSet &= tmpSet
        if answer == 'NO':
            resSet -= tmpSet
            noSet |= tmpSet
if len(resSet) != 0:
    print(*sorted(resSet))
else:
    print(*sorted({i for i in range(1, n + 1)} - noSet))
