def CountSort(A):
    grades = [0] * 101
    for i in A:
        grades[i] += 1
    for now in range(101):
        print((str(now) + ' ') * grades[now], end='')


myList = list(map(int, input().split()))
CountSort(myList)
