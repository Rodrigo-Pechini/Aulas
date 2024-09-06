from cores import *


def menu():
    print()
    print('=' * 50)
    print(f'{verde()}MENU PRINCIPAL{limpo()}'.center(50))
    print('=' * 50)
    print(f'''
    {amarelo()}1 - {azul()}Ver pessoas cadastradas.{limpo()}
    {amarelo()}2 - {azul()}cadastrar uma nova pessoa.{limpo()}
    {amarelo()}3 - {azul()}sair do sistema.{limpo()}
    ''')
    print('=' * 50)


def opcao(msg):
    while True:
        try:
            valor = int(input(msg))
        except (ValueError, TypeError):
            print(f'{vermelho()}ERRO! Digite um valor valido.{limpo()}')
        else:
            if valor in (1, 2, 3):
                return valor
            else:
                print(f'{amarelo()}O valor {valor} não é coerente com as opções{limpo()}')
                continue


def Titulo(msg):
    print()
    print('=' * 50)
    print(f'{verde()}{msg}{limpo()}'.center(50))
    print('=' * 50)


def lerArquivo(nome):
    a = open(nome, 'tr')
    for linha in a:
        dados = linha.split(';')
        dados[1] = dados[1].replace('\n', '')
        print(f'{dados[0]:<40}{dados[1]:>3} anos')



"""def Tabela():
    if len(registros) > 0:
        for v in registros:
            for i in v.values():
                try:
                    if i.isalpha():
                        print(f'|Nome: {i}', end='')
                except AttributeError:
                    print(f'Idade: {i}')
    else:
        return print(f'{amarelo()}Nenhuma pessoa foi cadastrada{limpo()}')"""
