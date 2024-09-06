#meu programa não tem problema com a resposta vazia

nome = str(input('Qual é seu nome? ')).capitalize().strip()

soma = 0#para quebra do loop
sexo = ''#quardar o valor que o user digitou no caso "F" ou "M"

while soma == 0:#se soma for ainda 0 o whuile ainda vai continuar rodando
    sexo = str(input('Digite seu sexo [F/M]: ')).upper().strip()[0]#interção com o user
    if sexo == 'F' or sexo == 'M':
        soma += 1#adiciona 1 no soma q faz o lupe romper
    if soma == 0:
        print('Sexo invalido digite novamente')#caso o user erre a digitação

if sexo == 'F':
    print(f'Sexo do {nome} foi registrado como feminino.')
else:
    print(f'Sexo do {nome} foi regitrasdo como masculino.')
