def fatorial(n, show=False):
    """
    ->Calculo fatorial de um numero 'n'
    :param n: Um numero para fazer seu fatorial
    :param show: (OPCIONAL)Mostrar ou não o calculo
    :return: Retorna o valor de 'n' depois do calculo fatorial
    """

    f = 1
    for c in range(n, 0, -1):
        if show:
            if c > 1:
                print(f'{c} x ', end='')
            else:
                print(f'{c} = ', end='')
        f *= c
    return f


num = int(input('Um numero para calcular seu fatorial: '))
rps = str(input('Deseja mostrar a conta? [S/N] ')).upper()[0]
if rps == 'S':
    print(fatorial(num, show=True))
else:
    print(fatorial(num))
