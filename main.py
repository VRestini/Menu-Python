from listaUm import *
from listaDois import *

tamanho = int(input("Digite o tamanho:"))
v = [0] * tamanho
v2 = [0] * tamanho
for i in range(len(v)):
    valor = int(input("Digite o valor:"))
    v[i] = valor

resp = 's'
while resp == 's' or resp == 'S':
    print("----- MENU -----")
    print("\n NÍVEL 1: \n 1- Primeiro elemento \n 2- Negativo \n 3- Soma \n 4- Média \n 5- Média \n 6- Pri e ult \n 7- Índice par \n 8- Ordenar \n 9- Exista")
    print("\n NÍVEL 2: \n 1- Copia o vetor \n 2- Inverte o vetor \n 3- Crescente \n 4- Decrescente \n 5- Ordem solicitada \n 6- Separa o vetor \n 7- Acima da média \n 8- Maior elemento \n 9- Busca vetor")
    nivel = int(input("Escolha o nível:"))
    while nivel != 1 and nivel != 2:
        print("Erro!")
        nivel = int(input("Escolha o nível:"))
    else:
        if nivel == 1:
            esc = int(input("Escolha o exercício:"))
            while esc != 1 and esc != 2 and esc != 3 and esc != 4 and esc != 5 and esc !=6 and esc != 7 and esc != 8 and esc != 9:
                print("Erro!")
                esc = int(input("Escolha o exercício:"))
            else:
                if esc == 1:
                    print("Mostrará o primeiro elemento do vetor v", v)
                    print(primeiro_elem(v))
                elif esc == 2:
                    print("Mostrará os valores negativos do vetor v", v)
                    negativo_elem(v)
                elif esc == 3:
                    print("Mostrará a soma dos valores do vetor v", v)
                    print(soma_elem(v))
                elif esc == 4:
                    print("Mostrará a média do vetor v", v)
                    print(media_elem(v))
                elif esc == 5:
                    print("Mostrará os valores ímpares do vetor v", v)
                    impar_elem(v)
                elif esc == 6:
                    print("Mostrará o primeiro e último elemento do vetor v", v)
                    prim_ulti_elem(v)
                elif esc == 7:
                    print("Mostrará os índices pares do vetor v", v)
                    indice_par_elem(v)
                elif esc == 8:
                    print("Mostrará os elemento ordenados do vetor v", v)
                    ordenar(v)
                else:
                    print("Mostrará seo número passado como parâmetro existe no vetor v", v)
                    n1 = int(input("Digite o valor aser passado como parametro: "))
                    print(exista(v, n1))
                resp = input("Deseja continuar:")
                while resp != 'S' and resp != 's' and resp != 'n' and resp != 'N':
                    print("Erro!")
                    resp = input("Deseja continuar:")
        elif nivel == 2:
            esc = int(input("Escolha o exercício:"))
            while esc != 1 and esc != 2 and esc != 3 and esc != 4 and esc != 5 and esc != 6 and esc != 7 and esc != 8 and esc != 9:
                print("Erro!")
                esc = int(input("Escolha o exercício:"))
            else:
                if esc == 1:
                    print("Copia os elementos dos vetores v1", v)
                    copia_vetor(v,v2)
                elif esc == 2:
                    print("copia os elementos invertidos nos vetores v", v)
                    inverte_vetor(v, v2)
                elif esc == 3:
                    print("Ordena em ordem crescente os elementos do vetor v", v)
                    ordena_vetor_crescente(v)
                elif esc == 4:
                    print("Ordena em ordem decrescente os elementos do vetor v", v)
                    print(ordena_vetor_decrescente(v))
                elif esc == 5:
                    print("Mostrará os valores em ordem do vetor v", v)
                    n1 = input("Digite a ordem:")
                    while n1 not in ['c', 'C', 'd', 'D']:
                        print("Erro!")
                        n1 = input("Digite novamente: ")
                    print(ordena_vetor(v, n1))
                elif esc == 6:
                    print("Organiza os ímpares na esquerda e os pares na direita do vetor v", v)
                    separa_vetor(v)
                elif esc == 7:
                    print("retorna quais elementos estam acima da media do vetor v", v)
                    conta_acima_media(v)
                elif esc == 8:
                    print("mostra o  maior elemento do vetor v", v)
                    print(maior_elemento(v))
                else:
                    print("Mostrará seo número passado como parâmetro existe no vetor v", v)
                    n1 = int(input("Digite o valor a ser passado como parametro: "))
                    print(busca_vetor(v, n1))
                resp = input("Deseja continuar:")
                while resp != 'S' and resp != 's' and resp != 'n' and resp != 'N':
                    print("Erro!")
                    resp = input("Deseja continuar:")
