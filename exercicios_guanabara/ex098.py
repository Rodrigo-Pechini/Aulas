from time import sleep


def contador(inico, fim, passo):

    print('=-' * 20)
    if passo < 0:
        passo *= -1# invertendo o sinal do numero
    if passo == 0:
        passo = 1
    print(f'contagem de {inico} até {fim} de {passo} em {passo}')
    if inico > fim:
        cont = inico
        while cont >= fim:
            print(cont, end=' ')
            cont -= passo
            sleep(0.5)
        print('Fim')
    else:
        for c in range(inico, fim + passo, passo):
            print(c, end=' ')
            sleep(0.5)
        print('Fim')


contador(1, 10, 1)
contador(10, 0, 2)
while True:
    print('=-' * 20)
    print('Agora sua vez de personalizar a contagem.')
    i = int(input('Inicio: '))
    f = int(input('Fim: '))
    p = int(input('Passo: '))
    contador(i, f, p)
    r = str(input('Deseja continuar? [S/N] ')).upper()[0]
    if r == 'N':
        break
print('PROGRAMA FINALIZADO')

