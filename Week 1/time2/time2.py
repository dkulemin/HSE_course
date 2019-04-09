sec = int(input())
h = sec % 86400 // 3600
m = sec % 86400 % 3600 // 60
s = sec % 86400 % 3600 % 60
mm = str(m // 10) + str(m % 10)
ss = str(s // 10) + str(s % 10)
print(h, mm, ss, sep=':')
