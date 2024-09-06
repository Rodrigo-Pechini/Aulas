num = (int(input('Digite o primeiro numero: ', )),
       int(input('Digite o segundo numero: ',)),
       int(input('Digite o terceiro numero: ',)),
       int(input('Digite o quartoo numero: ',)),)

print(f'Você digitou os valores: {num}')
print(f'O valor 9 apareceu {num.count(9)} vezes')

if 3 in num:
    print(f'O valor 3 apareceu na posisão {num.index(3) + 1}º')
else:
    print(f'valor 3 não encontrado')

print('Os valores pares digitados foram: ', end='')

for n in num:

    if n % 2 == 0:
        print(n, end=' ')

