def power(a, n):
    if n == 0:
        if a == 0:
            return 0
        return 1
    elif n > 0:
        powerA = 1
        while n != 0:
            powerA *= a
            n -= 1
        return powerA
    elif n < 0:
        powerA = 1
        while n != 0:
            powerA *= a
            n += 1
        return 1 / powerA


print(power(float(input()), int(input())))
