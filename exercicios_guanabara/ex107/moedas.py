def metade(preco):
    preco /= 2
    return preco


def dobro(preco):
    preco *= 2
    return preco


def diminue(preco, taxa):
    dez = 10 / 100 * preco
    preco -= dez
    return preco


def aumenta(preco, taxa):
    treze = 13 / 100 * preco
    preco += treze
    return preco
