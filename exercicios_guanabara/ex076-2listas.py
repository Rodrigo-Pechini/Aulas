produtos = ('Camiseta', 'Calça Jeans', 'Tênis', 'Jaqueta',
            'Óculos de Sol', 'Relógio', 'Bolsa', 'Boné', 'Carteira', 'Cinto')

precos = (179.80, 89.00, 89.90, 49.90, 129.99, 129.50,
          249.50, 159.90, 299.00, 199.00)

print('-' * 35)
print(f'{"LOJA":^33}')
print('-' * 35)

for c in range(1, 10):

    print((produtos[c]).ljust(23, '.'), end=' ')
    print(f'R$ {(precos[c]):7.2f}')

print('-' * 35)
