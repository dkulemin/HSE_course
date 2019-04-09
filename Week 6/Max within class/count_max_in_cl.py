fin = open('input.txt', 'r', encoding='utf8')
lines = fin.readlines()
myList9 = []
myList10 = []
myList11 = []
for line in lines:
    tmp = line.strip().split()
    if tmp[2] == '9':
        myList9.append(int(tmp[3]))
    if tmp[2] == '10':
        myList10.append(int(tmp[3]))
    if tmp[2] == '11':
        myList11.append(int(tmp[3]))
max9 = max(myList9)
max10 = max(myList10)
max11 = max(myList11)
count9 = 0
count10 = 0
count11 = 0
for now in myList9:
    if now == max9:
        count9 += 1
for now in myList10:
    if now == max10:
        count10 += 1
for now in myList11:
    if now == max11:
        count11 += 1
print(count9, count10, count11)
