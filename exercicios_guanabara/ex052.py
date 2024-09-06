num = int(input('Digite um numero: '))
tot = 0

# o mais importante é o resultado do if dentro do for, pois se ele acontecer +2 vezes
# o numero não vai ser primo

for c in range(1, num + 1):
    if num % c == 0:
        tot += 1
        print('\033[32m', end='')
    else:
        print('\033[31m', end='')
    print(f'{c}', end=' ')

print(f'\n\033[mO numero {num} foi divisivel {tot} vezes.')
if tot == 2:
    print('Por isso ele É PRIMO')
else:
    print('Por isso ele NÃO É PRIMO')
