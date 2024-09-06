maior = homens = mulheres = 0
print('-' * 20)
print(f'CADASTRO DE PESSOA')
print('-' * 20)

while True:

    print('-=' * 10)
    idade = int(input('Qual idade da pessoa? '))

    while True:
        sexo = str(input('Qual é o sexo? [M/F] ')).upper().strip()[0]
        if sexo in 'MF':
            break

    if idade >= 18:
        maior += 1
    if sexo == 'M':
        homens += 1

    if sexo == 'F' and idade < 20:
            mulheres += 1

    print('-=' * 10)
    while True:
        quebra = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
        if quebra in 'SN':
            break
    if quebra == 'N':
        break

print('-=' * 10)
print(f'Total de pessoa com mais de 18 anos: {maior}')
print(f'Foram cadastrado {homens} homens.')
print(f'Tem {mulheres} mulhres menores que 20 anos.')
