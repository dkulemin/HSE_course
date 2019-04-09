import sys
wordSet = set()
for line in sys.stdin.readlines():
    for i in line.split():
        wordSet.add(i)
print(len(wordSet))
