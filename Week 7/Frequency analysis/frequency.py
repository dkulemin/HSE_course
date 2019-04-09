import sys
words = {}
for line in sys.stdin.readlines():
    for i in line.split():
        words[i] = words.get(i, 0) + 1
output = []
for key, value in words.items():
    output.append((value, key))
output.sort(key=lambda value: (-value[0], value[1]))
for now in output:
    print(now[1])
