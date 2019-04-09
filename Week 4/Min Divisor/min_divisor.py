def MinDivisor(n):
    i = 2
    sqrtN = n**(1/2)
    while i <= sqrtN:
        if n % i == 0:
            return i
        i += 1
    return n


print(MinDivisor(int(input())))
