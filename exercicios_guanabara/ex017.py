from math import hypot

c1 = float(input('Digite o valor do cateto oposto: '))
c2 = float(input('Digite o valor do cateto adjacente: '))

'''soma_c = pow(c1, 2) + pow(c2, 2)
h = math.sqrt(soma_c)
print(f'O valor da hipotenusa sera de {h:.2f}.')'''

h = hypot(c1, c2)
print(f'O calor da hipotenusa será de {h:.2f}.')
