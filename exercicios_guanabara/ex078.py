valores = []

for c in range(0, 5):
    valores.append(int(input(f'Digite um numero para posição {c}: ')))

maximo = max(valores)
minimo = min(valores)
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
