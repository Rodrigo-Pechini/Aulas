def metade(preco=0):
    preco /= 2
    moeda(preco)
    return preco


def dobro(preco=0):
    preco *= 2
    moeda(preco)
    return preco


def diminue(preco=0, taxa=0):
    dez = taxa / 100 * preco
    preco -= dez
    moeda(preco)
    return preco


def aumenta(preco=0, taxa=0):
    treze = taxa / 100 * preco
    preco += treze
    moeda(preco)
    return preco


def moeda(preco=0, moeda='R$'):

    formatar = f'{moeda}{preco:.2f}'.replace('.', ',')
    return formatar
