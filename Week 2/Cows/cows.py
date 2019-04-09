n = int(input())
if n // 10 == 1:
    print(n, 'korov')
elif n % 10 == 1:
    print(n, 'korova')
elif n % 10 >= 5 or n % 10 == 0:
    print(n, 'korov')
else:
    print(n, 'korovy')
