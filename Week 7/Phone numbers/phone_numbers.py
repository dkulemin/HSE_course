def numSpliter(number):
    number = ''.join(number.split('-'))
    number = ''.join(number.split('('))
    number = ''.join(number.split(')'))
    number = number.strip('+')
    if len(number) > 7:
        return number[1:]
    else:
        return number


number = numSpliter(input())
address_book = []
for _ in range(3):
    tmp = numSpliter(input())
    address_book.append(tmp)
# print(number)
# print(address_book)
for now in address_book:
    if now == number or now == number[3:] \
            or now == ('495' + number):
        print('YES')
    else:
        print('NO')
