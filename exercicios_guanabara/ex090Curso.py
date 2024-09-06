aluno = {}

aluno['nome'] = str(input('Nome: ')).capitalize()
aluno['media'] = float(input(f'Media de {aluno["nome"]}: '))

if aluno['media'] <= 5:
    aluno['situação'] = 'Reprovado'
elif aluno['media'] <= 7:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Aprovado'

for k, v in aluno.items():
    print(f'--{k} é iqual {v}')
