k = int(input())
n = 1
count = 0
while n <= k:
    reverse = ''
    i = n
    while i // 10 != 0:
        reverse += str(i % 10)
        i //= 10
    reverse += str(i)
    if n == int(reverse):
        count += 1
    n += 1
print(count)
