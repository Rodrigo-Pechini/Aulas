print('Sequência de Fibonacci')
print(20 * '~')
n = int(input('Quantos termos você quer mostras: '))

a = 0
b = 1

while n != 0:

    proximo = a + b
    if a == 0:
        print(f'{a} - {b}', end=' - ')
    print(proximo, end=' - ')
    b = a
    a = proximo
    n -= 1

print('FIM')
