from time import sleep
from random import randint
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA ''')

player = int(input('Escolha uma opção: '))

rodape = 20 * '=-'
lista = ['PEDRA', 'PAPEL', 'TESOURA']
comp = randint(0, 2)

print('JO!')
sleep(1)
print('KEN!!')
sleep(1)
print('PO!!!')

print(rodape)
print(f'O COMPUTADOR ESCOLHEU {lista[comp]}\n'
      f'O JOGADOR ESCOLHEU {lista[player]}')
print(rodape)

if comp == 0:
    if player == 0:
        print('EMPATE.')
    elif player == 1:
        print('O JOGADOR VENCEU!')
    elif player == 2:
        print('O COMPUTADOR VENCEU!')
    else:
        print('JOGADA INVALIDA!')
elif comp == 1:
    if player == 0:
        print('O COMPUTADOR VENCEU!')
    elif player == 1:
        print('EMPATE.')
    elif player == 2:
        print('O JOGADOR VENCEU!')
    else:
        print('JOGADA INVALIDA.')
elif comp == 2:
    if player == 0:
        print('O JOGADOR VENCEU!')
    elif player == 1:
        print('O COMPUTADOR VENCEU!')
    elif player == 2:
        print('EMPATE.')
    else:
        print('JOGADA INVALIDA.')
