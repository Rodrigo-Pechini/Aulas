from random import randint

print('=-' * 30)
print('VAMOS JOGAR IMPAR OU PAR')
print('=-' * 30)

vit = 0
while True:
    comp = randint(0, 10)

    n = int(input('Digite um valor: '))

    while True:
        opcao = str(input('Par ou Impar: [P/I] ')).upper().strip()[0]
        if opcao in 'IP':
            break
    print('-' * 60)

    soma = n + comp
    if soma % 2 == 0:
        resp = 'Par'
    else:
        resp = 'Impar'

    print(f'Você jogou {n} o computador jogou {comp}, a soma deu {soma} é {resp}')
    print('-' * 60)

    if resp[0] == opcao:
        vit += 1
        print('VOCÊ VENCEU!!!\n'
              'Vamos jogar novamente...')
    else:
        break
    print('=-' * 30)

print(f'Você perdeu!')
print(f'Você ganhou {vit} vezes')
