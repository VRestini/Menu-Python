
def ordenar(vetor: list) -> list:
    aux = 0
    for i in range(len(vetor)):
        for a in range(len(vetor)):
            if vetor[i] < vetor[a]:
                aux = vetor[i]
                vetor[i] = vetor[a]
                vetor[a] = aux
    for i in range(len(vetor)):
        print(vetor[i])


def exista(vetor: list, n1: int) -> bool:
    for i in range(len(vetor)):
        if n1 == vetor[i]:
            return True
    if n1 != vetor[i]:
        return False

def primeiro_elem(vetor: list) -> int:
    return vetor[0]

def negativo_elem(vetor: list) -> None:
    for i in range(len(vetor)):
        if vetor[i] < 0:
            print(vetor[i])

def soma_elem(vetor: list) -> int:
    soma = 0
    for i in vetor:
        soma = soma + i
    return soma

def media_elem(vetor: list) -> float:
    soma = 0
    for i in vetor:
        soma = soma + i
    return soma / len(vetor)

def impar_elem(vetor: list) -> None:
    for i in range(len(vetor)):
        if (vetor[i] % 2 != 0):
            print("ímpar: ", vetor[i])

def prim_ulti_elem(vetor: list) -> None:
    ultimo = len(vetor)
    primeiro = vetor[0]
    print(primeiro, vetor[ultimo - 1])

def indice_par_elem(vetor: list) -> None:
    for i in range(len(vetor)):
        if i % 2 == 0:
            print(vetor[i])
