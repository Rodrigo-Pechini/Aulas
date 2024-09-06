nome = str(input('Digite seu nome: '))
sexo = str(input('Digite seu sexo [M/F]: ')).upper().strip()[0]

while sexo not in 'MF':
    sexo = str(input('Sexo invalido digite novamente [M/F]: ')).upper().strip()[0]
print(f'Sexo {sexo} registrado.')
