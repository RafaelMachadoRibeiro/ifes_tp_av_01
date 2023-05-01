import random

#1º Função
def ver (i,j,n):
    if(i>=0 and j>=0 and n>=0):
        if(i<n and j<n and i<j and n<=100):
            return True

#2º Função
def list (n):
    lista = []
    for i in range (n):
        num = random.randrange(0,100)
        lista.append(num)
    return lista

#3º Função
def troc (i,j,lista):
    aux = lista[i-1]
    lista[i-1] = lista[j-1]
    lista[j-1] = aux
    return lista

#Programa principal
i = int(input('Digite o valor de i: '))
j = int(input('Digite o valor de j: '))
n = int(input('Digite o valor de n: '))

fun_1 = ver(i,j,n)
if (fun_1 == True):
    fun_2 = list(n)
    print(fun_2)
    print(troc(i,j,fun_2))
else:
    print('Valores inválidos na entrada de dados')