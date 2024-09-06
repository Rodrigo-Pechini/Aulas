from datetime import date

ano_nasc = int(input('Ano de nascimento: '))
ano_atual = date.today().year
idade = ano_atual - ano_nasc

print(f'Este atleta tem {idade} anos ele é:')
if idade <= 9:
    print('MIRIM')
elif 9 < idade <= 14:
    print('INFANTIL')
elif idade > 14 and idade <= 19: #forma tradicional do programa logico
    print('JUNIOR')
elif 19 < idade <= 25:
     print('SÊNIOR')
else:
     print('MASTER')

#forma do curso 
'''if idade <= 9:
    print('MIRIM')
elif idade <= 14:
    print('INFANTIL')
elif idade <= 19: 
    print('JUNIOR')
elif idade <= 25:
     print('SÊNIOR')
else:
     print('MASTER')'''
