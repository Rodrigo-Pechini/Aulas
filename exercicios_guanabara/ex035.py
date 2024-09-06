print(20 * '-=')
print('Analizandor de triangulos!!')
print(20 * '-=')
a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))

if a + b > c and b + c > a and c + a > b:
    print('Os segmentos a cima \033[4;32mPODEM FORMAR\033[m um triângulo.')
else:
    print('Os segmentos a cima \033[4:31mNÃO PODEM FORMAR\033[m um triângulo.')
