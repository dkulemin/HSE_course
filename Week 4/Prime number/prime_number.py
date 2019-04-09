def IsPrime(n):
    i = 2
    sqrtN = n**(1/2)
    while i <= sqrtN:
        if n % i == 0:
            return 'NO'
        i += 1
    return 'YES'


print(IsPrime(int(input())))
