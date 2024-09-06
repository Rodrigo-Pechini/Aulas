from cores import *

arq = 'Arquivo.txt'


def CadastrarIdade(idade):
    while True:
        try:
            ano = int(input(idade))
        except (ValueError, TypeError):
            print(f'{vermelho()}ERRO! Digite um valor valido.{limpo()}')
        else:
            ano = str(ano)
            with open(arq, 'a') as arquivo:
                arquivo.write(f'{ano}\n')
            break


def CadastrarNome(nome):
    while True:

        pessoa = str(input(nome)).capitalize()
        if pessoa.isnumeric():
            print(f'{vermelho()}ERRO! Digite um valor valido.{limpo()}')
        else:
            with open(arq, 'a') as arquivo:
                arquivo.write(f'{pessoa};')
            break


def aquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print(f'{vermelho()}Houve um ERRO na criação do arquivo{limpo()}')
    else:
        print(f'Arquivo {nome} criado com sucesso.')
