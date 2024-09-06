n = 0
a = 0
cont = 0 - 1
while n != 999:

    cont += 1
    a += n
    n = int(input('Digite um numero [para parar digite 999]: '))

print(f'Foram digitados {cont} numeros e a soma entre eles é {a}')
