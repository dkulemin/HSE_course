s = input()
first = s.find('h')
last = s.rfind('h')
frag = s[first + 1:last]
s = s[:first + 1] + frag.replace('h', 'H') + s[last:]
print(s)
