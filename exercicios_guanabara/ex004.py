n = input('Digite algo: ')
print(f'O tipo primitivo desse valor é {type(n)}')
print(f'Contem só espaços? {n.isspace()}')
print(f'Contem só numero? {n.isnumeric()}')
print(f'Contem só letra? {n.isalpha()}')
print(f'Ele é alfanumerico? {n.isalnum()}')
print(f'Esta em letras mainusculas? {n.islower()}')
print(f'Esta em letras maiusculas? {n.isupper()}')
print(f'Esta capitalizado? {n.istitle()}')
