n = int(input())
print('+___ ' * n)
for i in range(n):
    print('|' + str(i + 1) + ' /', end=' ')
print()
print('|__\\ ' * n)
print('|    ' * n)
