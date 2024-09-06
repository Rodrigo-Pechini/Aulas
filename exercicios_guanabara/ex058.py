from random import randint

#Numero escolhido pelo computador
numeros = randint(1, 10)

#Uma breve interação com o usuario
print('''Olá sou seu computador...
Estou pensado em um numero entre 1 e 10''')
#print(numeros)
usuario = int(input('Qual é seu palpite? '))

#para a querba do loop
quebra = 0

#A quantidade de tentavias
tentativas = 0

#O loop que funciona até o usuario acertar o numero
while quebra == 0:

    # se o usuario digitar o numero certo o loop se quebra
    if usuario == numeros:
        quebra += 1

    # indicara se o numero é maior que o numero escolhido pelo usuairo
    elif numeros > usuario:
        print(30*'-')
        print(f'Mais que {usuario}, tente novamente.')
        usuario = int(input('Qual é o proximo palpite: '))
        tentativas += 1

   # indicara se o numero é menor que o numero escolhido pelo usuario
    elif numeros < usuario:
        print(30*'-')
        print(f'Menos que {usuario}, tente novamente.')
        usuario = int(input('Qual é o proximo palpite: '))
        tentativas += 1

if tentativas == 0:
    print(30 * '-')
    print('Uau você teve ZERO tentativas.\n'
          'Estou impressionado!!!')
elif tentativas >= 1:
    if tentativas == 1:
        print(30*'-')
        print(f'Você acertou!\n'
              f'Você precisou de uma tentativa.')
    else:
        print(30*'-')
        print(f'Você acertou!\n'
              f'Você presisou de {tentativas} tentativas.')
