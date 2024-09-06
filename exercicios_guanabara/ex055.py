peso_menor = 0
peso_maior = 0
for c in range(5):
    peso = float(input(f'Qual é o pesso da {c + 1}º pessoa em Kg: '))

    #if peso_menor == 0 and peso_maior == 0: meu jeito
    if c == 1: # jeito do curso
        peso_menor = peso
        peso_maior = peso
    elif peso > peso_maior:
        peso_maior = peso
    elif peso < peso_menor:
        peso_menor = peso

print(f'peso maior {peso_maior:.1f}Kg')
print(f'Peso menor {peso_menor:.1f}Kg')
