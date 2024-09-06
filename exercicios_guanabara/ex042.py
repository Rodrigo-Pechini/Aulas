a = float(input('Primeiro seguimento: '))
b = float(input('Segundo seguimento: '))
c = float(input('Terceiro seguimento: '))

n1 = a + b > c
n2 = b + c > a
n3 = a + c > b

correto = n1 == n2 == n3 #estou comparando as respostas booleanas

#aqui esta uma forma usando um if em um if
if correto == True:
    if a == b == c:
        print('Esse é um triangulo EQUILATERO')
    elif a == b or b == c or a ==c:
        print('Esse é um triangulo EQUILATERO')
    elif a != b != c != a: #tive que fazer a comparação com c & a pois poderia dar um erro
        print('Esse é um triangulo ESCALENO')
else:
    print('Não tem como formar um triangulo')

#aqui esta um jeito usando só um if
'''if a == b == c and correto == True:
    print('Esse é um triangulo EQUILATERO')
elif a == b or b == c or c == a and correto == True:
    print('Esse é um triangulo ESOSILES')
elif a != b != c != a and correto == True:
    print('Esse é um triangulo ESCALENO')
else:
    print('Não tem como formar um triangulo')'''
