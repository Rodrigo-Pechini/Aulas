print('Calculo fatorial')
n = int(input('Digite um numero: '))

'''c = n
f = 1
print(f'Calculando fatorial de {n}! = ', end='')
while c > 0:
    if c > 1:
        print(f'{c} x ', end='')
    else:
        print(f'{c} = ', end='')
    f *= c
    c -= 1
print(f)'''

f = 1
for c in range(n, 0, -1):#o -1 faz a conta de 'n' ate o zero
    if c > 1:
        print(f'{c} x ', end='')
    else:
        print(f'{c} = ', end='')
    f *= c
print(f)
