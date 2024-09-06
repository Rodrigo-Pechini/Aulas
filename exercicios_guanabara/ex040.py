nome = str(input('Digite o nome do alundo: '))
n1 = float(input('Primeira nota: '))
n2 = float(input(('Segunda nota: ')))

nota = (n1 + n2) / 2

if nota >= 7.0:
    print(f'A nota do aluno {nome} foi de {nota:.1f}, aluno APROVADO.')
elif nota < 5.0:
    print(f'A nota do aluno {nome} foi de {nota:.1f}, aluno REPROVADO.')
else:
    print(f'A nota do aluno {nome} foi de {nota:.1f}, aluno em RECUPERAÇÃO.')
