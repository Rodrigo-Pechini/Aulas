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
print('=-' * 20)
somapar = 0
somacoluna = 0
maior = max(matriz[1])
for n in matriz:
    for i, c in enumerate(n):
        print(f'[{c:^5}]', end=' ')
        if c % 2 == 0:
            somapar += c
        if i == 2:
            somacoluna += c
    print()
print('=-' * 20)
print(f'A soma de todos os pares é {somapar}')
print(f'A soma de todos os valores da 3º coluna é {somacoluna}')
print(f'O maior valor da 2º linha é  {maior}')
