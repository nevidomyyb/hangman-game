import random
from lib import arquivo
from string import ascii_lowercase


def escolherPalavra(arquivo):
    # system to pick a word from config.txt
    a = open(arquivo, 'rt')
    lista = a.readlines()
    listaR = list()
    for i, v in enumerate(lista):
        p = v.replace('\n', '').replace('_', ' ')
        listaR.append(p)
    choice = listaR[random.randint(0, len(listaR) - 1)]
    return choice


def startGame(arquivo):
    # start the game
    validos = ascii_lowercase + ' a'
    acertos = list()
    pos = list()
    dicti = dict()
    escolha = escolherPalavra(arquivo)
    escolhaS = escolha

    if escolha.count(' ') > 0:
        tamanho = len(escolha) - escolha.count(' ')
    else:
        tamanho = len(escolha)

    for c in range(0, tamanho):
        dicti[c] = '_'

    while True:
        if len(acertos) == 0:
            for c in dicti.values():
                print(c, end=' ')
            print()
        else:
            print()

        while True:
            chute = str(input('Digite a letra: '))
            if len(chute) > 1:
                print('Apenas uma letra é permitido')
            elif chute not in validos:
                print('Caractere inválido')
            else:
                break

        if chute in escolha:
            if chute in acertos:
                print('Letra já encontrada')
            else:
                print('Letra encontrada!')
                acertos.append(chute)
        else:
            print('Errou!')

        print(dicti)
        print(tamanho)
        print(escolha)
        print(escolhaS)
        print(acertos)
