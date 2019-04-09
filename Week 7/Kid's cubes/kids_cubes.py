fin = open('input.txt', 'r', encoding='utf8')
fout = open('output.txt', 'w', encoding='utf8')
n, m = map(int, fin.readline().split())
anya = {int(fin.readline()) for _ in range(n)}
borya = {int(fin.readline()) for _ in range(m)}
fin.close()
intersectSet = anya & borya
anyaOnly = anya.difference(intersectSet)
boryaOnly = borya.difference(intersectSet)
print(len(intersectSet), file=fout)
print(*sorted(intersectSet), file=fout)
print(len(anyaOnly), file=fout)
print(*sorted(anyaOnly), file=fout)
print(len(boryaOnly), file=fout)
print(*sorted(boryaOnly), file=fout)
fout.close()
