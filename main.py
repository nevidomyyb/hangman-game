from lib import arquivo
from lib import game
from os import system
import time

config = 'config.txt'
# checa e cria os arquivos de configuração
if not arquivo.arquivoExiste(config):
    arquivo.arquivoCriar(config)


# inicia o menu e suas funcionalidades
while True:

    print('-'*42)
    print('JOGO DA FORCA'.center(42))
    print('-'*42)
    print(f'{arquivo.amarelo}1{arquivo.original} menu registros')
    print(f'{arquivo.amarelo}2{arquivo.original} iniciar jogo')
    print(f'{arquivo.amarelo}3{arquivo.original} sair')
    print('-'*42)
    print(f'{arquivo.ciano}sua opção{arquivo.original}: ')
    try:
        opc = int(input(''))
    except:
        print('Apenas números são aceitos')
    else:
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
                try:
                    opt = int(input(''))

                except:
                    print('Apenas números são aceitos')
                else:
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
            game.startGame(config)
        elif opc == 3:
            print(f'{arquivo.ciano}finalizando{arquivo.original}')
            break
        else:
            print(f'{arquivo.ciano}opção inválida{arquivo.original}')
