from time import sleep

for segundos in range(10, -1, -1):
    if segundos == 0:
        print(f'Faltam {segundos} segundo para os fosgos')
    else:
        print(f'Faltam {segundos} segundos para os fogos')
    sleep(1)

print('*FOGOS EXPLODINDO*')
