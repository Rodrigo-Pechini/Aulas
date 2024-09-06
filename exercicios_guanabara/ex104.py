def leiaint(msg):
    """
    -> valida se o usuario digitou um numero ou não
    :param msg: o input do usuario
    :return: Se não for um numero retorna uma mensgem de erro
    e um input novo, se for um numero só retorna o valor
    """
    while True:
        valor = input(msg)
        valido = valor.strip().isnumeric()
        if valido:
            #O return funciona como break
            return valor
        print('\033[31mERRO! Digite um numero.\033[m')



n = leiaint('Digite um numero: ')
print(f'Você digitou o numero {n.strip()}')
