print('Calculo fatorial')
n1 = int(input('Digite um numero: '))
n2 = 0
n3 = 0
soma = 0

while n1 != 1:

    if n1 > n3:
        n2 = n1 - 1
        n3 = n2 * n1
    else:
        n3 *= n2
    n1 -= 1
    n2 -= 1
    soma += 1
    print(n3)

print(soma)
print('acabou')
