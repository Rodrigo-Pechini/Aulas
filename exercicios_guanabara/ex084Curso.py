princ = []
temp = []
menor = maior = 0
while True:
    temp.append(str(input('Digite o nome da pessoa: ')).capitalize())
    temp.append(float(input('Digite o peso: ')))
    if len(princ) == 0:
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        elif temp[1] < menor:
            menor = temp[1]
    # [:] é uma copia das informações de dados,  pois se não  copiar
    # as informações da lista de dados podem ser alterado na lista de pessoas
    princ.append(temp[:])
    # Dados só vai ser usado para fazer amarzenamentos na lista principal
    # Então possodescartala ao final do append em pessoas
    temp.clear()
    print('Cadastrado')
    while True:
        r = str(input('Deseja continua? [S/N] ')).upper().strip()[0]
        if r in 'SN':
            break
        else:
            print('Resposta invalida tente novamente.')
    print('=-' * 20)
    if r == 'N':
        break

print(f'Foram cadastradas {len(princ)} pessoas.')
print(f'O maior peso encontrado foi de {maior:.1f}kg. Peso de: ', end='')
for p in princ:
    if p[1] == maior:
        print(p[0], end=' ')
print()
print(f'O menor peso encontrado foi de {menor:.1f}Kg. Peso de: ', end='')
for p in princ:
    if p[1] == menor:
        print(p[0], end=' ')
