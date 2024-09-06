dados = {}
num_gols = []
dados['nome'] = str(input('Nome do jogador: ')).capitalize()
partidas = int(input(f'Quantas partidas o {dados["nome"]} jogou? '))

totgols = 0
for c in range(0, partidas):
    gols = int(input(f'Quantos gols fez na {c + 1}º partida: '))
    totgols += gols
    num_gols.append(gols)
print('=-' * 20)
dados['gols'] = num_gols[:]
dados['total'] = totgols

for k, v in dados.items():
    print(f'O {k} tem como valor {v}.')
print('=-' * 20)
print(f'O jogador {dados["nome"]} jogou {partidas} partidas.')
for c in range(0, partidas):
    print(f'   ==>Na {c+1}º partida {dados["nome"]} fez {dados["gols"][c]}')
print(f'No total foram {dados["total"]} gols.')
