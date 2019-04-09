fin = open('input.txt')
words = []
A = {}
for now in [i.split() for i in fin.readlines()]:
    words.extend(now)
for i in words:
    A[i] = A.get(i, 0) + 1
    print(A[i] - 1, end=' ')
