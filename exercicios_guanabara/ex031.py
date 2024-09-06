viagem = float(input('Qual vai ser a diastândoa da sua viagem? '))

valor1 = viagem * 0.50
valor2 = viagem * 0.45
print('Viagens de 200Km ou abaixo a passagem custa 0,50cc por Km. \nAcima de 200Km a passagem custa 0,45cc por Km.')
if viagem <= 200:
    print(f'Sua viagem deu no valor de {valor1:.2f}R$')
else:
    print(f'Sua viagem deu no valor de {valor2:.2f}R$')
