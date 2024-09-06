n = int(input('Digite um numero: '))
print(f'A tabuada do numero {n} é:')
print(12*'_')
for x in range(0, 11):
    print(f'{n} X {x:2} = {n*x}')
print(12*'_')
