from lib import arquivo
from lib import game
from os import system
import time

config = 'config.txt'
score = 'score.txt'

# function to clear terminal


def clear(): return system('cls')


# check if config and score exist
if not arquivo.arquivoExiste(config):
    arquivo.arquivoCriar(config)

if not arquivo.arquivoExiste(score):
    arquivo.arquivoCriar(score)

game.listarPalavras(config)

# start menus and functionalities
while True:
    # clear()
    print('-'*42)
    print('JOGO DA FORCA'.center(42))
    print('-'*42)
    print(f'{arquivo.amarelo}1{arquivo.original} menu registros')
    print(f'{arquivo.amarelo}2{arquivo.original} sair')
    print('-'*42)
    print(f'{arquivo.ciano}sua opção{arquivo.original}: ')
    opc = int(input(''))
    time.sleep(1)
    if opc == 1:
        while True:
            time.sleep(1)
            arquivo.header('MENU REGISTROS')
            print(f'{arquivo.amarelo}1{arquivo.original} registrar palavra')
            print(f'{arquivo.amarelo}2{arquivo.original} ver palavras registradas')
            print(f'{arquivo.amarelo}3{arquivo.original} deletar palavra')
            print(f'{arquivo.amarelo}4{arquivo.original} sair')
            print(f'{arquivo.ciano}sua opção{arquivo.original}: ')
            opt = int(input(''))
            if opt == 1:
                arquivo.registrarPalavra(config)
            elif opt == 2:
                arquivo.palavrasRegistradas(config)
            elif opt == 3:
                arquivo.excluirPalavra(config)
            elif opt == 4:
                print(f'{arquivo.ciano}saindo{arquivo.original}')
                break
            else:
                print(f'{arquivo.ciano}opção inválida{arquivo.original}')
                time.sleep(1)
    elif opc == 2:
        print(f'{arquivo.ciano}finalizando{arquivo.original}')
        break
    else:
        print(f'{arquivo.ciano}opção inválida{arquivo.original}')
