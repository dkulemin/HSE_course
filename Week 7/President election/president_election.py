fin = open('input.txt', encoding='utf8')
fout = open('output.txt', 'w', encoding='utf8')
candidates = {}
votes = 0
for line in fin:
    candidates[line.strip()] = candidates.get(line.strip(), 0) + 1
    votes += 1
fin.close()
output = []
for key, value in candidates.items():
    output.append((value, key))
output.sort(key=lambda cand: (-cand[0], cand[1]))
if output[0][0] / votes > 0.5:
    print(output[0][1], file=fout)
else:
    print(output[0][1], output[1][1], sep='\n', file=fout)
fout.close()
