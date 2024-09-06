print('Gerador de PA')
print('-=' * 10)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
termo = primeiro
c = 0
while c != 10:
    print(termo, end=' - ')
    termo += razao
    c += 1
print('Acabou')
