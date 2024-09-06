dias = int(input('Quantos dias você ficou com o carro? '))
km = int(input('Quantos Km você rodou com o carro? '))
aluguel = dias * 60
km_rodado = km * 0.15
total = aluguel + km_rodado
print(f'Sabendo que cada dia com o carro custa 60R$ e cada Km rodado custa 0,15c.'
      f' \nVocê deve pagar no total de {total:.2f}R$.')
