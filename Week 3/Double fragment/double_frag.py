s = input()
first = s.find('h')
second = len(s) - s[::-1].find('h') - 1
print(s[:first + 1], end='')
print(s[first + 1:second], end='')
print(s[first + 1:second], end='')
print(s[second:])
