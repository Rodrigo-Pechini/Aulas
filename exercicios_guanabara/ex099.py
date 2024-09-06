from time import sleep


def maior(*num):
    print('=-' * 20)
    print('Analizando valores...')
    mai = 0
    if len(num) > 0:
        for e, n in enumerate(num):
            print(n, end=' ')
            sleep(0.5)
            if e == 0:
                mai = n
            else:
                if n > mai:
                    mai = n
        print(f'Foram encontrado {e + 1} valores ao todo\nO maior valor encontrado foi {mai}')
    else:
        print(f'foram encotrado {len(num)} valores ao todo\nO maior valor encontrado foi 0')


maior(2, 4, 7, 8, 2, 6)
maior(5, 2, 9, 3)
maior(1, 2)
maior(6)
maior()
