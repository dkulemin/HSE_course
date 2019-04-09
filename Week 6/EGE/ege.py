fin = open('input.txt', 'r', encoding='utf8')
fout = open('output.txt', 'w', encoding='utf8')
n = int(fin.readline())
myList = []
for line in fin:
    tmp = line.split()
    score1 = int(tmp[-3])
    score2 = int(tmp[-2])
    score3 = int(tmp[-1])
    if score1 >= 40 and score2 >= 40 and score3 >= 40:
        myList.append(score1 + score2 + score3)
if len(myList) == 0:
    print(1, file=fout)
elif n >= len(myList):
    print(0, file=fout)
elif myList.count(max(myList)) > n:
    print(1, file=fout)
else:
    myList.sort(reverse=True)
    i = n - 1
    while myList[i] == myList[n]:
        i -= 1
    else:
        print(myList[i], file=fout)
fin.close()
fout.close()
