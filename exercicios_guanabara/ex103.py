def ficha(jogador=False, gols=False):
    if not jogador:
        jogador = '<desconhecido>'
    if not gols:
        gols = 0
    print(f'O nome do jogador é {jogador} e fez {gols} gols')


nome = input('Nome do jogador: ').capitalize().strip()
num_gols = input('Numero de gols: ').strip()
ficha(nome, num_gols)
