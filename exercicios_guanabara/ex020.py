from random import shuffle

n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Segundo aluno: '))
n4 = str(input('Terceiro aluno: '))
lista = [n1, n2, n3, n4]
shuffle(lista)
print('A ordem de apresentação sera:')
print(lista)
