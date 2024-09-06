valor_casa = float(input('Qual é o valor da casa? '))
valor_salario = float(input('Qual é o valor do seu salario? '))
financiamento = int(input('Em quantos anos de financiamento? '))

parcelas = valor_casa / (financiamento * 12)
salario30 = valor_salario * 30 / 100
cores = {
    'limpa': '\033[m',
    'verde': '\033[32m',
    'vermelho': '\033[31m'
}

print(f'A casa que você vai comprar é de {valor_casa:.2f}R$, suas parecelas durnate {financiamento} anos'
      f'\n vai custar {parcelas:.2f}R$ por mês.')

if parcelas < salario30:
    print(f'Seu imprestimo foi {cores["verde"]}APROVADO{cores["limpa"]}.')
else:
    print(f'Seu imprestimo foi {cores["vermelho"]}NEGADO{cores["limpa"]}.')
