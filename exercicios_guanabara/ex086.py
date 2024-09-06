matriz = [[], [], []]
a = 0
b = 0
for c in range(1, 10):
    valores = int(input(f'Digite um valor para posisão {a , b}: '))
    if c <= 3:
        matriz[0].append(valores)

    else:
        if c <= 6:
            matriz[1].append(valores)
        else:
            if c <= 9:
                matriz[2].append(valores)
    b += 1
    if c == 3:
        a += 1
        b = 0
    if c == 6:
        a += 1
        b = 0

for n in matriz:
    for c in n:
        print(f'[{c:^5  }]', end=' ')
    print()
