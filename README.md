# Aulas de python
***
Realizei o um curso de python com o professor Gustavo Guanabara do [Curso em video](https://www.youtube.com/c/CursoemVídeo).
Foi uma experiência indescritivel, além de aprender a linguagem python foi me ensinado logica de programção.

## O que aprendi exatamente
* Algoritimos e logica de programação.
***
* Interação com o usuario e variaveis
````
nome = input('Qual é seu nome? ')
print(f'ola, {nome}')
````
***
* Estrutura de condições.
Neste código tem uma entrada de um numero pelo usuario e depois um menu para converter este valor em binario, octal e hexadecimal.
````
num = int(input('Digite um numero: '))

print('[ 1 ] converter para BINARIO.')
print('[ 2 ] converter para OCTAL.')
print('[ 3 } converter para HEXADECIMAL.')

escolha = int(input('Sua opção: '))

if escolha == 1:
   print(bin(num)[2:])
elif escolha == 2:
   print(oct(num)[2:])
elif escolha == 3:
   print(hex(num)[2:])
else:
   print('Opção invalida.')
````
***
* Utilizar bibliotecas.
Neste código entrara 4 nomes de alunos e guardara em uma lista, utilizando a biblioteca random com a função shuffle para embaralhar a ordem dos nomes.
````
from random import shuffle

n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Segundo aluno: '))
n4 = str(input('Terceiro aluno: '))
lista = [n1, n2, n3, n4]
shuffle(lista)
print('A ordem de apresentação sera:')
print(lista)

````
***
* Loops.
Neste código vai registrar o nome e sexo da pessoa, porém se ela digitar o sexo errado( F/M ) o programa retorna um erro e pede para digitar novamente.
````
#meu programa não tem problema com a resposta vazia

nome = str(input('Qual é seu nome? ')).capitalize().strip()

soma = 0#para quebra do loop
sexo = ''#quardar o valor que o user digitou no caso "F" ou "M"

while soma == 0:#se soma for ainda 0 o whuile ainda vai continuar rodando
    sexo = str(input('Digite seu sexo [F/M]: ')).upper().strip()[0]#interção com o user
    if sexo == 'F' or sexo == 'M':
        soma += 1#adiciona 1 no soma q faz o lupe romper
    if soma == 0:
        print('Sexo invalido digite novamente')#caso o user erre a digitação

if sexo == 'F':
    print(f'Sexo do {nome} foi registrado como feminino.')
else:
    print(f'Sexo do {nome} foi regitrasdo como masculino.')

````
***
* Cores.
Neste código vai avaliar sua provação para um emprestimo para pagar sua casa, se for aprovado retorna alguns valores e um APROVADO em verde ou um NEGADO em vermelho
````
valor_casa = float(input('Qual é o valor da casa? '))
valor_salario = float(input('Qual é o valor do seu salario? '))
financiamento = int(input('Em quantos anos de financiamento? '))

parcelas = valor_casa / (financiamento * 12)
salario30 = valor_salario * 30 / 100
cores = {
    'limpa': '\033[m',
    'verde': '\033[32m',
    'vermelho': '\033[31m'
}

print(f'A casa que você vai comprar é de {valor_casa:.2f}R$, suas parecelas durnate {financiamento} anos'
      f'\n vai custar {parcelas:.2f}R$ por mês.')

if parcelas < salario30:
    print(f'Seu imprestimo foi {cores["verde"]}APROVADO{cores["limpa"]}.')
else:
    print(f'Seu imprestimo foi {cores["vermelho"]}NEGADO{cores["limpa"]}.')

````
***
* Tuplas, listas, dicionarios.
Neste código vai mostrar o desempenho de um jogador, com uma tabela simples com o nome, gols feitos, total de gols e outra tabela com as informações de
quantidade de partidas, gols em cada partida e numero total de gols.
````
dados = {}
num_gols = []
dados['nome'] = str(input('Nome do jogador: ')).capitalize()
partidas = int(input(f'Quantas partidas o {dados["nome"]} jogou? '))

totgols = 0
for c in range(0, partidas):
    gols = int(input(f'Quantos gols fez na {c + 1}º partida: '))
    totgols += gols
    num_gols.append(gols)
print('=-' * 20)
dados['gols'] = num_gols[:]
dados['total'] = totgols

for k, v in dados.items():
    print(f'O {k} tem como valor {v}.')
print('=-' * 20)
print(f'O jogador {dados["nome"]} jogou {partidas} partidas.')
for c in range(0, partidas):
    print(f'   ==>Na {c+1}º partida {dados["nome"]} fez {dados["gols"][c]}')
print(f'No total foram {dados["total"]} gols.')

````
***
* Funções.
Neste código foi criado uma função que vai retornar se a pessoa tem voto obrigatorio, não pode votar ou voto opcional.
````
#posso importar uma biblioteca na função, se for utilizar ela SÓ na função

def voto(data):
    from datetime import date
    global idade
    idade = date.today().year - data
    votar = ''
    if idade <= 15:
        votar = 'NÃO PODE VOTAR'
    elif idade > 61 or idade <= 17:
        votar = 'VOTAR É OPICIONAL'
    else:
        votar = 'VOTO OBRIGATORIO'
    return votar


idade = 0
ano = int(input('Em que ano você nasceu: '))
# estou chamando a função para alterar o valor da variavel idade
voto(ano)
print(f'Esta pessoa tem {idade} anos: {voto(ano)}')

````
***
* Modularização.
Neste código foi utilizado dois arquivos, um contendo só as funções e outro o codigo principal.
![Captura de tela 2024-09-06 155757](https://github.com/user-attachments/assets/591b33a2-ac16-4722-8ffa-ad5e7419c2b5)
***
* Tratamento de erros.
Neste código vai ocorre uma ferificação se o site [Pudim](https://www.pudim.com.br) esta acessível ou não
````
import urllib
import urllib.request

try:
    site = urllib.request.urlopen('https://www.pudim.com.br')
except:
    print('Este site não está acessivel no momento.')
else:
    print('Consegui acessar o site Pudim com sucesso.')
    print(site.read())

````
****
* Interação com arquivos.txt.
Neste código vai se criar um arquivo.txt se ele não existir e quardar dados dentro deste arquivo para quando você fechar o programa poder
utilizalos mais tarde.
![Captura de tela 2024-09-06 161513](https://github.com/user-attachments/assets/a95f8161-2237-4819-8258-16b49f47034f)
***
## Objetivos daqui para frente.
Agora com uma base solida sinto que posso prosseguir e continuar estudano.

Meu objetivo agora é dominar POO em python e depois seus frameworks.

Agora me encontro em um momentro crucial, pois python me abre varias portas para o ramo da tecnologia, mas no momento estou pensando em dados
pois python é dominante nesta área e me indentifiquei muito com esta linguagem, claro que vou estar sempre atualizados com outras linguagem e 
provavelmente aprenda outras, mas no momento me sinto mais competende com esta carreira e quem sabe mais para frente busco uma carreira backend.


