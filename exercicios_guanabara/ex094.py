dados = []
pessoas = {}
media = 0

while True:
    pessoas['nome'] = str(input('Nome: ')).capitalize()
    pessoas['idade'] = soma = int(input('Idade: '))
    media += soma
    while True:
        pessoas['sexo'] = str(input('Sexo: [F/M] ')).upper().strip()[0]
        if pessoas['sexo'] in 'FM':
            if pessoas['sexo'] == 'M':
                print('\033[32mCADASTRADO\033[m')
            else:
                print('\033[32mCADASTRADA\033[m')
            break
        print('\033[31mINVALIDO\033[m.\nDigite novamente F ou M.')
    while True:
        r = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
        if r in 'SN':
            print('=-' * 20)
            break
        print('\033[31mINVALIDO\033[m.\nDigite novamente S ou N.')
    dados.append(pessoas.copy())
    pessoas.clear()
    if r == 'N':
        break

media /= len(dados)
print(f'(A) Ao todo temos {len(dados)} pessoas cadastradsa.')
print(f'(B) A média de idade do grupo é de {media} anos')

print('(c) As mulheres cadastradas foram: ', end='')
for d in dados:
    if d['sexo'] == 'F':
        print(d["nome"], end=' ')
print()

print('(D) Lista das pessoas que estão acima da media.')
for d in dados:
    if d['idade'] > media:
        print(f'nome = {d["nome"]}; idade = {d["idade"]}; sexo = {d["sexo"]};')
