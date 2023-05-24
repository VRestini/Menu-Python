"""Em todos os exercicios que envolva mais de um segundo vetor, o segundo deve ser inicializado com
todas as posições zeradas.
    lista1 = [41, 72, 39, 4, 35]
    lista2 = [0, 0, 0, 0, 0]
1. Fazer um procedimento chamado 'copia_vetor(v1, v2)' que copie os elementos do vetor v1 em v2.
2. Fazer um procedimento chamado 'inverte_vetor(v1, v2)' que copie os elementos invertidos do vetor v1
em v2, ou seja, o primeiro elemento de v1 será o último de v2...
    lista1 = [41, 72, 39, 4, 35]
    lista2 = [35, 4, 39, 72, 41]
3. Fazer um procedimento chamado 'ordena_vetor_crescente(v)' que ordene em ordem crescente o vetor
passado por parâmetro.
4. Fazer um procedimento chamado 'ordena_vetor_decrescente(v)' que ordene em ordem decrescente o
vetor passado por parâmetro.
5. Fazer um procedimento chamado 'ordena_vetor(v, forma)' que baseado na forma ('c' para crescente
ou 'd' para decrescente) ordene na ordem solicitada.
6. Fazer um procedimento chamado 'separa_vetor(v)' que coloque nas posições mais a direita os valores
pares e mais a esquerda os impares.
    lista1 = [4, 72, 39, 41, 35]
7. Fazer uma função chamada 'conta_acima_media(v) que retorne quantos elementos do vetor estão
acima da média.
8. Fazer uma função chamada 'maior_elemento(v)' que retorne o elemento de maior valor do vetor.
9. Fazer uma função chamada 'busca_vetor(v, valor) que retorne True caso o valor seja encontrado
em v, senão retorne False.
"""

v1 = [ 41, 72, 39, 4, 35]
v2 = [0, 0, 0, 0, 0]
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
    v2 = v1
    print (v2)
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

print(busca_vetor(v1, 35))