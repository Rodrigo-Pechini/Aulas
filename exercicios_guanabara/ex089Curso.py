ficha = list()
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    r = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if r == 'N':
        break
print('=-' * 20)
print(f'{"Nº":^4}{"NOME":^10}{"MEDIA":>8}')
print('-' * 26)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:^10}{a[2]:>8.1f}')
while True:
    opc = int(input('Mostar notas de qual aluno? (999 para finalizar) '))
    if opc == 999:
        print('FINALIZANDO...')
        break
    if opc <= len(ficha) - 1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
print("<<< VOLTE SEMPRE >>>")
