from time import sleep

n1 = float(input('Digite um numero: '))
n2 = float(input('Digite outro numero: '))
quebra = True

while quebra:
    
    print(30 * '-=')
    print('''ESOLHA UMA OPÇÃO:
    [1] SOMA.
    [2] MULTIPLICAR.
    [3] MAIOR.
    [4] NOVOS NUMEROS.
    [5] SAIR DO PROGRAMA.''')

    opcao = int(input('Digite a opção: '))
    print(30 * '-=')

    if opcao == 1:
        valor = n1 + n2
        print(f'A soma entre {n1} + {n2} é {valor}.')
    elif opcao == 2:
        valor = n1 * n2
        print(f'A multiplicação entre {n1} * {n2} é {valor}.')
    elif opcao == 3:
        if n1 > n2:
            valor = n1
            print(f'Entre o valor {n1} e {n2} o maoir é {valor}')
        elif n1 < n2:
            valor = n2
            print(f'Entre os numeros {n1} e {n2} o maior é {valor}')
        else:
            print('Os dois numeros são iguais')
    elif opcao == 4:
        n1 = float(input('Digite um novo numero: '))
        n2 = float(input('Digite outro: '))
    elif opcao == 5:
        quebra = False
        print('Finalizando...')
    else:
        print('Opção invalida digite novamente.')
    sleep(2)

print('Pograma finalizado.')
