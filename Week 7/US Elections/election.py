fin = open('input.txt')
election = {}
for line in fin:
    key, value = line.split()
    election[key] = election.get(key, 0) + int(value)
for key in sorted(election):
    print(key, election[key])
