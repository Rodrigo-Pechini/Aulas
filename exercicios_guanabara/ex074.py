from random import randint

numeros = (randint(1, 10), randint(1, 10), randint(1, 10),
           randint(1, 10), randint(1, 10), )

maior = 0
menor = 0
cont = 0
for n in numeros:

    cont += 1
    print(n, end=' ')

    if cont == 1:
        maior = n
        menor = n
    if n > maior:
        maior = n
    elif n < menor:
        menor = n

print(f'\nO maior numero foi {maior}')
print(f'O menor numero foi {menor}')
