from datetime import date

data = date.today().year

nome = str(input('Seu nome: ')).strip()
sexo = str(input('Você é do sexo masculino ou feminino? ')).strip().lower()

if sexo == 'masculino':

    ano = int(input('Ano de nascimento: '))
    n = data - ano
    if n > 18:
        saldo = n - 18
        print(f'{nome} você tem {n} anos, seu tempo de alistamento passou,\n'
              f'você deveria ter se alistado a {saldo} anos atras.\n'
              f'Seu alistamento foi em {data - saldo}')
    elif n < 18:
        saldo = 18 - n
        print(f'{nome} você tem {n} anos, ainda falta {saldo} anos,\n'
              f'para o seu alistamento.\n'
              f'Seu alistamento será em {saldo + data}')
    else:
        print(f'{nome} você tem {n} anos, você vai se alistar este ano.')

elif sexo == 'feminino':
    print(f'Olá {nome}, você não precisa fazer alistamento obrigatório.')
else:
    print('Não compreendi, digite o sexo novamente.')
