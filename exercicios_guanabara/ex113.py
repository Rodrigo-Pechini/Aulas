def leiaint(msg):
    while True:
        try:
            valor = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO! Digite um numero inteiro valido.\033[m')
        except KeyboardInterrupt:
            print('\n\033[31mO usuario preferiu não digitar esse numero\033[m')
            return 0
        else:
            break
    return valor

def leiaflo(msg):
    while True:
        try:
            valor = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO! Digite um numero real valido.\033[m')
        except KeyboardInterrupt:
            print('\n\033[31mO usuario preferiu não digitar esse numero\033[m')
            return 0
        else:
            break
    return valor


inteiro = leiaint('Digite um numero inteiro: ')
flutu = leiaflo('Digite um numero real: ')
print(f'O valor inteiro digitado foi de {inteiro} e real {flutu}')
