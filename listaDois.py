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

v1 = [41, 72, 39, 4, 35]
v2 = [0, 0, 0, 0, 0]
def copia_vetor(vetor1, vetor2: list) -> list:
    v2 = v1
    print (v2)
def inverte_vetor(vetor1, vetor2: list) -> list:
    v2 = v1
    exi = list(reversed(v2))
    print(exi)
def ordena_vetor_crescente(vetor1: list) -> list:
    print(sorted(vetor1))

def ordena_vetor_decrescente(vetor1: list) -> list:
    print(sorted(vetor1, reverse = True))

copia_vetor(v1, v2)
inverte_vetor(v1, v2)
ordena_vetor_crescente(v1)
ordena_vetor_decrescente(v1)