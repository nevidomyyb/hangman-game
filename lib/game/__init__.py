from string import ascii_lowercase
from lib import arquivo as arcs
from string import ascii_lowercase
import random

validos = ascii_lowercase + ' a'

#escolhe uma palavra aleatória do arquivo de configuração
def escolherPalavra(arquivo):
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

#verifica se o dicionario contém "_" se não, significa que a palavra está completa e venceu a rodada
def verificarVitoria(dicionario):
    lista = list()
    for c in dicionario.values():
        lista.append(c)    
    if "_" in lista:
        return False
    else:
        return True
#função de iniciar o jogo
def startGame(arquivo):
    escolha = escolherPalavra(arquivo)
    dicti = dict()
    tentativas = list()
    vida = 6
    #corrige ESPAÇOS e _ nas palavras
    tamanho = len(escolha)
    #mostra os traços e letras(caso já tenha acertado alguma)
    criarTraços(dicti, tamanho)

    #começa o sistema do jogo
    while True:
        #verifica se já venceu
        if verificarVitoria(dicti):
            print(f'{arcs.verde}VOCÊ VENCEU!'.center(48))
            print(f'{arcs.verde}PARABÉNS'.center(48))
            print(f'{arcs.original}')
            break
        else:
            #faz perder se tiver vida zerada
            if vida <= 0:
                print(f'{arcs.vermelho}VOCÊ PERDEU!'.center(48))
                print(f'BOA SORTE DA PRÓXIMA VEZ{arcs.original}'.center(48))
                
                break
            else:
                mostrarTraços(dicti)
                #recebe a letra digitada, verifica se já foi encontrada e se é correta para a palavra.
                while True:
                    chute = letra()
                    if not chute in tentativas:
                        if chute in escolha:
                            tentativas.append(chute)
                            print('Acertou!')
                            vida = vida + 1
                            print(f'{arcs.verde}Vida{arcs.original}:{arcs.azul} {vida}{arcs.original}')
                            break
                        else:
                            tentativas.append(chute)
                            print('Errou!')
                            vida = vida - 1
                            print(f'{arcs.verde}Vida{arcs.original}:{arcs.vermelho} {vida}{arcs.original}')        
                            break
                    else:
                        print('Letra já tentada')
                        break
                #posiciona a letra encontrada no dicionario na posição correta.
                for LA in tentativas:
                    if LA in escolha:
                        for pos, char in enumerate(escolha):
                            if char == LA:
                                dicti[pos] = LA 
                        