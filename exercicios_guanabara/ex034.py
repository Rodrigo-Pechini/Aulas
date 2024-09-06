salario = float(input('Digite seu salario atual: '))

aumento10 = salario * 10 / 100 + salario
aumento15 = salario * 15 / 100 + salario

if salario <= 1250.00:
    print(f'O valor novo do seu salario é de {aumento15}R$')
else:
    print(f'O valor novo do seu salario é de {aumento10}R$')
