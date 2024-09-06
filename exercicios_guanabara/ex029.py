veloci = int(input('O quão rapido você ja foi com um carro? '))

multa = (veloci - 80) * 7

if veloci > 80:
    print(f'Voce foi multado o valor da multa é de \033[31m{multa}R$\033[m')
elif veloci >= 50:
    print('Nossa que rapido quase foi \033[31mmultado\033[m.')
else:
    print('Boa ande em segurança.')
