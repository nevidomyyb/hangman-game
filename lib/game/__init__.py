import random
from lib import arquivo
from string import ascii_lowercase

validos = ascii_lowercase + ' a'

#escolhe uma palavra aleatória do arquivo de configuração
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

#sistema para perguntar a letra e verificar se é válido ou nao.
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

#cria os traços do tamanho da letra em um dicionario para ficar mais organizado
def criarTraços(dicionario, tamtam):
    for c in range(0, tamtam):
        dicionario[c] = '_'

#para mostrar as letras e traços
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
    #mostra os traços e letras(caso já tenha acertado alguma)
    criarTraços(dicti, tamanho)

    #começa o sistema do jogo
    while True:
        #se nenhuma letra foi acertada mostra os traços
        if len(acertos) == 0:
            mostrarTraços(dicti)
        #recebe a letra digitada, verifica ]///se já foi encontrada e se é correta para a palavra.
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
        #posiciona a letra encontrada no dicionario na posição correta.
        for LA in acertos:
            if LA in escolha:
                for pos, char in enumerate(escolha):
                    if char == LA:
                        dicti[pos] = LA 
        mostrarTraços(dicti)