import random
from lib import arquivo
from string import ascii_lowercase

validos = ascii_lowercase + ' a'


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


def letra():
    while True:
        chute = str(input('Digite uma letra: '))
        if len(chute) > 1:
            print('Apenas uma letra por vez!')
        elif chute not in validos:
            print('Essa letra não é valida')
        else:
            break
    return chute


def criarTraços(dicionario, tamtam):
    for c in range(0, tamtam):
        dicionario[c] = '_'


def mostrarTraços(dicionario):
    for c in dicionario.values():
        print(f'{c}', end=' ')
    print()


def startGame(arquivo):
    # start the game
    escolha = escolherPalavra(arquivo)
    dicti = dict()
    acertos = list()

    #corrige ESPAÇOS e _ nas palavras
    if escolha.count(' ') > 0:
        tamanho = len(escolha) - escolha.count(' ')
    else:
        tamanho = len(escolha)

    criarTraços(dicti, tamanho)

    while True:
        if len(acertos) == 0:
            mostrarTraços(dicti)
    
        while True:
            chute = letra()
            if chute in escolha:
                if chute in acertos:
                    print('Letra já encontrada.')
                else:
                    print('Acertou!')
                    acertos.append(chute)
                    break
            else:
                print('Errou!')

        for LA in acertos:
            if LA in escolha:
                for pos, char in enumerate(escolha):
                    if char == LA:
                        dicti[pos] = LA 

        mostrarTraços(dicti)