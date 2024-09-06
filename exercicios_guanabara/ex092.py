from datetime import date

dados = {}
ano = date.today().year

dados['Nome'] = str(input('Nome: ')).capitalize()
data = int(input('Ano de nascimento: '))
dados['Idade'] = ano - data
dados['CTPS'] = ctps = int(input('Carteira de trabalho (0 não tem): '))

if ctps != 0:
    dados['Contratação'] = int(input('Ano de contratação: '))
    dados['Salario'] = int(input('Salario: R$ '))
    dados['Aposentadoria'] = (dados['Contratação'] - data) + 35

print('=-' * 20)
for k, v in dados.items():
    print(f'{k} tem valor {v}')
