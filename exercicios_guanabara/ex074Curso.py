from random import randint

numeros = (randint(1, 10), randint(1, 10), randint(1, 10),
           randint(1, 10), randint(1, 10))

print('Os numero sorteados foram: ', end='')

for n in numeros:
    print(n, end=' ')

print(f'\nO maior numero foi {max(numeros)}')
print(f'O menor numero foi {min(numeros)}')
