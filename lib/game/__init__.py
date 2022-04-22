import random


def escolherPalavra(arquivo):
    a = open(arquivo, 'rt')
    lista = a.readlines()
    listaR = list()
    for i, v in enumerate(lista):
        p = v.replace('\n', '').replace('_', ' ')
        listaR.append(p)
    choice = listaR[random.randint(0, len(listaR) - 1)]
