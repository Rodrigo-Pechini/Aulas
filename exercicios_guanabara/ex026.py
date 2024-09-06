frase = str(input('Digite uma frase: ')).strip().lower()

quant = frase.count('a')
inicio = frase.find('a') + 1
ultima = frase.rfind('a') + 1

print(f'Sua frase: {frase} \ntem {quant} letas A')
print(f'A primeira letra A aparece na posição {inicio}')
print(f'A ultima letra A aparece na posção {ultima}')
