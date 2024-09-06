jogador = dict()
partidas = list()

jogador['nome'] = str(input('Nome do jogador: ')).capitalize()
tot = int(input(f'Quantas partidas o {jogador["nome"]} jogou? '))

for c in range(0, tot):
    partidas.append(int(input(f'Quantos gols na {c + 1}º partida: ')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)

print('=-' * 20)
print(jogador)
print('=-' * 20)

for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('=-' * 20)

print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])}')
for i, v in enumerate(jogador['gols']):
    print(f'   ==>Na {i + 1}º partida, fez {v} gols.')
print(f'Foi um total de {jogador["total"]} gols.')
