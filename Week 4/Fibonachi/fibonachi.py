def phib(n):
    if n == 0 or n == 1:
        return n
    else:
        return phib(n - 1) + phib(n - 2)


print(phib(int(input())))
