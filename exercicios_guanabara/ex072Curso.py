numeros = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis',
           'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze',
           'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito',
           'dezenove', 'vinte')


while True:

    contagem = int(input('Digite um numero entre 0 e 20: '))

    if 0 <= contagem <= 20:
        print(f'Você digitou o numero \033[32m{numeros[contagem]}\033[m')

        while True:
            opicao = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
            if opicao in 'SN':
                break
            else:
                print('\033[31mOpção invalidada tente novamente\033[m')

        if opicao in 'N':
            break
    else:
        print('\033[31mOpção invalidada tente novamente\033[m')
