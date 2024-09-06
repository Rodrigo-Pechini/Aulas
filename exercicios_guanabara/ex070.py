soma = umbarao = menor = 0
barato = ' '

while True:
    print('=-' * 20)
    produto = str(input('Qual é o nome do produto? ')).strip().capitalize()
    preco = float(input('Preço: R$ '))
    soma += preco

    if preco >= 1000:
        umbarao += 1

    if menor == 0 or menor > preco:
        menor = preco
        barato = produto

    print('=-' * 20)
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break

print(f'O total de sua compra foi de R${soma:.2f}')
print(f'Você comprou {umbarao} acima de R$1000')
print(f'O produto mais barato comprado é {barato} custando R${menor}')
