def sum(a, b):
    a += 1
    if b != 0:
        return sum(a, b - 1)
    return a - 1


print(sum(int(input()), int(input())))
