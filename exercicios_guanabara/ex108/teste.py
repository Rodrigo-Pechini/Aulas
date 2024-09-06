from ex109.moedas import *

n = float(input('Digite um preço: R$ '))

print(f'A metade de {moeda(n)} metade é de {moeda(metade(n))}')
print(f'O dobro de {moeda(n)} é {moeda(dobro(n))}')
print(f'Diminuindo 10% de {moeda(n)} temos {moeda(diminue(n, 10))}')
print(f'Aumento 13% de {moeda(n)} temos {moeda(aumenta(n, 13))}')
