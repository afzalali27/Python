string = input('enter the string : ')
digit = 0
letter = 0
for x in string:
    if x >= '1' and x <= '9':
        digit += 1
    elif ('a' <= x <= 'z') or ('A' <= x <= 'Z'):
        letter += 1
print(f'Digits : {digit}')
print(f'Letters : {letter}')
