from random import randint
from time import sleep

jogos = []
lista = []

valor = int(input('Quantos jogos você quer fazer? '))
print('GERANDO {} JOGOS'.format(valor))
tot = 0
while tot <= valor:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        elif cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()

for i, n in enumerate(jogos):
    print(f'jogo {i+1}: {n}')
    sleep(1)

print(f'----BOA SORTE----')
