s = input()
i = 0
while i < len(s):
    if i % 3 != 0:
        print(s[i], end='')
    i += 1
