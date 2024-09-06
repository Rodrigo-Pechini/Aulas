lugar = input('Aonde você esta agora? ')
temp = float(input(f'Informe a temperatura de {lugar} em ºC: '))
f = temp * (9/5) + 32
print(f'O {lugar} esta com {temp}ºC que tambem corresponde a {f}ºF')
