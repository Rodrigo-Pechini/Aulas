nome = str(input('Digite seu nome completo: '))

#Forma do curso
print('ANALIZANDO SEU NOME')
print(f'Seu nome completo é {nome}.')
print(f'Seu nome com letras maiusculas {nome.upper()}.')
print(f'seu nome com letras minusculas {nome.lower()}.')
print(f'Seu nome tem no total de {len(nome) - nome.count(" ")} letras.')
print(f'Seu primeiro nome é {nome.split()[0]} e ele tem no total de {len(nome.split()[0])} letras.')


#meu jeito
'''nome_maiusculo = nome.upper()
nome_minusculo = nome.lower()
nome_primeiro1 = nome.split()
nome_primeiro2 = len(nome_primeiro1[0])
nome_numeros1 = len(''.join(nome_primeiro1))

print('ANALIZANDO SEU NOME...')
print(f'Seu nome completo é {nome}')
print(f'seu nome em letras maiusculas {nome_maiusculo}')
print(f'seu nome em letras minusculas {nome_minusculo}')
print(f'Seu nome tem no total de {nome_numeros1} letras')
print(f'Seu primeiro nome é {nome_primeiro1[0]} e ele tem {nome_primeiro2}')'''
