num = int(input('Digite um numero ente 0 até 9999: '))

u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print(f'ANALIZANDO O NUMERO {num}')
print(f'Sua unidade é: {u}')
print(f'Sua desena é: {d}')
print(f'Sua centena é: {c}')
print(f'Seu milhar é: {m}')
