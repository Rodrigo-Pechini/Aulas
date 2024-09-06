nome = str(input('Qual é seu nome? ')).strip()

maiu = nome.upper()
titu = maiu.title()
silva = 'Silva' in titu

print(f'Seu nome tem Silva? {silva}')
