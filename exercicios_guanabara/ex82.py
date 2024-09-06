valores = []

while True:

    valores.append(int(input('Digite um numero: ')))

    while True:
        r = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
        if r in 'NS':
            break
        else:
            print('Opção invalida tente novamente.')
    if r == 'N':
        break
    print('=-' * 20)

pares = []
impares = []

for v in valores:
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)

print(f'Os valores digitados foram {valores}')
print(f'Os numeros pares são {pares}')
print(f'Os numeros impares são {impares}')
