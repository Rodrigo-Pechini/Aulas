from random import randint
from time import sleep

print('ROLANDO DADOS')

dados = {}
for c in range(1, 5):
    dados[f'jogador {c}'] = randint(1, 6)

for k, v, in dados.items():
    print(f'O {k} tirou o valor {v}')

#NÃO CONSEGUI MOSTRAR O RANKING