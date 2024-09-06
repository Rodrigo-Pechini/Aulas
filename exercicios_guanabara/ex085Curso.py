num = [[], []]
valores = 0
for c in range(1, 8):
    valores = int(input(f'Digite {c}º numero: '))
    if valores % 2 == 0:
        num[0].append(valores)
    else:
        num[1].append(valores)
print('=-' * 20)
num[0].sort()
num[1].sort()
print(f'Os valores PARES digitados foram {num[0]}')
print(f'Os valores IMPARES digitados forma {num[1]}')
