time = list()
jogador = dict()
partidas = list()

while True:
    jogador.clear()
    partidas.clear()
    jogador['nome'] = str(input('Nome do jogador: ')).capitalize()
    tot = int(input(f'Quantas partidas o {jogador["nome"]} jogou? '))
    for c in range(0, tot):
        partidas.append(int(input(f'Quantos gols na {c + 1}º partida: ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        r = str(input('Deseja continua? [S/N] ')).upper().strip()[0]
        if r in 'SN':
            break
        print('\033[31mINVALIDO\033[m.\nDigite novamente S ou N.')
    if r == 'N':
        break

print('=-' * 30)
print('cod', end='')
for k in jogador.keys():
    print(f'{k:<15}', end='')
print()
print('-' * 40)
for k, v in enumerate(time):
    print(f'{k:<3} ', end='')
    for v in v.values():
        print(f'{v:<15}', end='')
    print()
print('-' * 40)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Não existe jogador com codigo {busca}')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}:')
        for i, g in enumerate(time[busca]['gols']):
            print(f'   Na partida {i + 1} fez {g} gols')
    print('-' * 40)
print('<< VOLTE SEMPRE >>')
