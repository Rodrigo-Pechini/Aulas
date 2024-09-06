import math

angulo = float(input('Digite um angulo: '))
cos = math.cos(math.radians(angulo))
sen = math.sin(math.radians(angulo))
tang = math.tan(math.radians(angulo))
print(f'O angulo de {angulo} tem o COSSENO de {cos:.2f}.')
print(f'O angulo de {angulo} tem o SENO de {sen:.2f}.')
print(f'O angulo de {angulo} tem a TANGENTE de {tang:.2f}.')
