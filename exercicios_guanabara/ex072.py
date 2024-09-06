numeros = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis',
           'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze',
           'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito',
           'dezenove', 'vinte')



while True:

    contagem = int(input('Digite um numero entre 0 e 20: '))

    if contagem > 20:
        print('Opção invalida tente novamente.')
    elif contagem < 0:
        print('Opção invalida tente novamente.')
    else:
        break

print(f'Você digitou o numero {numeros[contagem]}')
