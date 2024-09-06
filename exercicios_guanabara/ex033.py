a = int(input('Digite um numero: '))
b = int(input('Digite outro numero: '))
c = int(input('Digite o ultimo numero: '))

#verificando o menor numero
menor = a
if b < a and b < c:
    menor = b
if c < b and c < a:
    menor = c

#verificando o menor numero
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c

print(f'O menor numero é \033[31m{menor}\033[m!')
print(f'O maior numero é \033[32m{maior}\033[m!')
