from ex108.moedas import *

n = float(input('Digite um preço: R$ '))

print(f'A metade de {moeda(n)} metade é de {metade(n)}')
print(f'O dobro de {moeda(n)} é {dobro(n)}')
print(f'Diminuindo 10% de {moeda(n)} temos {diminue(n, 10)}')
print(f'Aumento 13% de {moeda(n)} temos {aumenta(n, 13)}')
