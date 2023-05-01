import random

#1º função
def gerar_lista (n):
    lista = []
    for i in range(n):
        num = random.randint(0, 100)
        lista.append(num)
    return lista

#2º função
def acumu (list_normal,n):
    list_acumu = []
    acumu = 0
    for i in list_normal:
        acumu += i
        list_acumu.append(acumu)
    return list_acumu

#Programa principal
n = int(input('Digite o valor de N: '))
fun_1 = gerar_lista(n)
print(fun_1)
fun_2 = acumu(fun_1,n)
print(fun_2)