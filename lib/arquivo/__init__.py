from string import ascii_lowercase

vermelho = '\033[31m'
verde = '\033[32m'
azul = '\033[34m'
ciano = '\033[36m'
magenta = '\033[35m'
amarelo = '\033[33m'
preto = '\033[30m'
branco = '\033[37m'
original = '\033[0;0m'


def arquivoExiste(arquivo):
    try:
        a = open(arquivo, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def arquivoCriar(arquivo):
    try:
        a = open(arquivo, 'wt+')
    except:
        print('falha ao criar arquivo')
    else:
        a.close()
        print(f'arquivo {arquivo} criado com sucesso')


def registrarPalavra(arquivo):
    validos = ascii_lowercase + ' a_'
    try:
        a = open(arquivo, 'at')
    except:
        print('falha ao registrar palavra')
    else:
        while True:
            word = input('Palavra: ').replace(' ', '_')
            if all(c in validos for c in word):
                if not verificarExistencia(word, arquivo):
                    a.write(f'{word}\n')
                    a.close()
                    break
                else:
                    print('palavra já registrada')
            else:
                print('palavra inválida')


def verificarExistencia(palavra, arch):
    arch = open(arch, 'rt')
    lista = arch.readlines()
    for i, v in enumerate(lista):
        lista[i] = v.replace('\n', '')
    if palavra in lista:
        return True
    else:
        return False


def header(msg):
    print('-'*42)
    print(f'{msg}'.center(42))
    print('-'*42)


def palavrasRegistradas(arquivo):
    a = open(arquivo, 'rt')
    lista = a.readlines()
    palavras = list()
    for i, v in enumerate(lista):
        p = v.replace('\n', '').replace('_', ' ')
        print(p)
