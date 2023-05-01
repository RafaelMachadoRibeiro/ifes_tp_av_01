import random

#1º função
def list (n):
    lista = []
    for i in range(n):
        num = round (random.uniform (0,100),2)
        lista.append(num)
    return lista

#2º função 
def calc (lista,n):
    soma_list = sum(lista)
    media = soma_list / n
    
    list_cres = sorted(lista)
    if n % 2 == 0:
        mediana = (list_cres[n//2 - 1] + list_cres[n//2]) / 2
        return mediana
    else:
        mediana = list_cres[n//2]
        return lista,media,mediana       

#programa principal
n = int(input('Digite o valor de n: '))

fun_1 = list(n)
fun_2 = calc(fun_1,n)