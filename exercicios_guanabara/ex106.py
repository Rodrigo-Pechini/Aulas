from time import sleep

def escreva(msg):
    tam = len(msg) + 4
    print('-' * tam)
    print(f'  {msg}')
    print('-' * tam)


while True:
    escreva('SISTEMA DE AJUDA PyHELP')
    pergunta = str(input("Função ou Biblioteca: ")).capitalize()
    if pergunta == 'Fim':
        break
    escreva(f"Acessando o manual do comando '{pergunta}'")
    sleep(1)
    print(help(pergunta))
