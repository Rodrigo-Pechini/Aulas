def leiadin(msg):
    while True:
        valor = str(input(msg).strip().replace(',', '.'))
        valido = valor.isalpha()
        if valido or valor == '':
            print(f'\033[31mERRO! "{valor}" não é um numero valido\033[m')
        else:
            break
    return float(valor)
