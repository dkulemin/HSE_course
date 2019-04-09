s = input()
first = s.find('h')
second = len(s) - s[::-1].find('h') - 1
print(s[:first], end='')
print(s[second + 1:])
