import random
import os

def numeros_sorteados(lista_sorteados):
    print('\n=================')
    print("NUMEROS QUE JA FORAM SORTEADOS: \n")
    print(lista_sorteados)
    print('=================\n')
    print('Total de numeros sorteados: ', len(lista_sorteados))
    print('=================\n')

def main():
    sorteados = []
    p = int(input("Numero de participantes? "))
    lista = list(range(1,p+1))
    print(lista)
    while True:
        opcao = int(input("1) ALTERAR NUMERO TOTAL DE PARTICIPANTES\n2) SORTEAR UM NUMERO\n3) Sair \n\n"))
        os.system('clear')
        if opcao == 1:
            p = int(input("\nQuantas participantes? "))
            os.system('clear')
        if opcao == 2:
            if(len(lista) > 0):
                s = random.SystemRandom().choice(lista)
                sorteados.append(s)
                lista.remove(s)
                print('NUMERO SORTEADO: ', s)
                if len(sorteados) == p:
                    print("Todos números já sorteados :)")
                    numeros_sorteados(sorteados)
                    break
            numeros_sorteados(sorteados)
        if opcao == 3:
            break

if __name__ == '__main__':
    main()
