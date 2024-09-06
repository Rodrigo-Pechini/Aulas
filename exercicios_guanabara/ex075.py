n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))
n3 = int(input('Digite o terceiro numero: '))
n4 = int(input('Digite o quarto numero: '))

tupla = (n1, n2, n3, n4)

print(f'Você digitou os valores: {tupla}')
print(f'O valor 9 apareceu {tupla.count(9)} vezes')

if not 3 in tupla:
    print(f'valor 3 não encontrado')
else:
    print(f'O valor 3 apareceu na posisão {tupla.index(3) + 1}º')

print('Os valores pares digitados foram: ', end='')
for n in tupla:

    if n % 2 == 0:
        print(n, end=' ')

