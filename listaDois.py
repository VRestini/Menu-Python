

def separa_vetor(vetor1: list) -> None:
    for i in range(0, len(vetor1)):
        if vetor1[i] % 2 == 0:
            for a in range(i, len(vetor1)):
                if vetor1[a] % 2 == 1:
                    aux = vetor1[i]
                    vetor1[i] = vetor1[a]
                    vetor1[a] = aux
    print(vetor1)




def copia_vetor(vetor1, vetor2: list) -> list:
    vetor2 = vetor1.copy()
    print(vetor2)
def inverte_vetor(vetor1, vetor2: list) -> list:
    a = -1
    for i in range(len(vetor2)):
        vetor2[i] = vetor1[a]
        a = a - 1
    print(vetor2)

def ordena_vetor_crescente(vetor1: list) -> list:
    aux = 0
    for i in range(len(vetor1)):
        for a in range(len(vetor1)):
            if vetor1[i] < vetor1[a]:
                aux = vetor1[i]
                vetor1[i] = vetor1[a]
                vetor1[a] = aux
    for i in range(len(vetor1)):
        print(vetor1[i])


def ordena_vetor_decrescente(vetor1: list) -> list:
    aux = 0
    for i in range(len(vetor1)):
        for a in range(len(vetor1)):
            if vetor1[i] > vetor1[a]:
                aux = vetor1[i]
                vetor1[i] = vetor1[a]
                vetor1[a] = aux
    for i in range(len(vetor1)):
        print(vetor1[i])


def ordena_vetor(vetor1: list, forma : str) -> None:

    if forma in ['c', 'C']:
        aux = 0
        for i in range(len(vetor1)):
            for a in range(len(vetor1)):
                if vetor1[i] < vetor1[a]:
                    aux = vetor1[i]
                    vetor1[i] = vetor1[a]
                    vetor1[a] = aux
        for i in range(len(vetor1)):
            print(vetor1[i])



    elif forma in ['d', 'D']:
        aux = 0
        for i in range(len(vetor1)):
            for a in range(len(vetor1)):
                if vetor1[i] > vetor1[a]:
                    aux = vetor1[i]
                    vetor1[i] = vetor1[a]
                    vetor1[a] = aux
        for i in range(len(vetor1)):
            print(vetor1[i])
    else:
        print("erro")


def conta_acima_media(vetor1: list) -> list:
    soma = 0
    for i in vetor1:
        soma = soma + i
    media = soma / len(vetor1)
    for i in range(len(vetor1)):
        if vetor1[i] > media:
            print(vetor1[i])

def maior_elemento(vetor1: list) -> int:
    aux = vetor1[0]
    for i in range(len(vetor1)):
        if vetor1[i] > aux:
            aux = vetor1[i]
    return(aux)

def busca_vetor(vetor1: list, n1: int) ->list:
    for i in range(len(vetor1)):
        if n1 == vetor1[i]:
            return True
    if n1 != vetor1[i]:
        return False

