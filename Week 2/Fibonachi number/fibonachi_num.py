a = int(input())
if a == 0 or a == 1:
    print(a)
else:
    fOfN = 1
    nMinTwo = 0
    nMinOne = 1
    i = 1
    while fOfN < a:
        fOfN = nMinOne + nMinTwo
        nMinTwo = nMinOne
        nMinOne = fOfN
        i += 1
    if fOfN == a:
        print(i)
    else:
        print(-1)
