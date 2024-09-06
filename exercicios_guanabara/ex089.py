geral = []
alunos_notas_medias = []
alunos = []
notas = []
medias = []
media = 0
cont = 0

while True:
    alunos.append(str(input('Nome do aluno: ')).capitalize())
    alunos_notas_medias.append(alunos[:])
    for c in range(0, 2):
        notas.append(float(input(f'Nota {c+1}: ')))
        media += notas[c]
    while True:
        r = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
        if r in 'SN':
            print('=-' * 20)
            break
        else:
            print('Opção invalida digite novamente.')
    medias.append(media/2)
    alunos_notas_medias[cont].append(notas[:])
    alunos_notas_medias[cont].append(medias[:])
    notas.clear()
    alunos.clear()
    medias.clear()
    media = 0
    cont += 1
    if r == 'N':
        break

print('Nº | NOME     | MEDIA')
for i, l in enumerate(alunos_notas_medias):
    print(f'{i}  | {l[0]:^8} | {l[2]}')
print('=-' * 20)
while True:
    mostra = int(input('Mostra nota de qual aluno? '))
    print(f'As notas {alunos_notas_medias[mostra][0]} são {alunos_notas_medias[mostra][1]}')
    if mostra == 999:
        break
print('PROGRAMA FINALIZADO')
