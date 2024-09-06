from datetime import date

data = date.today().year
menor_idade = 0
maior_idade = 0

for c in range(0, 7):
    idade = int(input(f'Em que ano a {c + 1}º nasceu? '))
    idade = data - idade
    if idade >= 18:
        maior_idade += 1
    else:
        menor_idade += 1

print(f'Tem {maior_idade} pessoas com maior idade.')
print(f'Tem {menor_idade} pessoas com menor idade.')
