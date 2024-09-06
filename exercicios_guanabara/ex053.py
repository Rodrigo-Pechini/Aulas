frase = str(input('Digite uma frase: ')).upper().strip().split()
junto = ''.join(frase)
inverso = ''

#ex: RODRIGO, o primeio -1 indica o inicio no 'O', o segundo -1  indica que o programa
#tem que terminar o ciclo(letra) nome -1 e o terceiro -1 faz com que o progra leia do 'O' até 'R'

for letra in range(len(junto) - 1, -1, -1):
    inverso = inverso + junto[frase]
print(junto, inverso,)

#O if vai ler a str do jeito normal(da esquerda para direita) e comparar elas.

if inverso == junto:
    print('TEMOS UM PALINDROMO')
else:
    print('NÃO É UM PALINDROMO')
#     OLA    PESSOA   LINDA    MUITO

''''m0 = 0
n1 = 1
print(frase[m0], end='')
print(frase[n1])'''
