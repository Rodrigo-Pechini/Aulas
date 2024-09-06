from time import sleep
from random import choice

print('''Suas opçãoes:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA ''')

player = int(input('Escolha uma opção: '))

rodape = 20 * '=-'
lista = [0, 1, 2]
comp = choice(lista)

if comp == 0:
    comp = 'pedra'
elif comp == 1:
    comp = 'papel'
elif comp == 2:
    comp = 'tesoura'

if player == 0:
    player = 'pedra'
elif player == 1:
    player = 'papel'
elif player == 2:
    player = 'tesoura'

print('JO!')
sleep(1)
print('KEN!!')
sleep(1)
print('PO!!!')

print(rodape)
print(f'O COMPUTADOR ESCOULHEU {comp.upper()}\n'
      f'O JOGADOR ESCOLHEU {player.upper()}')
print(rodape)

if comp == 'tesoura' and player == 'papel' or comp == 'papel' and player == 'pedra'\
        or comp == 'pedra' and player == 'tesoura':
    print(' O COMPUTADOR VENCEU')
elif player == 'tesoura' and comp == 'papel' or player == 'papel' and comp == 'pedra'\
        or comp == 'tesoura' and player == 'pedra':
    print(' O JOGADOR VENCEU')
elif comp == player:
    print(' EMPATE')
