a = int(input())
b = int(input())
c = int(input())
odd = a % 2 == 1 or b % 2 == 1 or c % 2 == 1
even = a % 2 == 0 or b % 2 == 0 or c % 2 == 0
if odd and even:
    print('YES')
else:
    print('NO')
