def ficha(jogador='<desconhecido>', gols=0):
    print(f'O nome do jogador é {jogador} e fez {gols} gols')


nome = str(input('Nome do jogador: ')).capitalize()
num_gols = str(input('Numero de gols: '))
if num_gols.isnumeric():
    num_gols = int(num_gols)
else:
    num_gols = 0
if nome.strip() == '':
    ficha(gols=num_gols)
else:
    ficha(nome, num_gols)
