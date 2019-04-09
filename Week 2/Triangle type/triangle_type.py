a = int(input())
b = int(input())
c = int(input())
if a > b and a > c:
    tmp = a
    a = c
    c = tmp
elif b > a and b > c:
    tmp = b
    b = c
    c = tmp
if (a + b) > c:
    if a**2 + b**2 == c**2:
        print('rectangular')
    elif a**2 + b**2 > c**2:
        print('acute')
    else:
        print('obtuse ')
else:
    print('impossible')
