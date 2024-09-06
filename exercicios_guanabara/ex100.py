from random import randint
from time import sleep


def sorteia(lista):
    print('Sorteando 5 valores da lista ', end='')
    for c in range(0, 5):
        a = randint(1, 10)
        print(a, end=' ')
        lista.append(a)
    print()


def somapar(lista):
    par = 0
    for n in lista:
        if n % 2 == 0:
            par += n
    print(f'Somando todos os valores de {lista}, temos {par}')


numeros = list()
sorteia(numeros)
somapar(numeros)
