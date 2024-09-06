print('Calculando o IMC')
peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))

imc = peso / (2 ** altura)

print(imc)          #TESTAR CODIGO

if imc < 18.5:
    print('você esta ABAIXO DO PESO.')
elif imc < 25:
    print('Você esta no PESO IDEAL.')
elif imc < 30:
    print('Você esta com SOBREPESO.')
elif imc < 40:
    print('você esta com OBESIDADE.')
else:
    print('Você esta com OBESIDADE MÓRBIDA.')
