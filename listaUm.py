v = [34, 6, 57, 3, 45, -10, 5]

def ordenar(vetor: list) -> list:
    return print(sorted(vetor))


def exista(vetor: list, n1: int) -> bool:
    for i in range(len(vetor)):
        if n1 == v[i]:
            return True
        else:
            return False

def primeiro_elem(vetor: list) -> int:
    return v[0]

def negativo_elem(vetor: list) -> None:
    for i in range(len(vetor)):
        if v[i] < 0:
            print(v[i])

def soma_elem(vetor: list) -> int:
    soma = 0
    for i in vetor:
        soma = soma + i
    return soma

def media_elem(vetor: list) -> float:
    soma = 0
    for i in vetor:
        soma = soma + i
    return soma / len(v)

def impar_elem(vetor: list) -> None:
    for i in range(len(vetor)):
        if (v[i] % 2 != 0):
            print("ímpar: ", v[i])

def prim_ulti_elem(vetor: list) -> None:
    ultimo = len(vetor)
    primeiro = v[0]
    print(primeiro, v[ultimo - 1])

def indice_par_elem(vetor: list) -> None:
    for i in range(len(vetor)):
        if i % 2 == 0:
            print(v[i])
