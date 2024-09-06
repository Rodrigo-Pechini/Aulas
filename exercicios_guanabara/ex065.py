opcao = ''
n = cont = media = num_maior = num_menor = 0

while not opcao == 'N':

    cont += 1
    n = int(input('Digite um numero: '))
    opcao = str(input('Quer continuar?[N/S] ')).upper().strip()[0]
    media += n
    if cont == 1:
        num_maior = n
        num_menor = n
    else:
        if num_maior < n:
            num_maior = n
        if num_menor > n:
            num_menor = n

media /= cont
print(f'Você digitou {cont} numeros e sua media é de {media:.2f}')
print(f'O menor numero digitado foi {num_menor} e o maior foi {num_maior}')
