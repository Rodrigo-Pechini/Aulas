valores = []

maximo = 0
minimo = 0

for c in range(0, 5):
    valores.append(int(input(f'Digite um numero para posição {c}: ')))

    if c == 0:
      maximo = minimo = valores[c]
    else:
        if maximo < valores[c]:
            maximo = valores[c]
        if minimo > valores[c]:
            minimo = valores[c]

print('=' * 40)
print(f'Os valores digitados foram {valores}')

print(f'O maior valor é {maximo} e ele esta na posisão: ', end='')
for e, v in enumerate(valores):
    if maximo == v:
        print(e, end=' ')

print(f'\nO menor valor é {minimo} ele esta na posisão: ', end='')
for e, v in enumerate(valores):
    if minimo == v:
        print(e, end=' ')
