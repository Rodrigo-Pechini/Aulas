from random import randint
from time import sleep

jogos = []
lista = []

valor = int(input('Quantos jogos você quer fazer? '))
print('GERANDO {} JOGOS'.format(valor))
num = 0
for n in range(1, valor + 1):
    for c in range(0, 7):
        aletorio = randint(1, 60)
        if c == 0:
            num = aletorio
        else:
            if aletorio != num:
                num = aletorio
                lista.append(num)
    lista.sort()
    jogos.append(lista[:])
    lista.clear()

for i, n in enumerate(jogos):
    print(f'jogo {i+1}: {jogos[i]}')
    sleep(1)

print(f'----BOA SORTE----')
