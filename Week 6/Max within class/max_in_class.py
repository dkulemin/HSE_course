fin = open('input.txt', 'r', encoding='utf8')
max9 = 0
max10 = 0
max11 = 0
for line in fin:
    lst = list(line.split())
    if lst[2] == '9':
        score = int(lst[3])
        if score > max9:
            max9 = score
    elif lst[2] == '10':
        score = int(lst[3])
        if score > max10:
            max10 = score
    elif lst[2] == '11':
        score = int(lst[3])
        if score > max11:
            max11 = score
print(max9, max10, max11)
