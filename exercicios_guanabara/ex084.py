pessoas = []
dados = []
totpessoas = 0
while True:
    user = str(input('Digite o nome da pessoa: ')).capitalize()
    peso = float(input('Digite o peso: '))
    totpessoas += 1
    dados.append(user)
    dados.append(peso)
    # [:] é uma copia das informações de dados,  pois se não  copiar
    # as informações da lista de dados podem ser alterado na lista de pessoas
    pessoas.append(dados[:])
    # Dados só vai ser usado para fazer amarzenamentos na lista principal
    # Então possodescartala ao final do append em pessoas
    dados.clear()
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

maior = 0
menor = 0
for n, p in enumerate(pessoas):
    if n == 0:
        maior = p[1]
        menor = p[1]
    else:
        if p[1] > maior:
            maior = p[1]
        elif p[1] < menor:
            menor = p[1]

print(f'Foram cadastradas {totpessoas} pessoas.')
print(f'O maior peso encontrado foi de {maior:.1f}kg. Peso de: ', end='')
for p in pessoas:
    if p[1] == maior:
        print(p[0], end=' ')
print()
print(f'O menor peso encontrado foi de {menor:.1f}Kg. Peso de: ', end='')
for p in pessoas:
    if p[1] == menor:
        print(p[0], end=' ')
