def power(a, n):
    if n == 0:
        if a == 0:
            return 0
        return 1
    if n % 2 == 0:
        return (a**2)**(n / 2)
    else:
        return a * power(a, n - 1)


print(power(float(input()), int(input())))