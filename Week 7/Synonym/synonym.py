n = int(input())
synonyms = {}
for now in range(n):
    value, key = input().split()
    synonyms[key] = value
    synonyms[value] = key
print(synonyms[input()])
