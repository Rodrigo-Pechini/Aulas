jogadores = []
num_gols = []
dados = {}

while True:
    dados['nome'] = str(input('Nome do jogador: ')).capitalize()
    partidas = int(input(f'Quantas partidas o {dados["nome"]} jogou? '))

    totgols = 0
    for c in range(0, partidas):
        gols = int(input(f'Quantos gols fez na {c + 1}º partida: '))
        totgols += gols
        num_gols.append(gols)
    print('\033[32mJOGADOR CADASTRADO\033[m')
    dados['gols'] = num_gols[:]
    dados['total'] = totgols
    while True:
        r = str(input('Deseja continua? [S/N] ')).upper().strip()[0]
        if r in 'SN':
            break
        print('\033[31mINVALIDO\033[m.\nDigite novamente S ou N.')
    jogadores.append(dados.copy())
    dados.clear()
    num_gols.clear()
    print('=-' * 30)
    if r == 'N':
        break
print('Cod |Nome |Gols |Total')
i = 0
for i, j in enumerate(jogadores):
    print(f"{i} |{j['nome']} |{j['gols']} |{j['total']}")
while True:
    print('=-' * 30)
    codigo = int(input('Quer mostrar o codigo de qual jogador? (999 para interremper) '))
    if codigo == 999:
        print('=-' * 30)
        break
    else:
        print('=-' * 30)
        if codigo <= i:
            print(f'LEVANTAMENTO DO JOGADOR {jogadores[codigo]["nome"]}')
            for e, j in enumerate(jogadores[codigo]['gols']):
                print(f'Na {e+1}º partida fez {j}')
        else:
            print('Jogador não enontrado')
print('Programa finalizado')