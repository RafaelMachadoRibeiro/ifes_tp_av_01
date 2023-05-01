import random

#Função 1
def list(n):
    lista = []
    for i in range (n):
        num = round (random.uniform (0,100),2)
        lista.append(num)
    return lista

#Função 2
def ord(lista,n):
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

#Programa principal
n = int(input('Digite o valor de N: '))

fun_1 = list(n)
print(fun_1)
fun_2 = ord(fun_1,n)
print(fun_2)