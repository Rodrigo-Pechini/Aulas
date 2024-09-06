def area(larg, comp):
    a = larg * comp
    print(f'A area de um terreno {larg}X{comp} é de {a:.1f}m²')


print('CALCULO DE TERRENO')
print('-' * 20)
l = float(input('Digite a largura {m}: '))
c = float(input('Digite o comprimento {m}: '))
area(l, c)
