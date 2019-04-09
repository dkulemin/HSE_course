s = input()
if len(s) > 1:
    print(s[0], end='')
    print(s[1:len(s) - 1].replace('', '*'), end='')
    print(s[-1])
else:
    print(s)
