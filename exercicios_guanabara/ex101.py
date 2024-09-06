#from datetime import date
#posso importar uma biblioteca na função, se for utilizar ela SÓ na função


def voto(data):
    from datetime import date
    global idade
    idade = date.today().year - data
    votar = ''
    if idade <= 15:
        votar = 'NÃO PODE VOTAR'
    elif idade > 61 or idade <= 17:
        votar = 'VOTAR É OPICIONAL'
    else:
        votar = 'VOTO OBRIGATORIO'
    return votar


idade = 0
ano = int(input('Em que ano você nasceu: '))
# estou chamando a função para alterar o valor da variavel idade
voto(ano)
print(f'Esta pessoa tem {idade} anos: {voto(ano)}')
