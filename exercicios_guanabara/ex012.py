n1 = float(input('Qual é o valor do produto? R$'))
n2 = float(input('Qual é o valor do desconto em porcentagem? %'))
n3 = n1*n2/100
print(f'O seu produto terá um desconto de {n2:.0f}%,\nentão o produto estará com o valor de R${n1-n3:.2f}.')
