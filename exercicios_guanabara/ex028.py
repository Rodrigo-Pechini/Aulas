from random import randint
from time import sleep

jogo = str(input('Vamos jogar um jogo? ')).lower().strip()
if jogo == 'sim':
    print('Yaay!!!')
else:
    print('Vamos jogar mesmo assim hehe')

num1 = randint(0, 5)
num2 = int(input('Estou pensado em um numero de 0 a 5 sabe qual é? '))
print('PROCESSANDO...')
sleep(3)
if num1 == num2:
    print('Yaaay, você acertou!!!')
else:
    print(f'Não foi o certo estava pensando em {num1} não no {num2}')
