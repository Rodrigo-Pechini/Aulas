from random import randint
from time import sleep
from operator import itemgetter

jogos = {
    'jogador 1': randint(1, 6),
    'jogador 2': randint(1, 6),
    'jogador 3': randint(1, 6),
    'jogador 4': randint(1, 6)
}

ranking = []
print('Valores sorteados')
for k, v in jogos.items():
    print(f'O {k} tirou {v} no dado.')
print('=-' * 20)
print('RANKING')
ranking = sorted(jogos.items(), key=itemgetter(1), reverse=True)
for i, n in enumerate(ranking):
    print(f'{i+1}º lugar: O {n[0]} com {n[1]}')

