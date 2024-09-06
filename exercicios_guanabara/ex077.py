
#tem problema de ordem da avogal
#ex: 'cidade' = a e i

palavra = ("cachorro", "livro", "montanha", "mariposa", "relogio",
            "musica", "chave", "cidade", 'floresta', "teclado")

for c in range(0, len(palavra)):

    a = palavra[c].count('a') * 'a '
    e = palavra[c].count('e') * 'e '
    i = palavra[c].count('i') * 'i '
    o = palavra[c].count('o') * 'o '
    u = palavra[c].count('u') * 'u '

    avogais = a + e + i + o + u

    print(f'Na palavra {palavra[c].upper()} encontramos: {avogais}')
