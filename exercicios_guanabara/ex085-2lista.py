princ = []
pares = []
impares = []

for c in range(1, 8):
    n = int(input(f'Digite {c}º numero: '))
    if n % 2 == 0:
        pares.append(n)

    else:
        impares.append(n)

princ.append(pares)
princ.append(impares)

print(f'Os valores PARES digitados foram {sorted(princ[0])}')
print(f'Os valores IMPARES digitados forma {sorted(princ[1])}')
