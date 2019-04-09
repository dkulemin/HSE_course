import sys
text = {}
myList = []
for line in sys.stdin.readlines():
    for i in line.split():
        text[i] = text.get(i, 0) + 1
for key, value in text.items():
    myList.append((value, key))
myList.sort(key=lambda word: (-word[0], word[1]))
print(myList[0][1])
