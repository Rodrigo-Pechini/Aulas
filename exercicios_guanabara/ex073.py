tabela = ('Flamengo', 'Palmeiras', 'Atlético Mineiro', 'São Paulo', 'Fluminense',
          'Vasco', 'Grêmio', 'Internacional', 'Corinthians', 'Santos', 'Botafogo',
          'Atlético Paranaense', 'Cruzeiro', 'Bragantino', 'Ceará', 'Bahia',
          'Fortaleza', 'Goiás', 'Atlético Goianiense', 'Chapecoense', 'América Mineiro'
          )
print(50 * '-=')
print(f'AQUI ESTA A TABELA DO BRASILEIRÃO 2024\n{tabela}')
print(50 * '-=')
print(f'AQUI ESTÃO OS 5 PRIMEIROS NO BRASILEIRÃO 2024\n{tabela[0:5]}')
print(50 * '-=')
print(f'AQUI ESTÃO OS 4 ULTIMOS COLOCADOS DO BRASILEIRÃO 2024\n{tabela[-4:]}')
print(50 * '-=')
print(f'AQUI ESTA A TABELA ORGANIZADA EM ORDEM ALFABETICA\n{sorted(tabela)}')
print(50 * '-=')
print(f'A CHAPECOENCE ESTA EM {tabela.index("Chapecoense") + 1}º NA TABELA')
