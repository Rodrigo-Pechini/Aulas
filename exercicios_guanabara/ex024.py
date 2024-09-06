local = str(input('Em qual cidade você nasceu? ')).strip()

minu = local.lower()
titu = minu.title()
santo = 'Santo' in titu

print(f'Sua cidade tem Santo? {santo}')
