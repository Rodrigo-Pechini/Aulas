def Area(largura, comprimento):
    area = largura * comprimento
    print(f'A area de um terreno {largura}X{comprimento} é de {area:.1f}m²')


print('CALCULO DE TERRENO')
print('-' * 20)
largura = float(input('Digite a largura {m}: '))
comprimento = float(input('Digite o comprimento {m}: '))
Area(largura, comprimento)
