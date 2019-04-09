n = int(input())
while n // 10 != 0:
    print(n % 10, end='')
    n //= 10
print(n)
