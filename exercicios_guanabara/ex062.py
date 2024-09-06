primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
termo = primeiro
cont = 0
loops = 10

while loops != 0:

    if loops != 0:
        print(termo, end=' - ')
        termo += razao
        loops -= 1
    if loops == 0:
        print('PAUSA')
        loops = int(input('Quantos termos você quer mostrar a mais: '))
    cont += 1

print(f'Progressão finalizada com {cont} termos mostrados.')
