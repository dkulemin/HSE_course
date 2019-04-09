def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)


def ReduceFraction(n, m):
    return n // gcd(n, m), m // gcd(n, m)


n, m = ReduceFraction(int(input()), int(input()))
print(n, m)
