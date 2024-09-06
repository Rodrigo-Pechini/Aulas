valores = []

while True:
    print()

    n = (int(input('Digite um numero: ')))

    if n in valores:
        print('Numero repetido, não sera adicionado.')
    else:
        valores.append(n)
        print('Numero adicionado com suceso')

    while True:
        opcao = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
        if opcao in 'NS':
            break
        else:
            print('Opção invalida tente novamente.')

    if opcao in 'N':
        break

print('=' * 30)
print(f'Você digitou os valores {sorted(valores)}')
