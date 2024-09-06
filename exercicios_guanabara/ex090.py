aluno = {}

aluno['nome'] = str(input('Nome do aluno: ')).capitalize()
aluno['media'] = float(input('Media a do aluno: '))

if aluno['media'] <= 5:
    aluno['situação'] = 'Reprovado'
elif aluno['media'] <= 7:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Aprovado'

print(f'O nome do aluno é {aluno["nome"]}.'
      f'\nSua media é de {aluno["media"]}.'
      f'\nE ele foi {aluno["situação"]}.')
