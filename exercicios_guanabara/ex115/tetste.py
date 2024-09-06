from time import sleep
import interface
import dados
import cores

arq = 'Arquivo.txt'

if not dados.aquivoExiste(arq):
    dados.criarArquivo(arq)

while True:
    sleep(0.5)
    interface.menu()
    n = interface.opcao(f'{cores.verde()}Digite uma opção:{cores.limpo()} ')
    if n == 2:
        sleep(0.5)
        interface.Titulo('CADASTRO DE PESSOA')
        sleep(0.5)
        dados.CadastrarNome(f'{cores.verde()}Digite o nome:{cores.limpo()} ')
        dados.CadastrarIdade(f'{cores.verde()}Digite a idade:{cores.limpo()} ')
        print(f'{cores.azul()}Pessoa cadastrada{cores.limpo()}')
    elif n == 1:
        sleep(0.5)
        interface.Titulo('PESSOAS CADASTRADAS')
        sleep(0.5)
        interface.lerArquivo(arq)

    else:
        break

interface.Titulo('PROGRAMA FINALIZADO')
