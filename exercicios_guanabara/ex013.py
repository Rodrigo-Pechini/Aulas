n1 = float(input('Qual é o valor do salario atualmente? '))
n2 = float(input('Qual será o aumento de salario em porcentagem? '))
n3 = n1*n2/100
print(f'O valor a ser adicionado no salario será de {n3:.2f} reais\nentão o valor do salario ficará de {n1+n3:.2f} reais.')
