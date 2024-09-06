print('Gerador de PA')
print('-=' * 10)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
termo = primeiro
c = 1
total = 0
mais = 10

while mais != 0:
    total += mais

    while c <= total:
        print(termo, end=' - ')
        termo += razao
        c += 1

    print('Pausa')
    mais = int(input('Quantos termos a mais você quer mostras: '))

print(f'Progressão finalizada com {total} termos mostrados.')
