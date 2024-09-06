
nome_atual = ''
idade_atual = 0
nome_anterior = ''
idade_anterior = 0
tot_menorque20 = 0
tot_mulheres = 0
tot_homens = 0
media = 0

print('PESQUISA IBGE')
for c in range(1, 5):

    print(f'Informações da {c}º pessoa')
    nome_atual = str(input('Digite seu nome: ')).capitalize().strip()
    idade_atual = int(input('Digite sua idade: '))
    sexo = str(input('Digite seu sexo(F ou M): ')).upper().strip()
    print('Obrigado(a) pelas informações.\n')

    media += idade_atual

    if c == 1:#Amarzenamento da primeira pessoas para comparação com as procimas
        nome_anterior = nome_atual
        idade_anterior = idade_atual
    if idade_atual > idade_anterior and sexo == "M":#nome e idade do homen mais velho
        idade_anterior = idade_atual
        nome_anterior = nome_atual
    if sexo == "F":#contagem de mulheres
        tot_mulheres += 1
    if sexo == "M":#contagem de homens
        tot_homens += 1
    if sexo == "F" and 20 > idade_atual:#contagem de mulheres menores de 20 anos
        tot_menorque20 += 1

media = media / 4
if tot_mulheres == 4:#SE a pesquisa tiver só mulheres
    print('Não há homem na pesquisa.')
    if tot_menorque20 == 1:#mulher no singular
        print(f'Há {tot_menorque20} mulher menor que 20 anos.')
        print(f'A media de todas as idades é de {media:.1f}.')
    else:#mulher no plural
        print(f'Há {tot_menorque20} mulheres menor que 20 anos.')
        print(f'A media de todas as idades é de {media:.1f}.')

elif tot_homens == 4:#SE a pesquisa tiver só homens
    print(f'O homem mais velho é {nome_anterior} com {idade_anterior} anos.')
    print(f'Não há mulheres na pesquisa.')
    print(f'A media de todas as idades é de {media:.1f}.')

else:
    print(f'O Homem mais velho é {nome_anterior} com {idade_anterior} anos.')
    if tot_menorque20 == 1:#mulher no singular
        print(f'Há {tot_menorque20} mulher menor que 20 anos.')
        print(f'A media de todas as idades é de {media:.1f}.')
    else:#mulher no plural
        print(f'Há {tot_menorque20} mulheres menor que 20 anos.')
        print(f'A media de todas as idades é de {media:.1f}.')
