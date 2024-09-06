def metade(preco=0):
    preco /= 2
    return moeda(preco)


def dobro(preco=0):
    preco *= 2
    return moeda(preco)


def diminue(preco=0, taxa=0):
    dez = taxa / 100 * preco
    preco -= dez
    moeda(preco)
    return moeda(preco)


def aumenta(preco=0, taxa=0):
    treze = taxa / 100 * preco
    preco += treze
    return moeda(preco)


def moeda(preco=0, moeda='R$'):

    formatar = f'{moeda}{preco:.2f}'.replace('.', ',')
    return formatar


def resumo(preco=0, juros=0, reducao=0):

    print('-' * 30)
    print(f'{"RESUMO DO VALOR ":^30}')
    print('-' * 30)
    print(f"Preço analizado: \t{moeda(preco)}")
    print(f"Dobro do preço: \t{dobro(preco)}")
    print(f"Metade do preço: \t{metade(preco)}")
    print(f"Aumento de {juros}%: \t{aumenta(preco, juros)}")
    print(f"Redução de {reducao}%: \t{diminue(preco, reducao)}")
    print('-' * 30)
