#não tem problema de ordem de avogal
#ex: 'cidade' = i a e

palavra = ("cachorro", "livro", "montanha", "mariposa", "relogio",
           "musica", "chave", "cidade", 'floresta', "teclado")

for p in palavra:
    print(f'\nNa palavra {p.upper()} encontramos: ', end='')

    # cada palavra da tupla(palavras) é uma lista de letras, então por exemplo:
    #"livro" o 'L' encontra na posisão [0] e sucesivamente.

    for letras in p:
        # se tiver 'aeiou' na letras(palavra) ele vai printar
        #  ele vai printar a avogal desta letra
        if letras.lower() in 'aeiou':
            print(letras, end=' ')
