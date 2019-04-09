for i in range(1, int(input()) + 1):
    myTuple = tuple(range(1, i + 1))
    for j in myTuple:
        print(j, end='')
    print()
