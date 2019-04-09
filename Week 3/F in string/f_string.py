s = input()
first = s.find('f')
if first != -1:
    second = len(s) - s[::-1].find('f') - 1
    print(first)
    if second != first:
        print(second)
