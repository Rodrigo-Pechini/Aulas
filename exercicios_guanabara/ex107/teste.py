from ex109.moedas import *

n = float(input('Digite um preço: R$ '))

print(f'A metade de {n} metade é de {metade(n)}')
print(f'O dobro de {n} é {dobro(n)}')
print(f'Diminuindo 10% de {n} temos {diminue(n, 10)}')
print(f'Aumento 13% de {n} temos {aumenta(n, 13)}')
