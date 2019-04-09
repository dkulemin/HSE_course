fin = open('input.txt', 'r', encoding='utf8')
avr9 = 0
avr10 = 0
avr11 = 0
i9 = 0
i10 = 0
i11 = 0
for line in fin:
    lst = list(line.split())
    if lst[2] == '9':
        avr9 += int(lst[3])
        i9 += 1
    if lst[2] == '10':
        avr10 += int(lst[3])
        i10 += 1
    if lst[2] == '11':
        avr11 += int(lst[3])
        i11 += 1
fin.close()
print(avr9 / i9, avr10 / i10, avr11 / i11)
