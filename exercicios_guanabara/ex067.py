cont = 0
while True:

    n = int(input('Quer ver a tabuada de qual valor: '))
    print('-' * 20)
    if n > 0:
        print(f'A tabuada do numero {n} é:')
        while not cont == 10:
            cont += 1
            print(f'{n} X {cont:2} = {n * cont}')
        if cont == 10:
            cont = 0
    else:
        break
    print('-' * 20)

print('Programa de tabuada encerrado.'
      'Volte sempre.')
