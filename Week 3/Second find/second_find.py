s = input()
first = s.find('f')
if first != -1:
    second = s.find('f', first + 1)
    print(second)
else:
    print(-2)
