import random

#1º função
def gerar_lista (n):
    lista = []
    for i in range(n):
        num = random.randint(0, 100)
        lista.append(num)
    return lista

#2º função
def calc (lista,n):
    #Média
    soma_list = sum(lista)
    med = soma_list / n
    #Variância
    variancia = sum([(x - med) ** 2 for x in lista]) / (n - 1)
    #Desvio padrão
    desvio = variancia ** 0.5
    return desvio

#Program principal
n = int(input('Digite o valor de N: '))

fun_1 = gerar_lista(n)
fun_2 = calc(fun_1,n)

print('O desvio padrão da lista é: {}'.format(fun_2))