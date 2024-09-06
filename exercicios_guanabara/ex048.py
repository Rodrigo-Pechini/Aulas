soma = 0 #a soma de todos os numeros multiplos de 3
cont = 0 #quantas vezes o for rodou
for x in range(1, 500, 2):
    if x % 3 == 0:
        soma = soma + x
        cont = cont + 1
print(f'A soma de {cont} valores é {soma}')
