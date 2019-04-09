def f():
    a = int(input())
    if a != 0:
        f()
        print(a)
        return None
    print(a)


f()
