listagem = ('Camiseta', 179.80, 'Calça Jeans', 89.00, 'Tênis', 89.90, 'Jaqueta',
            49.90, 'Óculos de Sol', 129.99,  'Relógio', 129.50, 'Bolsa', 249.50,
            'Boné', 249.50, 'Carteira', 159.90, 'Cinto', 299.00)

print('-' * 40)
print(f'{"LOJA":^40}')
print('-' * 40)

for c in range(0, len(listagem)):

    if c % 2 == 0:
        print(f'{listagem[c]:.<30}', end='')
    else:
        print(f"R$ {listagem[c]:>7.2f}")

print('-' * 40)
