valores = []

while True:
    valores.append(int(input('Digite um numero: ')))

    while True:
        r = str(input('Deseja continuar? [S/N]')).upper().strip()[0]
        if r in 'SN':
            break
        else:
            print('valor invalido digite novamente.')

    if r == 'N':
        break
print('=-' * 20)
print(valores)
print(f'Você digitou {len(valores)} valores')

if 5 in valores:
    print('O valor 5 faz parte da lista, e ele esta na possição: ', end='')
    for e, l in enumerate(valores):
        if l == 5:
            print(e, end=' ')
else:
    print('O valor 5 não foi encotrado na lista', end='')
print()
valores.sort(reverse=True)
print(f'Os valores em ordem decrescente são {valores}')