def f():
    a = int(input())
    if a != 0:
        return a + f()
    return 0


print(f())
