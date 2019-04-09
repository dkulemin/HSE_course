n = int(input())
if n == 0 or n == 1:
    print(n)
else:
    i = 2
    nMinTwo = 0
    nMinOne = 1
    fOfN = -1
    while i <= n:
        fOfN = nMinOne + nMinTwo
        nMinTwo = nMinOne
        nMinOne = fOfN
        i += 1
    print(fOfN)
