print(20 * '=', 'LOJÃO RODRIGO', 20 * '=')

valor = float(input('Digite o valor do produto: '))

print('''FORMAS DE PAGAMENTOS
[ 1 ] á vista em dinheiro/cheque
[ 2 ] á vista no cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')

opcao = int(input('Qual é a opção: '))

if opcao == 1:
    desconto = valor - (valor * 10 / 100)
    print(f'Seu o produto teve um desconto de 10%, então '
          f'ele custará {desconto}R$')
elif opcao == 2:
    desconto = valor - (valor * 5 / 100)
    print(f'Seu produto teve um desconto de 5%, então '
          f'ele custará {desconto}R$')
elif opcao == 3:
    desconto = valor / 2
    print(f'Seu produto de {valor:.2f}R$ foi parcelado em 2x de {desconto:.2f}R$')
elif opcao == 4:
    parecelas = int(input('Em quantas parcelas? '))
    if parecelas >= 20:
        juros = ((valor * 35 / 100) + valor) / parecelas
        print(f'Seu produto foi parcelado em {parecelas}x de {juros:.2f}R$,\n'
              f'no final ele custara {juros * parecelas:.2f}R$.')
    else:
        juros = ((valor * 20 / 100) + valor) / parecelas
        print(f'Seu produto foi parcelado em {parecelas}x de {juros:.2f}R$,\n'
              f'no final ele custara {juros * parecelas:.2f}R$.')
else:
    print('Opção invalida.')
