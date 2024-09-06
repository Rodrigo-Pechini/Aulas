valor = [str(input('Digite a expreção: '))]

aberto = 0
fechado = 0

for v in valor[0]:
    if v == '(':
        aberto += 1
    if v == ')':
        fechado += 1

if aberto == fechado:
    print('Sua expressão esta correta')
else:
    print('Sua expresão esta incorreta')
